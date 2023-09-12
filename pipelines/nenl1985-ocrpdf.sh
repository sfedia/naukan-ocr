#!/usr/bin/bash

git show ynk-nenl1985-v3:training/nenl1985/ynk.traineddata > /usr/share/tesseract-ocr/4.00/tessdata/ynk.traineddata ;

mkdir -p input/nenl1985-ocrpdf ;

python3 pipelines/collect-nenl1985.py input/nenl1985-ocrpdf;

cp src/nenl1985/nenl1985.1.jpg input/nenl1985-ocrpdf/page-001.jpg ;

cd input/nenl1985-ocrpdf ;

convert $(ls -v *.jpg) nenl1985-merged.pdf ;

cd ../../ ;

mkdir -p output/nenl1985-ocrpdf ;

ocrmypdf -l ynk input/nenl1985-ocrpdf/nenl1985-merged.pdf output/nenl1985-ocrpdf/nenl1985-merged-ocr.pdf ;