FROM node:20-bullseye

WORKDIR /app

RUN apt-get update
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y libtesseract-dev

RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/rus.traineddata
RUN mv rus.traineddata /usr/share/tesseract-ocr/4.00/tessdata

RUN apt-get install -y ocrmypdf

RUN sed -i \
    's|</policymap>|<policy domain="coder" rights="read \| write" pattern="PDF" />\n</policymap>|' \
    /etc/ImageMagick-6/policy.xml

RUN apt-get install -y vim

RUN apt-get install -y poppler-utils

RUN apt-get install -y python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .
