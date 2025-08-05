import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys

TARGET_NAME = "overrideinsianswer.do"

def get_application_dir():
    """Retourne le répertoire d'installation de l'application"""
    if getattr(sys, 'frozen', False):
        # L'application est compilée (exécutable)
        return os.path.dirname(sys.executable)
    else:
        # L'application est en mode développement (script Python)
        return os.path.dirname(__file__)

BOUCHON_DIR = os.path.join(get_application_dir(), "bouchons")

def detect_dmpconnect_dir():
    """Détecte automatiquement le dossier DmpConnect-JS2"""
    candidates = [
        os.path.expandvars(r"%LOCALAPPDATA%\DmpConnect-JS2"),
        os.path.expandvars(r"%ProgramFiles%\DmpConnect-JS2"),
        os.path.expandvars(r"%ProgramFiles(x86)%\DmpConnect-JS2"),
    ]
    
    # Ajout de chemins spécifiques pour macOS
    if sys.platform == "darwin":
        candidates.extend([
            os.path.expanduser("~/Library/Application Support/DmpConnect-JS2"),
            "/Applications/DmpConnect-JS2",
            "/usr/local/DmpConnect-JS2"
        ])
    
    for path in candidates:
        if os.path.isdir(path):
            return path
    return ""

def browse_dmpconnect_dir():
    """Permet à l'utilisateur de sélectionner manuellement le dossier DmpConnect-JS2"""
    directory = filedialog.askdirectory(title="Sélectionner le dossier DmpConnect-JS2")
    if directory:
        dmp_dir.set(directory)

def refresh_bouchon_list():
    """Rafraîchit la liste des fichiers bouchons"""
    if os.path.exists(BOUCHON_DIR):
        files = [f for f in os.listdir(BOUCHON_DIR) if os.path.isfile(os.path.join(BOUCHON_DIR, f))]
        combo['values'] = files
        if files:
            combo.set(files[0])
    else:
        combo['values'] = []
        combo.set("")

def deploy_bouchon():
    """Déploie le bouchon sélectionné"""
    selected = combo.get()
    if not selected:
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier bouchon.")
        return
    
    source_file = os.path.join(BOUCHON_DIR, selected)
    if not os.path.isfile(source_file):
        messagebox.showerror("Erreur", f"Fichier introuvable : {source_file}")
        return
    
    target_dir = dmp_dir.get()
    if not target_dir or not os.path.isdir(target_dir):
        messagebox.showerror("Erreur", "Le répertoire DmpConnect-JS2 est invalide.")
        return

    # Supprimer les anciens fichiers .do
    try:
        for f in os.listdir(target_dir):
            if f.endswith(".do"):
                file_path = os.path.join(target_dir, f)
                try:
                    os.remove(file_path)
                    print(f"Fichier supprimé : {f}")
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible de supprimer {f} : {e}")
                    return
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la lecture du répertoire : {e}")
        return

    # Copier et renommer le nouveau bouchon
    try:
        target_file = os.path.join(target_dir, TARGET_NAME)
        shutil.copy2(source_file, target_file)
        messagebox.showinfo("Succès", f"Bouchon déployé avec succès !\n\nFichier : {TARGET_NAME}\nRépertoire : {target_dir}")
        print(f"Bouchon déployé : {source_file} -> {target_file}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la copie : {e}")

def create_bouchon_dir():
    """Crée le dossier bouchons s'il n'existe pas"""
    if not os.path.exists(BOUCHON_DIR):
        try:
            os.makedirs(BOUCHON_DIR)
            messagebox.showinfo("Information", f"Dossier 'bouchons' créé : {BOUCHON_DIR}\n\nVeuillez y placer vos fichiers bouchons.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer le dossier bouchons : {e}")

# Interface utilisateur
root = tk.Tk()
root.title("Bouchonneur 🤖 - Déployeur de bouchons")
root.geometry("700x500")
root.resizable(True, True)

# Configuration des couleurs modernes
COLORS = {
    'bg_primary': '#2c3e50',
    'bg_secondary': '#34495e',
    'bg_light': '#ecf0f1',
    'accent': '#3498db',
    'success': '#27ae60',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'text_light': '#ffffff',
    'text_dark': '#2c3e50'
}

# Style et configuration
root.configure(bg=COLORS['bg_primary'])
style = ttk.Style()
style.theme_use('clam')

# Configuration du style ttk
style.configure('Title.TLabel', 
                font=('Segoe UI', 18, 'bold'),
                background=COLORS['bg_primary'],
                foreground=COLORS['text_light'])

style.configure('Subtitle.TLabel',
                font=('Segoe UI', 10),
                background=COLORS['bg_primary'],
                foreground=COLORS['text_light'])

style.configure('Custom.TLabelframe',
                background=COLORS['bg_secondary'],
                foreground=COLORS['text_light'])

style.configure('Custom.TLabelframe.Label',
                font=('Segoe UI', 11, 'bold'),
                background=COLORS['bg_secondary'],
                foreground=COLORS['text_light'])

# Frame principal avec dégradé
main_frame = tk.Frame(root, bg=COLORS['bg_primary'], padx=25, pady=25)
main_frame.pack(fill=tk.BOTH, expand=True)

# En-tête avec logo et titre
header_frame = tk.Frame(main_frame, bg=COLORS['bg_primary'])
header_frame.pack(fill=tk.X, pady=(0, 25))

# Logo et titre
title_frame = tk.Frame(header_frame, bg=COLORS['bg_primary'])
title_frame.pack()

logo_label = tk.Label(title_frame, text="🤖", font=("Segoe UI", 48), 
                     bg=COLORS['bg_primary'], fg=COLORS['accent'])
