@echo off
echo ========================================
echo Compilation de Bouchonneur 🤖 en .exe
echo ========================================

echo.
echo Installation des dependances...
pip install -r requirements.txt

echo.
echo Compilation avec PyInstaller...
pyinstaller --onefile --noconsole --name "Bouchonneur" deploy_bouchon_gui.py

echo.
echo Compilation terminee !
echo L'executable se trouve dans le dossier 'dist'
echo.
pause 