import tkinter as tk
from tkinter import ttk, messagebox

def dire_bonjour():
    messagebox.showinfo("Titre fenetre", "Une fenetre d'infos ou autres")

def change_msg():
    msgachanger.config(text="le msg a changé au clic")

def toggle_message():
    """Change le texte et la couleur du message selon l’état de la case."""
    if check_var1.get():
        msg_param.config(text="Option activée ✅", fg="green")
    else:
        msg_param.config(text="Option désactivée ❌", fg="red")

# --- Fenêtre principaleeeeeee ---
fenetre = tk.Tk()
fenetre.title("Application multi-onglets")
fenetre.geometry("500x300")

# --- Onglets ---
onglets = ttk.Notebook(fenetre)
onglets.pack(expand=True, fill='both')

# --- Onglet 1 ---
accueil = ttk.Frame(onglets)
onglets.add(accueil, text='Accueil')

tk.Label(accueil, text="Grand titre", font=("Arial", 20)).pack(pady=20)
tk.Button(accueil, text="ouvrir fenetre", command=dire_bonjour).pack()
tk.Button(accueil, text="appel fonction", command=change_msg).pack()

# ⚠️ ATTENTION : il faut séparer la création et le .pack()
msgachanger = tk.Label(accueil, text="msg à changer", font=("Arial", 12))
msgachanger.pack(pady=20)

# --- Onglet 2 ---
parametres = ttk.Frame(onglets)
onglets.add(parametres, text='Paramètres')

tk.Label(parametres, text="Réglage du volume :").pack(pady=10)
tk.Scale(parametres, from_=0, to=100, orient='horizontal').pack()

check_var1 = tk.BooleanVar()
tk.Checkbutton(parametres, text="Activer option 1", variable=check_var1, command=toggle_message).pack(pady=10)

check_var2 = tk.BooleanVar()
tk.Checkbutton(parametres, text="Activer option 2", variable=check_var2).pack(pady=10)

# ⚠️ Même problème ici : séparer création et pack()
msg_param = tk.Label(parametres, text="Option désactivée ❌", font=("Arial", 12), fg="red")
msg_param.pack(pady=10)

fenetre.mainloop()
