FROM node:20-bullseye

WORKDIR /app

RUN apt-get update
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y libtesseract-dev

RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/rus.traineddata
RUN mv rus.traineddata /usr/share/tesseract-ocr/4.00/tessdata

#COPY . .
