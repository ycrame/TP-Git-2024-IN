# 🛠️ TP Git

### ❓ Qu'est-ce que Git ?

Git est un logiciel de gestion de versions. C'est-à-dire qu'il vous aide à gérer les différentes versions de votre code, ainsi qu'à collaborer à plusieurs sur un même projet.

N'hésitez pas à vous référer au 📚 [cours](Cours.pdf) préparé par INSAlgo ou aux 📖 [slides](Formation-2024.pdf) pour ce TP !

### 💻 Installation de git

Sur Linux, git est installé par défaut sur le système.
Pour ce qui est de Windows et MacOS, il suffit de se rendre sur <https://git-scm.com/downloads> et de suivre les instructions de Windows / MacOS selon votre système.
Après avoir téléchargé git, configurez Git pour qu’il associe vos commits à votre nom et adresse e-mail:

`git config --global user.name "Votre Nom"`

`git config --global user.email supermail@gmail.com`

### 📝 Créer un compte Github

Vous avez besoin d'un compte Github pour ce TP.
Si vous ne possédez pas encore de compte github, vous pouvez le créer sur <https://github.com/join>.

Ensuite, il vous faudra forker ce projet afin que vous l'ayez sur votre profile. Nous suggérons qu'un des deux binôme fork le projet, et ensuite invite l'autre à collaborer.


## 🏁 Partie 0 : Prise en main

