## Генерация бокса
```
tesseract --oem 0 -l rus ynk.nenl1985.exp1.jpg ynk.nenl1985.exp1 batch.nochop makebox
```
### Дальнейшая генерация из тренированной модели
```
sudo cp ynk.traineddata /opt/local/share/tessdata
python3 manager.py nenl1985 make-boxes ynk ynk 3
```
## Тренировка на основе (исправленного) бокса 
```
tesseract -l rus ynk.nenl1985.exp1.jpg ynk.nenl1985.exp1 box.train
```
На выходе на этом этапе - `.tr` файлы
## Извлечение unicharset
```
unicharset_extractor ynk.nenl1985.exp0.box ynk.nenl1985.exp1.box ...
```
## Оформление font_properties
```
<fontname> <italic> <bold> <fixed> <serif> <fraktur>
```
В случае с nenl1985:
```
nenl1985 0 0 0 0 0
```
## mftraining по .tr файлам
```
mftraining -F font_properties -U unicharset -O ynk.unicharset ynk.nenl1985.exp0.tr ynk.nenl1985.exp1.tr ...
```
## cntraining по .tr файлам
```
cntraining ynk.nenl1985.exp0.tr ynk.nenl1985.exp1.tr ...
```

## Тестирование
```
sudo cp training/nenl1985/ynk.traineddata /opt/local/share/tessdata
cd tests/
tesseract nenl1985.12.2.jpg nenl1985.12.2 -l ynk
```

## Запуск редактора боксов
### Онлайн
http://johanjunkka.com/tesseract-web-box-editor/
Не поддерживает tiff
### Оффлайн
```
open qt-box-editor-1.13.0-alpha.app
```
Работает только с тессерактом из brew
### Установка
См. здесь https://github.com/zdenop/qt-box-editor/blob/master/INSTALL

## Установка тессеракта 4 + rus через макпортс
```
sudo port install tesseract
sudo port install tesseract-rus
sudo port install tesseract-training
```
Ставится `tesseract @4.1.3_3` и `tesseract-rus @4.1.0_0`.

## Установка тессеракта 4 через brew
Brew-формула для тессеракта 4.1.3: https://github.com/Homebrew/homebrew-core/blob/c69bf1e5fb6baba54f1d1006a42a5ed6df698e1f/Formula/tesseract.rb


Можно скачать .rb и собрать
```
wget https://raw.githubusercontent.com/Homebrew/homebrew-core/c69bf1e5fb6baba54f1d1006a42a5ed6df698e1f/Formula/tesseract.rb
brew install --build-from-source tesseract.rb
```

Если при сборке возникает проблема, связанная с устаревшим CLT:

```
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
```

## Установка тессеракта 5 + rus через brew
```
brew install tesseract
brew install tesseract-lang 
```
Проблема в несовместимости пакетов: tesseract==5.x, tesseract-lang==4.x.
Надо решить проблему путем установки tesseract 4.x через brew.

