#!/bin/bash

echo "========================================"
echo "Compilation de Bouchonneur 🤖 pour macOS"
echo "========================================"

echo ""
echo "Installation des dépendances..."
pip3 install -r requirements.txt

echo ""
echo "Compilation avec PyInstaller..."
pyinstaller --onefile --noconsole --name "Bouchonneur" deploy_bouchon_gui.py

echo ""
echo "Compilation terminée !"
echo "L'exécutable se trouve dans le dossier 'dist'"
echo "" 