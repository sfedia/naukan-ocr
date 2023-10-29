#!/usr/bin/bash
git show ynk-nenl1990-v6.5:train/nenl1990/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk.traineddata ;

mkdir -p output/nenl1990-hocr/ ;

rm -rf output/nenl1990-hocr/* ;

cp -r input/nenl1990-splpages/* output/nenl1990-hocr;

python3 scripts/hocr_process_pages.py output/nenl1990-hocr ynk ;

rm -rf output/nenl1990-hocr/*.jpg ;
