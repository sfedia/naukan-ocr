#!/usr/bin/bash
git show ynk-nenl1985-v3.1:train/nenl1985/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk1.traineddata ;
git show ynk-nenl1990-v4:train/nenl1990/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk2.traineddata ; 

mkdir -p output/nenl1990/ ;

cp -r input/nenl1990-splpages/* output/nenl1990;

python3 scripts/process_pages.py output/nenl1990 ynk1+ynk2 ;

rm -rf output/nenl1990/*.jpg ;