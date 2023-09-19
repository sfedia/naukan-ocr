#!/usr/bin/bash
git show ynk-nenl1985-v3.1:train/nenl1985/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk.traineddata ;

mkdir -p output/nenl1985/ ;
mkdir -p input/nenl1985/;

python3 pipelines/collect-nenl1985.py input/nenl1985;

cp input/nenl1985/* output/nenl1985/ ;

python3 scripts/process_pages.py output/nenl1985 ynk ;

python3 scripts/nenl1985_format_pages.py output/nenl1985 ;

rm -f output/nenl1985/*.jpg ;
rm -f output/nenl1985/*.tiff ;
rm -f output/nenl1985/*.png ;