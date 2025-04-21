#!/bin/bash

# Sprawdź, czy PyInstaller jest zainstalowany, a jeśli nie, to go zainstaluj
if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller not found, installing..."
    pip install -U pyinstaller
fi

# Usuń stare foldery 'build' i 'dist' (jeśli istnieją)
[ -d "./build" ] && rm -rf ./build
[ -d "./dist" ] && rm -rf ./dist

# Utwórz aplikację EXE przy użyciu PyInstaller
pyinstaller --onefile --distpath ./dist --workpath ./build --name TaskManager TaskManager.py

# Jeśli plik EXE został utworzony, uruchom go
if [ -f "./dist/TaskManager.exe" ]; then
    ./dist/TaskManager.exe
else
    echo "Nie udało się utworzyć pliku EXE."
fi