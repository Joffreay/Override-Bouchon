# Bouchonneur 🤖 - Déployeur de bouchons

Application graphique moderne pour déployer des fichiers bouchons.

## 🚀 Fonctionnalités

- **Détection automatique** du dossier DmpConnect-JS2
- **Sélection de fichiers bouchons** depuis le dossier `bouchons/` dans le répertoire d'installation
- **Déploiement automatique** avec suppression des anciens fichiers `.do`
- **Support multi-plateforme** (Windows et macOS)
- **Privilèges administrateur** automatiques sur Windows

## 📁 Structure du projet

```
MonProjet/
├── deploy_bouchon_gui.py      # Script principal
├── requirements.txt            # Dépendances Python
├── build_exe.bat              # Script de compilation Windows
├── build_macos.sh             # Script de compilation macOS
├── README.md                  # Ce fichier
└── bouchons/                  # Dossier contenant les fichiers bouchons
    ├── bouchon_test_1.json
    ├── bouchon_test_2.json
    └── bouchon_test_3.json
```

## 🛠️ Installation et compilation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Compilation sous Windows

1. Ouvrez une invite de commande dans le dossier du projet
2. Exécutez le script de compilation :
   ```bash
   build_exe.bat
   ```
3. L'exécutable sera créé dans le dossier `dist/`

### Compilation sous macOS

1. Ouvrez le Terminal dans le dossier du projet
2. Rendez le script exécutable :
   ```bash
   chmod +x build_macos.sh
   ```
3. Exécutez le script de compilation :
   ```bash
   ./build_macos.sh
   ```
4. L'exécutable sera créé dans le dossier `dist/`

### Compilation manuelle

Si vous préférez compiler manuellement :

```bash
# Installation des dépendances
pip install pyinstaller

# Compilation
pyinstaller --onefile --noconsole --name "Bouchonneur" deploy_bouchon_gui.py
```

## 📋 Utilisation

### 1. Préparation des fichiers bouchons

**Important** : Placez vos fichiers bouchons dans le dossier `bouchons/` **à côté de l'exécutable**. Si le bouchonneur de trouve pas vos fichiers bouchons, vérifiez le dossier inscrit et rafraîchissez la liste. 

Structure recommandée :
```
VotreDossier/
├── Bouchonneur.exe          # L'exécutable
├── bouchons/                # Dossier contenant vos bouchons
│   ├── bouchon_test_1.json
│   ├── bouchon_test_2.json
│   └── ...
└── README.md
```

### 2. Lancement de l'application

- **Windows** : Double-cliquez sur `Bouchonneur.exe`
  - L'application demandera automatiquement les privilèges d'administrateur
  - Acceptez l'élévation des privilèges pour un fonctionnement optimal
- **macOS** : Double-cliquez sur `Bouchonneur`

### 3. Déploiement d'un bouchon

1. **Sélectionnez un fichier bouchon** dans la liste déroulante
2. **Vérifiez le chemin** du dossier DmpConnect-JS2 (détecté automatiquement ou sélectionné manuellement)
3. **Cliquez sur "🚀 DÉPLOYER LE BOUCHON"**
4. L'application :
   - Supprime tous les fichiers `.do` existants dans le dossier DmpConnect-JS2
   - Copie le fichier bouchon sélectionné
   - Le renomme en `overrideinsianswer.do`
   - Affiche une confirmation de succès

## 🔧 Chemins de détection automatique

### Windows
- `%LOCALAPPDATA%\DmpConnect-JS2`
- `%ProgramFiles%\DmpConnect-JS2`
- `%ProgramFiles(x86)%\DmpConnect-JS2`

### macOS
- `~/Library/Application Support/DmpConnect-JS2`
- `/Applications/DmpConnect-JS2`
- `/usr/local/DmpConnect-JS2`

## ⚠️ Notes importantes

- **Dossier bouchons** : L'application utilise le dossier `bouchons/` dans le même répertoire que l'exécutable
- **Droits d'écriture** : L'application nécessite des droits d'écriture dans le dossier DmpConnect-JS2
- **Fichiers .do** : Les fichiers `.do` existants seront supprimés avant le déploiement
- **Fichiers valides** : L'application fonctionne avec n'importe quel type de fichier

## 🐛 Dépannage

### Problème : "Le répertoire DmpConnect-JS2 est invalide"
- Vérifiez que le dossier existe
- Utilisez le bouton "📁 Parcourir..." pour sélectionner manuellement le dossier

### Problème : "Impossible de supprimer [fichier]"
- Vérifiez que l'application a les droits d'écriture
- Fermez DmpConnect-JS2 s'il est en cours d'exécution

### Problème : "Erreur lors de la copie"
- Vérifiez l'espace disque disponible
- Vérifiez les permissions du dossier de destination

### Problème : Aucun fichier bouchon visible
- Vérifiez que le dossier `bouchons/` existe à côté de l'exécutable
- Placez vos fichiers bouchons dans ce dossier
- Utilisez le bouton "🔄 Rafraîchir la liste"


## 📝 Version

Version 1.0 - Compatible Windows et macOS 🤖 
