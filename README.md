# Jeu de mémoire Dual and Back

Un jeu d'amélioration de la mémoire basé sur Python, avec une interface graphique construite avec Tkinter et Pygame pour la gestion du son.

## Caractéristiques

- Grille 3x3 avec des signaux visuels et sonores aléatoires.
- Durées de séances de jeu multiples.
- Confirmations utilisateurs (boutons) avec retour visuel.
- Rapport de jeu détaillé.

---

## Installation
Il vous faut avoir installer:  
- git  
  https://git-scm.com/downloads
- python (minimum version 3.1 - Recommandée : 3.12.5)  
  https://www.python.org/downloads/release/python-3125/

Pour l'IDE, j'utilise VsCode, je le recommande donc.  
https://code.visualstudio.com/download

Une fois que vous avez **bien INSTALLÉ VsCode, Python et Git**, continuez avec ce qui suit :

1. Créer un dossier pour le projet.  
   Lancer l'interface de ligne de commande (le CLI) - Ne **sortez pas du dossier** créé précédemment.

   Voici comment :  
   Ici "mon-dossier" c'est en fait le dossier que vous venez de créer. Donc à priori votre dossier n'est pas nommé "mon-dossier".  

   ![image](https://github.com/user-attachments/assets/0a7c4ca1-9606-4cd6-b02c-2abfa7aaa99f)

   TAPEZ cmd sur le clavier et tapez ENTER, cela va ouvrir la fenêtre de la ligne de commande (appelé le CLI) :  

   ![image](https://github.com/user-attachments/assets/36254828-458e-4a8b-a11d-82f8665abf82)

   La fenêtre du CLI s'ouvre :   

      ![image](https://github.com/user-attachments/assets/c959725d-e59a-4ffe-b816-0174b60ced1f)

2. Clonez ce repo avec la commande suivante :  
   `git clone https://github.com/jendives2000/DualNBack2024.git`  
  Tout le dossier du projet devrait avoir été copié sur votre machine.

1. Créez et activez un environnement virtuel (optionnel mais recommandé) :  
Copiez le code ci-dessous. **Remplacer mon-venv** par le nom que vous voulez donner à votre environnement :  
`python -m venv mon-venv`  
Activez l'environnement :  
`mon-venv\Scripts\activate`

1. Installez les dépendances :  
`pip install -r requirements.txt`


5.  Ouvrir le projet dans VsCode :
Tapez `code .`  
VsCode se lance et ouvre le projet. 

Désormais vous avez le projet ouvert dans VsCode. Ne codez pas encore. Gardez la fenêtre du CLI ouverte. 

---

## Lancer l'application :  
Toujours dans la fenêtre de commande; tapez :
`python dual_and_back_app.py`   
Une nouvelle fenêtre va s'ouvrir et lancera le jeu. Essayez le, explorez le jeu pour en en avoir une bonne idée.

---

## Avant de coder :  
Ce qui suit est **TRÈS important**.
Avant de commencer à coder dans VsCode, faites les choses suivantes :   
- lisez le document infos-code
- lisez ensuite le document CONTRIBUER.md
- consultez l'onglet "ISSUES" pour choisir un problème sur lequel vous travaillerez
  ![image](https://github.com/user-attachments/assets/64fbb0ec-e3ee-478d-ad79-482550be94fe)
- puis dans VsCode, sélectionnez le bon interpréteur (le python que vous avez installé) ainsi que l'environnement que vous avez créé dans le CLI précédémment.  
Si cela vous est difficile, contactez-moi sur Discord. Un document "aide_vscode" sera ajouté pour vous montrer comment faire. 

---
