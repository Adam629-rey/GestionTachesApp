# Gestion des tâches

Application simple de gestion de tâches en Python avec interface graphique Tkinter et stockage local SQLite.

## Fonctionnalités

- Ajouter une tâche
- Supprimer une tâche
- Marquer une tâche comme terminée
- Afficher les tâches avec un état visuel
- Sauvegarde locale dans une base SQLite

## Prérequis

- Python 3.9 ou plus
- Tkinter (installé avec la plupart des distributions Python)

## Lancement

```bash
python GTV3.py
```

## Structure du projet

- `GT3.py` : logique métier et base de données SQLite
- `GTV3.py` : interface utilisateur Tkinter
- `taches.db` : fichier généré automatiquement lors du premier lancement

## Remarque

Le fichier `taches.db` est igné dans Git via le `.gitignore` afin d’éviter de versionner les données locales.
