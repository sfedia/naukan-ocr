# FROM node:20-bullseye
FROM python:3.8.11-bullseye

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

RUN apt-get install -y libxml2-dev libxslt1-dev python3-dev

RUN apt-get install -y python3-pip

ENV NODE_VERSION=16.13.0
RUN apt install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version
RUN git clone https://github.com/eloops/hocr2pdf
COPY hocr2pdf src/hocr2pdf
RUN cd src/hocr2pdf && npm install -g

WORKDIR /app

RUN apt-get install -y vim

RUN apt-get install -y poppler-utils

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .
