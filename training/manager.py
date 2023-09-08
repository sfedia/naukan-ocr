#!/usr/bin/python3

import sys
import os
import json
import subprocess


folder = sys.argv[1]
action = sys.argv[2]


def unpack_positions(positions_argv):
    positions = []
    for part in positions_argv.split(","):
        if "-" not in part:
            positions.append(int(part))
        else:
            a, b = map(int, part.split("-"))
            positions.extend(range(a, b + 1))
    return positions


image_extensions = ("tif", "tiff", "jpg", "jpeg", "png")


os.chdir(folder)


# python3 manager.py nenl1985 create-boxes-index
if action == "create-boxes-index":
    if "boxes.json" in os.listdir("."):
        raise Exception(f"boxes.json already exists in {folder}!")

    with open("boxes.json", "w", encoding="utf-8") as boxes_json:
        boxes_json.write(json.dumps({}))
        boxes_json.close()
    
    print("Created boxes.json!")

# python3 manager.py nenl1985 make-boxes rus ynk 0,1-2
elif action == "make-boxes":
    source_lang = sys.argv[3]
    dest_lang = sys.argv[4]
    positions_argv = sys.argv[5]
    files_in_folder = os.listdir(".")
    positions = unpack_positions(positions_argv)
    print("Following positions will be processed:", positions)
    
    for pos in positions:
        relevant = [fn for fn in files_in_folder if fn.startswith(f"{dest_lang}.{folder}.exp{pos}.")]
        relevant_images = [fn for fn in relevant if fn.rsplit(".", 1)[-1] in image_extensions]

        if len(relevant_images) > 1:
            raise Exception("More than 1 image found for position:", relevant_images)
        elif len(relevant_images) == 0:
            raise Exception(f"No images found for position {pos}!")
        
        source_image = relevant_images[0]

        print(f"Creating box for position {pos}...")
        box_creation = subprocess.check_output(
            f"tesseract --oem 0 -l {source_lang} {source_image} {dest_lang}.{folder}.exp{pos} batch.nochop makebox",
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(box_creation.decode("utf-8"))
        box_index = json.loads(open("boxes.json", "r", encoding="utf-8").read())
        with open("boxes.json", "w", encoding="utf-8") as boxes_json:
            box_index[pos] = {
                "corrected": False
            }
            boxes_json.write(json.dumps(box_index, ensure_ascii=False, indent=2))
            boxes_json.close()

# python3 manager.py nenl1985 mark-as-corrected 0,1-2
elif action == "mark-as-corrected":
    positions_argv = sys.argv[3]
    positions = unpack_positions(positions_argv)
    for pos in positions:
        box_index = json.loads(open("boxes.json", "r", encoding="utf-8").read())
        with open("boxes.json", "w", encoding="utf-8") as boxes_json:
            box_index[str(pos)]["corrected"] = True
            boxes_json.write(json.dumps(box_index, ensure_ascii=False, indent=2))
            boxes_json.close()
        print(f"Marked box #{pos} as corrected!")

# python3 manager.py nenl1985 train rus ynk 0,1-2
elif action == "train":
    # tesseract -l rus ynk.nenl1985.exp1.jpg ynk.nenl1985.exp1 box.train
    source_lang = sys.argv[3]
    dest_lang = sys.argv[4]
    positions_argv = sys.argv[5]
    files_in_folder = os.listdir(".")
    positions = unpack_positions(positions_argv)
    box_index = json.loads(open("boxes.json", "r", encoding="utf-8").read())
    for pos in positions:
        relevant_boxes = [fn for fn in files_in_folder if fn == f"{dest_lang}.{folder}.exp{pos}.box"]
        if len(relevant_boxes) == 0:
            raise Exception(f"No box found for position {pos}!")
        box = relevant_boxes[0]


        relevant = [fn for fn in files_in_folder if fn.startswith(f"{dest_lang}.{folder}.exp{pos}.")]
        relevant_images = [fn for fn in relevant if fn.rsplit(".", 1)[-1] in image_extensions]

        if len(relevant_images) > 1:
            raise Exception("More than 1 image found for position:", relevant_images)
        elif len(relevant_images) == 0:
            raise Exception(f"No images found for position {pos}!")
        
        source_image = relevant_images[0]

        if str(pos) not in box_index:
            raise Exception(f"Box #{pos} not in box index!")
        elif not box_index[str(pos)]["corrected"]:
            print(f"Box #{pos} not corrected, skip")
        
        print(f"Training on box #{pos}")
        box_train = subprocess.check_output(
            f"tesseract -l {source_lang} {source_image} {dest_lang}.{folder}.exp{pos} box.train",
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(box_train.decode("utf-8"))

# python3 manager.py nenl1985 extract-unicharset ynk 0-2
elif action == "extract-unicharset":
    lang = sys.argv[3]
    positions_argv = sys.argv[4]
    positions = unpack_positions(positions_argv)
    cmd = "unicharset_extractor "
    cmd += " ".join(f"{lang}.{folder}.exp{pos}.box" for pos in positions)
    print(f"Extracting unicharset")
    unicharset_extraction = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    result = unicharset_extraction.decode("utf-8")
    with open("UNICHARSET_REPORT", "w", encoding="utf-8") as report:
        report.write(result)
        report.close()
    print(result)


# python3 manager.py nenl1985 mftraining ynk 0-2
elif action == "mftraining":
    # mftraining -F font_properties -U unicharset -O ynk.unicharset ynk.nenl1985.exp0.tr ynk.nenl1985.exp1.tr ...
    lang = sys.argv[3]

    # Taking two files from prep/
    print("Taking two files from prep/")
    cp_font_properties = subprocess.check_output(
        f"cp prep/font_properties .",
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(cp_font_properties.decode("utf-8"))
    cp_unicharambigs = subprocess.check_output(
        f"cp prep/unicharambigs .",
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(cp_unicharambigs.decode("utf-8"))


    positions_argv = sys.argv[4]
    positions = unpack_positions(positions_argv)
    cmd = f"mftraining -F font_properties -U unicharset -O {lang}.unicharset "
    cmd += " ".join(f"{lang}.{folder}.exp{pos}.tr" for pos in positions)
    print(f"Running mftraining")
    mftraining = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(mftraining.decode("utf-8"))
    for fn in ("inttemp", "pffmtable", "shapetable"):
        mv = subprocess.check_output(
            f"mv {fn} {lang}.{fn}",
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(mv.decode("utf-8"))

# python3 manager.py nenl1985 cntraining ynk 0-2
elif action == "cntraining":
    lang = sys.argv[3]
    positions_argv = sys.argv[4]
    positions = unpack_positions(positions_argv)
    cmd = f"cntraining "
    cmd += " ".join(f"{lang}.{folder}.exp{pos}.tr" for pos in positions)

    print("Performing cntraining")
    cntraining = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(cntraining.decode("utf-8"))
    for fn in ("normproto",):
        mv = subprocess.check_output(
            f"mv {fn} {lang}.{fn}",
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(mv.decode("utf-8"))

# python3 manager.py nenl1985 format-names ynk
elif action == "format-names":
    lang = sys.argv[3]

    # Rename files before combining it all
    files_in_folder = os.listdir(".")

    found = set()

    for fn in files_in_folder:
        if fn == "unicharambigs" and f"{lang}.unicharambigs" not in files_in_folder:
            mv = subprocess.check_output(
                f"mv {fn} {lang}.{fn}",
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(mv.decode("utf-8"))
            found.add("unicharambigs")
        elif fn == "font_properties" and f"{lang}.font_properties" not in files_in_folder:
            mv = subprocess.check_output(
                f"mv {fn} {lang}.{fn}",
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(mv.decode("utf-8"))
            found.add("font_properties")
        elif fn == "unicharset" and f"{lang}.unicharset" not in files_in_folder:
            mv = subprocess.check_output(
                f"mv {fn} {lang}.{fn}",
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(mv.decode("utf-8"))
            found.add("unicharset")


# python3 manager.py nenl1985 combine ynk
elif action == "combine":
    lang = sys.argv[3]
    cmd = f"combine_tessdata {lang}."
    print("Performing combine_tessdata")
    combine_tessdata = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(combine_tessdata.decode("utf-8"))


# python3 manager.py nenl1985 clean-trained
elif action == "clean-trained":
    files_in_folder = os.listdir(".")
    trained_extensions = {
        ".font_properties"
        ".inttemp",
        ".normproto",
        ".pffmtable",
        ".tr",
        ".shapetable",
        ".traineddata",
        ".unicharset",
        ".unicharambigs"
    }
    for fn in files_in_folder:
        for ext in trained_extensions:
            if fn.endswith(ext):
                print(f"Removing {fn}")
                rm = subprocess.check_output(
                    f"rm {fn}",
                    stderr=subprocess.STDOUT,
                    shell=True
                )
                print(rm.decode("utf-8"))