Pour vous initier à Git nous vous proposons dans un premier temps de tester les commandes vues durant la partie théorique sur un PlayGround spécial git : [Git School](https://git-school.github.io/visualizing-git/#free) ou [Learning Git Branching](https://learngitbranching.js.org/?locale=fr_FR)

**Git School:** 

<img width="299" alt="image" src="https://github.com/user-attachments/assets/2d130404-3454-43b3-a14f-109d83805b50">

Learning Git Branching:**

<img width="299" alt="image" src="https://github.com/user-attachments/assets/149b4ec4-8294-4579-ba76-4a4221f8c730">



Initiez-vous à :
- `git branch`
- `git switch` / `git checkout` 
- `git commit` & `git add`
- `git push`
- `git pull`
- `git merge`
  
## 🌍 Partie 1 : Hello world

**IMPORTANT** : Les commandes données par la suite ne sont pas complètes, c'est à vous de trouver les bons arguments à ajouter ;) Vous pouvez vous aider des ressources de ce dépot ou d'Internet.

### 🔄 Cloner le dépot

Récupérez ce dépot en local sur votre PC en utilisant la commande `git clone`. Déplacez vous dans le dossier ainsi crée.

### 🌿 Créer une branche et un dossier

Chaque binôme travaille sur le répo forké par l'un des deux. Créez chez un membre du binôme une branche (nommée `prénom1-prénom2`) avec `git switch -c`, puis l'autre binôme se placera sur celle-ci avec `git switch`.

**A faire que par un des deux binôme :**
Créez aussi un dossier portant le même nom à la racine du projet, où vous placerez votre code.
Créez votre fichier de code dans le langage de votre choix. Faites en sorte que celui-ci affiche `Hello world` à l’exécution.

### 🤝 Partager les modifications

Toutes ces actions étant faites sur un PC, il faut les partager pour que le second membre du binôme puisse y accéder !
Commencez par ajouter à Git les modifications apportées au fichier avec `git add` suivi du chemin vers le fichier.

C'est le moment d'essayer la commande `git status`. Elle vous permet de voir les modifications qui seront enregistrées dans le prochain commit. Cette commande est très utile pour savoir où on en est. Prenez l'habitude de l'utiliser avant chaque commit pour être sûr de ce que vous faites.

Vous pouvez maintenant enregistrer les modifications avec `git commit`. Pensez à bien décrire ce que vous avez fait dans le message de commit ! Pour écrire votre message directement dans le terminal, ajoutez `-m` à la commande suivi du message entre guillemets.

Il faut ensuite pousser les modifications sur le dépot GitHub avec `git push` (lisez bien les messages d'erreur si vous en avez, ils vont aideront à trouver la bonne commande).

Pour voir si le code a bien été partagé, rendez vous sur Github et vérifiez que votre branche est bien apparue, avec votre fichier.

### 🔄 Récupérer les modifications

Une fois les modifications en ligne, il faut les récupérer sur le second PC.

Pour voir les branches que vous avez en local, vous pouvez utiliser `git branch` sans argument. Vous pouvez constater que vous n'avez que la branche `main` pour l'instant, et pas celle de votre binôme. Pour voir aussi les branches du dépot distant, ajoutez `--all` à la commande.

Mais là encore, la branche de votre binôme ne s'affiche pas, pourquoi ? En fait, il faut mettre à jour en local les informations sur le dépot avec `git fetch`. Constatez maintenant que la branche est dans la liste.

Vous pouvez maintenant vous placer sur votre branche, ce qui a pour effet d'appliquer les commits, et donc de récupérer les modifications ! Comme vous venez de récupérer la branche sur votre machine, elle est à jour avec le dépot. Mais par la suite, il faudra récupérer les nouveaux commits avec `git pull`.

Que se passe-t-il si vous retournez sur la branche `main` ? Vous devriez maintenant comprendre comment Git vous permet d'avoir plusieurs versions d'un projet en parallèle.

### ✏️ Plus de modifications

C'est maintenant à l'autre membre du binôme de faire des modifications. Changez le message pour ne plus afficher `Hello world` mais `Hello INSA`. Faites en sorte que l'autre membre du binôme récupère les changements.

## 🤝 Partie 2 : Travail en parallèle

Pour cette partie, vous allez utiliser le template de code. Copiez le fichier `fonctions.py` dans votre dossier, puis faites un commit avant toute modification, pour que les deux membres aient le fichier.

### 📅 Commits en parallèle

Un membre du binôme complète la fonction `addition()`, et l'autre la fonction `soustraction()`. Chacun pousse ensuite ses changements.

La deuxième personne va avoir une surprise : des changements ont été poussés entre temps, et git ne veut pas les écraser !

Il faut donc récupérer les modifications de la première personne et les fusionner.
Pour faire cela, il faut donner une stratégie à Git, nous allons utiliser le rebase. Vous pouvez donc récupérer puis rebase en ajoutant `--rebase` à la commande que vous utilisez pour récupérer les modifications.

### ⚔️ Résolution de conflit

Dans cette partie, les deux membres du binôme vont modifier la même fonction, `noms_binome()`, qui doit afficher vos noms sur deux lignes différentes. Chacun rajoute le code pour afficher son nom et seulement son nom. Faites ensuite un commit et poussez vos changements.

Comme vous avez normalement modifié la même ligne pour afficher votre nom, git ne sait pas quelle version garder !

Lorsqu'il y a un conflit comme ici, git génère dans le fichier de nouvelles lignes pour vous aider à comprendre où sont les problèmes. Ces lignes se présentent sous cette forme :

```c
<<<<<<< HEAD
int a = 1;
=======
int a = 2;
>>>>>>> branche_a_merge 
```

Vous pouvez alors choisir celles que vous voulez (la version de GitHub, la version locale, ou les deux). N'oubliez pas d'enlever les lignes rajoutées par git. Une fois cela fait, terminez le rebase avec `git rebase --continue`. Une fois le rebase terminé, vous devriez pouvoir pousser vos modifications.

Comment auriez-vous pu faire pour avoir moins de difficultés à fusionner ?

## 🗂️ Partie 3 : Mettre vos modifications sur la branche main

Le but est maintenant d'ajouter vos modifications sur la branche `main`. Cette branche étant protégée, vous ne pouvez pas mettre directement le code de votre branche dessus. Pour faire cela, vous devez passer par les **pull requests**.

### ➡️ Première pull request

Créez une pull request pour votre branche. Faites bien attention au titre et à la description afin que l'on sache en quoi votre code consiste ! Une fois cela fait, vous pouvez demander à un administrateur du dépot GitHub de valider vos modifications, pour les mettre sur la branche `main`.

### ❗ Pull request avec un conflit

Nous allons maintenant essayer de faire une pull request qui rentre en conflit avec la branche `main`. Pour cela, chacun des membres du binôme créent une branche à leur nom. Sur ces branches, rajoutez chacun votre nom dans le fichier `NOMS.txt`, sur la même ligne. Faites ensuite les pull requests pour ces branches.

Comme plus tôt, c'est celui qui passe en deuxième qui a des problèmes. Comme les changements sont en conflit, GitHub vous indique que les modifications ne peuvent pas être automatiquement appliquées sur le `main`. Aidez-vous de l'explication plus haut pour régler ce conflit en utilisant la commande `git rebase main` depuis votre branche locale.

## 🎮 Partie bonus : Coder un jeu

Si vous êtes arrivé jusque-là, c'est que vous êtes prêt à utiliser Git pour coder pour de vrai !
Codez un jeu de morpion en vous répartissant bien les tâches, notamment en découpant votre code en fonctions.
