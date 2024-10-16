# Canaux de Communication :   
- sur notre groupe de chat Discord Dual and Back 2024  
- dans les pages ISSUES qui concernent donc les problèmes disponibles et à résoudre  

# Interface PROJET  
L'interface PROJET, inspirée de la méthode KANBAN, permet une approche du projet plus visuelle et particulièrement plus simple pour le choix des ISSUES (problèmes à résoudre).  

Plusieurs catégories définissent ainsi les étapes de la "vie" de ces ISSUES.  

Les ISSUES à résoudre sont dans la catégorie "disponible". Une fois une ISSUE allouée à l'un d'entre nous, elle sera bougée dans la catégorie "en cours".  
Une fois que vous pensez avoir fini vous allez soumettre votre travail, elle passera dans la cat. "soumis", puis une fois passée en revue et confirmée, dans la cat. "RÉSOLUES".  

# GIT, GitHub et VsCode
## VsCode :
Je recommande d'utiliser VsCode pour votre choix d'IDE. Si vous avez installé GIT, VsCode sera doté d'un onglet "Source Control", qui fonctionne essentiellement comme une interface GIT.  
Appuyez sur CTRL + SHIFT + G sur votre clavier pour faire apparaître l'onglet si vous ne le voyez pas.  
![image](https://github.com/user-attachments/assets/e6d491d9-406d-49be-bc2e-8a0665bd881e)


C'est très pratique car cet onglet est intégré à VsCode, et donc pas besoin d'ouvrir un terminal, c'est à coté juste là dans la barre latérale gauche.  

Apprenez à vous en servir, c'est pas compliqué si vous avez déjà compris comment fonctionne Git/GitHub. 

## Sans VsCode :
Vous devez déjà avoir installé GIT sur votre PC. Le fichier README vous dit comment accéder à la ligne de commande. C'est là que vous lancerez vos commandes GIT.  
Assurez-vous de savoir à tout moment dans quel dossier vous êtes. Tapez la commande `cd` dans la ligne de commande pour savoir dans quel dossier vous êtes.  
Pour vérifier quelle branche est actuellement active dans votre repo local, utilisez :  
`git branch`  
L'active est celle avec l'astérisque devant : "*". 


# Les Étapes GIT à suivre :
Une fois le projet cloné, vous allez :

- 1. créer une branche :  
  Remplacez nom-branche par un nom pertinent qui décrit le travail que vous allez effectuer, comme `ajout-fonctionnalité` ou `correction-bug`.  
  Commande :
  `git checkout -b nom-branche`

- 2. Apportez les modifications nécessaires dans les fichiers du projet. Une fois terminé, vérifiez l'état des modifications avec :  
  `git status`  
  Cela vous montre les fichiers modifiés, ajoutés ou supprimés qui sont issus de vos modifications.

- 3. Ajoutez les fichiers modifiés à l'index de Git pour préparer le commit (staging). Vous pouvez utiliser :  
  `git add .`  
  Attention, il y a bien un point "." après add

  **NOTE :**  
  Pour ajouter des fichiers spécifiques :  
  `git add chemin/vers/fichier`
  
- 4. Une fois les changements ajoutés, créez un commit pour enregistrer vos modifications localement :  
  `git commit -m "Description des modifications apportées"`  
  Utilisez un message de commit clair et concis qui résume vos changements.

- 5. **IMPORTANT** :  
  Avant de pousser vos changements, assurez-vous que votre branche intègre les dernières mises à jour de la branche principale (celle sur github) pour éviter les conflits lors de la fusion :  

    *  a. Basculer sur sa propre branche principale (donc celle qui est le clone de la branche GitHub - obtenue depuis le clonage au tout début) :  
      `git checkout main`  
    *  b. La mettre à jour   :  
      `git pull origin main`  
    *  c. Revenir à sa branche de travail (celle où vous avez fait vos modifications) et fusionner les dernières modifications de `main` :  
      `git checkout nom-branche` - Remplacez bien sûr nom-branche par votre branche de travail  
      `git merge main`
  
  Si des conflits apparaissent, résolvez-les dans les fichiers concernés, ajoutez-les de nouveau (`git add .`) et terminez la fusion avec un commit si nécessaire.  
  - Envoyez votre branche et vos modifications vers GitHub :  
    `git push origin nom-branche`  

### AVANT DERNIERE ETAPE :  
Après avoir poussé la branche, accédez au répo sur votre propre compte GitHub :  

- Accédez à la page du répo sur votre propre compte GitHub.
- GitHub devrait vous proposer automatiquement de créer une Pull Request pour votre branche. Cliquez sur **"Compare & pull request"**.
- Remplissez les détails de la Pull Request :  
*  Titre : Décrivez brièvement l’objectif de la PR.
*  Description : Fournissez des détails supplémentaires sur les modifications, les raisons, et mentionnez les numéros d’issues liées si nécessaire.  
- Créer la Pull Request en cliquant sur "Create pull request".

### DERNIÈRE ÉTAPE :
Une fois la PR soumise, elle est accessible sur le repo d'origine (celui-ci donc) et les mainteneurs ou autres contributeurs (moi à priori) peuvent la réviser et faire des commentaires.  
Si des modifications supplémentaires sont demandées :  
- Effectuez les modifications dans la même branche, celle créée après le clonage donc (la branche locale).  
- Commitez et poussez les changements (ils seront ajoutés automatiquement à la PR existante).  

## Avant de commencer une nouvelle ISSUE :
Il est recommandé de supprimer la branche locale, pour garder votre environnement propre :   
Supprimer la branche locale :  
`git branch -d nom-branche`

Enfin, n’oubliez pas de mettre à jour votre branche principale (le clone) pour récupérer les dernières modifications apportées au projet :  
`git checkout main`  
`git pull origin main`  

---








