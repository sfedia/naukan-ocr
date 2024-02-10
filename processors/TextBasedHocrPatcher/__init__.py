import os
import lxml.html
from difflib import SequenceMatcher
from lxml import etree


class TextBasedHocrPatcher:
    def __init__(self, hocr_input_dir, pages_input_dir, output_dir):
        self.hocr_input_dir = hocr_input_dir
        self.pages_input_dir = pages_input_dir
        self.output_dir = output_dir

    def patch(self):
        for dirname in (
                self.hocr_input_dir,
                self.hocr_input_dir,
                self.output_dir
            ):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        hocr_files_list = os.listdir(self.hocr_input_dir)
        page_files_list = os.listdir(self.pages_input_dir)
        map_hocr = {hocr_fn.rsplit(".", 1)[0]: hocr_fn for hocr_fn in hocr_files_list}
        map_pages = {page_fn.rsplit(".", 1)[0]: page_fn for page_fn in page_files_list}
        
        if map_hocr.keys() != map_pages.keys():
            raise ValueError("Cannot obtain page/hocr mapping!")
        
        total_lines = 0
        patched_lines = 0
        skipped_lines = 0

        for key in map_hocr:
            hocr_file_name = map_hocr[key]
            page_file_name = map_pages[key]
            t, p, s = self.patch_by_pair(hocr_file_name, page_file_name)
            total_lines += t
            patched_lines += p
            skipped_lines += s
        
        # TODO(sfedia): fix this
        total_lines = patched_lines + skipped_lines
        print(f"Total lines: {total_lines}")
        print(f"Patched lines: {patched_lines} ({'{:2f}'.format(patched_lines / total_lines * 100)}%)")
        print(f"Skipped lines: {skipped_lines} ({'{:2f}'.format(skipped_lines / total_lines * 100)}%)")

    

    def patch_by_pair(self, hocr_file_name, page_file_name):
        hocr_file = open(os.path.join(self.hocr_input_dir, hocr_file_name), "rb")
        hocr_content = hocr_file.read()
        hocr = etree.fromstring(hocr_content)
        ns = {"xhtml": "http://www.w3.org/1999/xhtml"}

        page = open(os.path.join(self.pages_input_dir, page_file_name)).read()
        # import ipdb; ipdb.set_trace();

        hocr_lines = hocr.xpath("//*[@class='ocr_line']")
        page_lines = page.splitlines()

        patched_lines = 0
        skipped_lines = 0

        hocr_line_pointer = 0
        page_line_pointer = 0
        l_page_lines = len(page_lines)
        l_hocr_lines = len(hocr_lines)

        while page_line_pointer < l_page_lines:
            i = hocr_line_pointer
            sel = i
            score = 0
            while i < l_hocr_lines:
                hocr_token_elems = hocr_lines[i].xpath(".//*[@class='ocrx_word']/xhtml:strong", namespaces=ns)
                concat = " ".join([el.text for el in hocr_token_elems])
                sim_score = SequenceMatcher(
                    None,
                    page_lines[page_line_pointer].lower(),
                    concat.lower()
                ).ratio()
                if sim_score > score:
                    sel = i
                    score = sim_score
                i += 1
            hocr_line_pointer = sel
            # print("page_line_pointer, hocr_line_pointer, sel:", page_line_pointer, hocr_line_pointer, sel)

            cur_hocr_token_elems = hocr_lines[sel].xpath(".//*[@class='ocrx_word']/xhtml:strong", namespaces=ns)
            cur_hocr_tokens = [el.text for el in cur_hocr_token_elems]
            cur_page_tokens = page_lines[page_line_pointer].split()

            # print("----")
            # print(cur_hocr_tokens)
            # print(cur_page_tokens)
            # print("----^^")

            if len(cur_hocr_tokens) != len(cur_page_tokens):
                print("Page/HOCR lengths aren't equal, skip")
                print("----")
                print(cur_hocr_tokens)
                print(cur_page_tokens)
                print("----^^")
                skipped_lines += 1
            else:
                for e, element in enumerate(hocr_lines[sel].xpath(".//*[@class='ocrx_word']/xhtml:strong", namespaces=ns)):
                    element.text = cur_page_tokens[e]
                print(f"Formatted line {sel}")
                patched_lines += 1
            page_line_pointer += 1
        

        with open(os.path.join(self.output_dir, hocr_file_name), "w") as file:
            file.write(lxml.html.tostring(hocr, encoding='unicode'))
            file.close()

        return l_hocr_lines, patched_lines, skipped_lines