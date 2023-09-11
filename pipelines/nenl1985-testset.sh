#!/usr/bin/bash
git show ynk-nenl1985-v3:training/nenl1985/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk.traineddata ;

cp input/nenl1985-testset/* output/nenl1985-testset/ ;

python3 scripts/process_pages.py output/nenl1985-testset ynk ;

python3 scripts/nenl1985_format_pages.py output/nenl1985-testset ;