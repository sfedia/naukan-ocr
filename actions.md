## Генерация бокса
```
tesseract --oem 0 -l rus rus.nenl1985-p4-1.exp0.tiff rus.nenl1985-p4-1.exp0 batch.nochop makebox
```

## Запуск редактора боксов
```
open qt-box-editor-1.13.0-alpha.app
```
Работает только с тессерактом из brew

## Установка тессеракта 4 + rus через макпортс
```
sudo port install tesseract
sudo port install tesseract-rus
```
Ставится `tesseract @4.1.3_3` и `tesseract-rus @4.1.0_0`.

## Установка тессеракта 4 через brew
Надо самим сделать формулу.

## Установка тессеракта 5 + rus через brew
```
brew install tesseract
brew install tesseract-lang 
```
Проблема в несовместимости пакетов: tesseract==5.x, tesseract-lang==4.x.
Надо решить проблему путем установки tesseract 4.x через brew.
