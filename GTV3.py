import tkinter as tk
from tkinter.font import Font

from GT3 import Taches


class GestionTachesApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Gestion des tâches")
        self.root.protocol("WM_DELETE_WINDOW", self.fermer)

        self.taches = Taches()
        self.taches.db_connecter()
        self.taches_labels = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=15)

        self.entree = tk.Entry(self.frame, width=35)
        self.entree.grid(row=0, column=0, ipady=8)

        police = Font(family="Comic Sans MS")

        self.btn_ajouter = tk.Button(
            self.frame,
            text="+",
            padx=10,
            command=self.ajouter_tache,
            bg="Blue",
            font=police,
        )
        self.btn_terminer = tk.Button(
            self.frame,
            text="x",
            padx=10,
            command=self.terminer_tache,
            bg="Green",
            font=police,
        )
        self.btn_supprimer = tk.Button(
            self.frame,
            text="-",
            padx=10,
            command=self.supprimer_tache,
            bg="Red",
            font=police,
        )

        self.btn_ajouter.grid(row=0, column=1, padx=2)
        self.btn_terminer.grid(row=0, column=2, padx=2)
        self.btn_supprimer.grid(row=0, column=3, padx=2)

        self.afficher_taches()

    def nettoyer_labels(self) -> None:
        for label in self.taches_labels:
            label.destroy()
        self.taches_labels = []

    def selectionner(self, event) -> None:
        texte = event.widget.cget("text")
        self.entree.delete(0, tk.END)
        self.entree.insert(0, texte)

    def fermer(self) -> None:
        print("Déconnexion")
        self.taches.db_fermer()
        self.root.destroy()

    def afficher_taches(self) -> None:
        self.nettoyer_labels()

        for _, tache, etat in self.taches.recuperer():
            label = tk.Label(
                text=tache,
                font=Font(family="Comic Sans MS", weight="bold"),
                borderwidth=4,
                relief="raised",
            )
            label.pack(fill=tk.BOTH, expand=True)
            label.bind("<Button-1>", self.selectionner)
            self.taches_labels.append(label)

            if etat == 1:
                label.configure(bg="#6CD29B")

    def ajouter_tache(self) -> None:
        tache = self.entree.get().strip()
        if not tache:
            return

        self.taches.ajouter(tache)
        self.entree.delete(0, tk.END)
        self.afficher_taches()

    def supprimer_tache(self) -> None:
        tache = self.entree.get().strip()
        if not tache:
            return

        self.taches.supprimer(tache)
        self.entree.delete(0, tk.END)
        self.afficher_taches()

    def terminer_tache(self) -> None:
        tache = self.entree.get().strip()
        if not tache:
            return

        self.taches.terminer(tache)
        self.entree.delete(0, tk.END)
        self.afficher_taches()

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    fenetre = tk.Tk()
    app = GestionTachesApp(fenetre)
    app.run()