logo_label.pack()

title_label = tk.Label(title_frame, text="Bouchonneur 🤖", 
                      font=("Segoe UI", 24, "bold"), 
                      bg=COLORS['bg_primary'], fg=COLORS['text_light'])
title_label.pack()

subtitle_label = tk.Label(title_frame, text="Déployeur de bouchons", 
                         font=("Segoe UI", 12), 
                         bg=COLORS['bg_primary'], fg=COLORS['accent'])
subtitle_label.pack(pady=(5, 0))

# Section 1: Sélection du bouchon
bouchon_frame = tk.LabelFrame(main_frame, text="📁 Sélection du fichier bouchon", 
                              font=("Segoe UI", 11, "bold"), 
                              bg=COLORS['bg_secondary'], fg=COLORS['text_light'],
                              padx=15, pady=15, relief=tk.RAISED, bd=2)
bouchon_frame.pack(fill=tk.X, pady=(0, 20))

tk.Label(bouchon_frame, text=f"Fichiers disponibles dans le dossier 'bouchons/' :", 
         bg=COLORS['bg_secondary'], fg=COLORS['text_light'],
         font=("Segoe UI", 10)).pack(anchor='w', pady=(0, 8))

# Affichage du chemin du dossier bouchons
bouchon_path_label = tk.Label(bouchon_frame, text=f"📂 Dossier : {BOUCHON_DIR}", 
                              bg=COLORS['bg_secondary'], fg=COLORS['accent'],
                              font=("Segoe UI", 8))
bouchon_path_label.pack(anchor='w', pady=(0, 8))

combo = ttk.Combobox(bouchon_frame, width=60, font=("Segoe UI", 10), 
                     style='Custom.TCombobox')
combo.pack(fill=tk.X, pady=(0, 10))

# Bouton pour rafraîchir la liste
refresh_btn = tk.Button(bouchon_frame, text="🔄 Rafraîchir la liste", 
                       command=refresh_bouchon_list, 
                       font=("Segoe UI", 10, "bold"),
                       bg=COLORS['accent'], fg=COLORS['text_light'],
                       relief=tk.RAISED, bd=2, padx=15, pady=5,
                       activebackground=COLORS['accent'], activeforeground=COLORS['text_light'])
refresh_btn.pack(pady=(5, 0))

# Section 2: Répertoire DmpConnect-JS2
dmp_frame = tk.LabelFrame(main_frame, text="🎯 Répertoire DmpConnect-JS2", 
                          font=("Segoe UI", 11, "bold"), 
                          bg=COLORS['bg_secondary'], fg=COLORS['text_light'],
                          padx=15, pady=15, relief=tk.RAISED, bd=2)
dmp_frame.pack(fill=tk.X, pady=(0, 20))

tk.Label(dmp_frame, text="Chemin du dossier DmpConnect-JS2 :", 
         bg=COLORS['bg_secondary'], fg=COLORS['text_light'],
         font=("Segoe UI", 10)).pack(anchor='w', pady=(0, 8))

dmp_dir = tk.StringVar(value=detect_dmpconnect_dir())
entry = tk.Entry(dmp_frame, textvariable=dmp_dir, width=70, 
                font=("Segoe UI", 10), relief=tk.SUNKEN, bd=2)
entry.pack(fill=tk.X, pady=(0, 10))

# Bouton pour parcourir
browse_btn = tk.Button(dmp_frame, text="📁 Parcourir...", 
                      command=browse_dmpconnect_dir, 
                      font=("Segoe UI", 10, "bold"),
                      bg=COLORS['warning'], fg=COLORS['text_light'],
                      relief=tk.RAISED, bd=2, padx=15, pady=5,
                      activebackground=COLORS['warning'], activeforeground=COLORS['text_light'])
browse_btn.pack(pady=(0, 5))

# Section 3: Bouton de déploiement
deploy_frame = tk.Frame(main_frame, bg=COLORS['bg_primary'])
deploy_frame.pack(fill=tk.X, pady=(15, 0))

deploy_btn = tk.Button(deploy_frame, text="🚀 DÉPLOYER LE BOUCHON", 
                      command=deploy_bouchon, 
                      font=("Segoe UI", 14, "bold"), 
                      bg=COLORS['success'], fg=COLORS['text_light'],
                      relief=tk.RAISED, bd=3, padx=30, pady=15,
                      activebackground=COLORS['success'], activeforeground=COLORS['text_light'])
deploy_btn.pack()

# Status bar avec design moderne
status_frame = tk.Frame(main_frame, bg=COLORS['bg_secondary'], relief=tk.SUNKEN, bd=1)
status_frame.pack(fill=tk.X, pady=(20, 0))

status_label = tk.Label(status_frame, text="🤖 Prêt à bouchonner !", 
                       bg=COLORS['bg_secondary'], fg=COLORS['text_light'],
                       font=("Segoe UI", 9))
status_label.pack(side=tk.LEFT, padx=10, pady=5)

# Footer avec informations
footer_frame = tk.Frame(main_frame, bg=COLORS['bg_primary'])
footer_frame.pack(fill=tk.X, pady=(10, 0))

footer_label = tk.Label(footer_frame, text="Bouchonneur 🤖 v1.0 - Compatible Windows & macOS", 
                       bg=COLORS['bg_primary'], fg=COLORS['accent'],
                       font=("Segoe UI", 8))
footer_label.pack()

# Initialisation
create_bouchon_dir()
refresh_bouchon_list()

# Configuration de la fenêtre
root.protocol("WM_DELETE_WINDOW", root.quit)

if __name__ == "__main__":
    root.mainloop() 