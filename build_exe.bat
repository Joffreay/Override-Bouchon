@echo off
echo ========================================
echo Compilation de Bouchonneur 🤖 en .exe
echo ========================================

echo.
echo Installation des dependances...
pip install -r requirements.txt

echo.
echo Compilation avec PyInstaller...
python -m PyInstaller --onefile --noconsole --name "Bouchonneur" --manifest admin_manifest.xml deploy_bouchon_gui.py

echo.
echo Compilation terminee !
echo L'executable se trouve dans le dossier 'dist'
echo L'application demandera automatiquement les privilèges d'administrateur.
echo.
pause 