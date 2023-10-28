#!/usr/bin/bash
git show ynk-nenl1990-v6.4:train/nenl1990/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk.traineddata ;

mkdir -p output/nenl1990/ ;

rm -rf output/nenl1990/* ;

cp -r input/nenl1990-splpages/* output/nenl1990;

python3 scripts/process_pages.py output/nenl1990 ynk ;

rm -rf output/nenl1990/*.jpg ;