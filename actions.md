## Генерация бокса
```
tesseract --oem 0 -l rus rus.nenl1985-p4-1.exp0.tiff rus.nenl1985-p4-1.exp0 batch.nochop makebox
```

## Запуск редактора боксов
```
open qt-box-editor-1.13.0-alpha.app
```

## Установка тессеракта 4 + rus через макпортс
```
sudo port install tesseract
sudo port install tesseract-rus
```

## Установка тессеракта 5 + rus через brew
```
brew install tesseract
brew install tesseract-lang 
```
