# 📋 Guide d'Installation - Bouchonneur 🤖

## 🎯 Installation et Configuration

### Étape 1 : Téléchargement et extraction

1. **Téléchargez** l'exécutable `Bouchonneur.exe`
2. **Extrayez** le fichier dans un dossier de votre choix
3. **Créez** un dossier `bouchons` à côté de l'exécutable

### Étape 2 : Structure des dossiers

Votre dossier doit ressembler à ceci :
```
MonDossier/
├── Bouchonneur.exe          # L'application
├── bouchons/                # Dossier pour vos fichiers bouchons
│   ├── bouchon_test_1.json
│   ├── bouchon_test_2.json
│   └── vos_autres_bouchons...
└── README.md                # Documentation (optionnel)
```

### Étape 3 : Ajout de vos bouchons

1. **Placez** vos fichiers bouchons dans le dossier `bouchons/`
2. **Formats supportés** : `.json`, `.xml`, `.txt`, ou tout autre format
3. **L'application** copiera n'importe quel type de fichier

## 🚀 Utilisation

### Lancement de l'application

1. **Double-cliquez** sur `Bouchonneur.exe`
2. **L'interface** s'ouvre avec le design moderne
3. **Vérifiez** que le chemin du dossier bouchons est correct (affiché dans l'interface)

### Déploiement d'un bouchon

1. **Sélectionnez** un fichier bouchon dans la liste déroulante
2. **Vérifiez** le chemin DmpConnect-JS2 (détecté automatiquement)
3. **Cliquez** sur "🚀 DÉPLOYER LE BOUCHON"
4. **Confirmez** le succès dans la popup

## 🔧 Configuration

### Détection automatique du dossier DmpConnect-JS2

L'application cherche automatiquement dans ces emplacements :

**Windows :**
- `%LOCALAPPDATA%\DmpConnect-JS2`
- `%ProgramFiles%\DmpConnect-JS2`
- `%ProgramFiles(x86)%\DmpConnect-JS2`

**macOS :**
- `~/Library/Application Support/DmpConnect-JS2`
- `/Applications/DmpConnect-JS2`
- `/usr/local/DmpConnect-JS2`

### Sélection manuelle du dossier

Si le dossier n'est pas détecté automatiquement :
1. **Cliquez** sur "📁 Parcourir..."
2. **Sélectionnez** manuellement le dossier DmpConnect-JS2
3. **Le chemin** sera sauvegardé pour les prochaines utilisations

## ⚠️ Points importants

### Dossier bouchons
- ✅ **Correct** : Dossier `bouchons/` à côté de l'exécutable
- ❌ **Incorrect** : Dossier `bouchons/` dans le dossier de développement

### Permissions
- **Droits d'écriture** requis dans le dossier DmpConnect-JS2
- **Fermez** DmpConnect-JS2 s'il est en cours d'exécution
- **Vérifiez** les permissions du dossier de destination

### Fichiers
- **Tous les fichiers `.do`** existants seront supprimés avant déploiement
- **Le nouveau fichier** sera renommé en `overrideinsianswer.do`
- **N'importe quel format** de fichier peut être utilisé

## 🐛 Dépannage

### Problème : Aucun fichier bouchon visible
**Solution :**
1. Vérifiez que le dossier `bouchons/` existe à côté de l'exécutable
2. Placez vos fichiers bouchons dans ce dossier
3. Cliquez sur "🔄 Rafraîchir la liste"

### Problème : Erreur "DmpConnect-JS2 invalide"
**Solution :**
1. Utilisez le bouton "📁 Parcourir..."
2. Sélectionnez manuellement le dossier DmpConnect-JS2
3. Vérifiez que le dossier existe et est accessible

### Problème : Erreur de copie
**Solution :**
1. Fermez DmpConnect-JS2 s'il est en cours d'exécution
2. Vérifiez les permissions du dossier de destination
3. Vérifiez l'espace disque disponible

### Problème : L'application ne se lance pas
**Solution :**
1. Vérifiez que vous avez les droits d'administrateur
2. Essayez de lancer depuis une invite de commande
3. Vérifiez que l'antivirus ne bloque pas l'exécutable

## 📊 Vérification

### Test de fonctionnement

1. **Lancez** l'application
2. **Vérifiez** que le chemin du dossier bouchons s'affiche correctement
3. **Sélectionnez** un fichier bouchon dans la liste
4. **Vérifiez** que le chemin DmpConnect-JS2 est détecté
5. **Testez** le déploiement avec un fichier simple

### Indicateurs de succès

- ✅ **Interface moderne** avec thème sombre
- ✅ **Chemin du dossier bouchons** affiché dans l'interface
- ✅ **Liste de fichiers** bouchons visible dans la liste déroulante
- ✅ **Détection automatique** du dossier DmpConnect-JS2
- ✅ **Boutons fonctionnels** avec couleurs et icônes

## 🎉 Félicitations !

Votre **Bouchonneur 🤖** est maintenant correctement configuré et prêt à déployer vos bouchons !

**Rappel important :** L'application utilise maintenant le dossier `bouchons/` dans le même répertoire que l'exécutable, pas dans un dossier temporaire.

---

**Bouchonneur 🤖 v1.0** - Prêt à bouchonner ! 🚀 