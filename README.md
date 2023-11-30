# TP Git

### Qu'est-ce que Git ?

Git est un logiciel de gestion de versions. C'est-à-dire qu'il vous aide à gérer les différentes versions de votre code, ainsi qu'à collaborer à plusieurs sur un même projet.

N'hésitez pas à vous référer au [cours](Cours.pdf) ou aux slides [slides](Slides.pdf) pour ce TP !

### Installation de git

Sur Linux, git est installé par défaut sur le système.
Pour ce qui est de Windows et MacOS, il suffit de se rendre sur <https://git-scm.com/downloads> et de suivre les instructions de Windows / MacOS selon votre système.
Après avoir téléchargé git, configurez Git pour qu’il associe vos commits à votre nom et adresse e-mail:

`git config --global user.name "Votre Nom"`

`git config --global user.email supermail@gmail.com`

### Créer un compte Github

Vous avez besoin d'un compte Github pour ce TP.
Si vous ne possédez pas encore de compte github, vous pouvez le créer sur <https://github.com/join>.

### Cloner le dépot

Pour récupérer ce dépot en local sur votre pc.

**Attention**, l'URL du dépot n'est pas l'URL dans la barre de navigation !

## Partie 1 : Hello world

### Créer une branche et un dossier

Chaque binôme travaille sur sa propre branche. Créez chez un membre du binôme votre branche (nommée `prénom1-prénom2`) avec `git branch`, puis placez vous sur celle-ci avec `git checkout`.

**A noter** : Les commandes données ici ne sont pas complètes, c'est à vous de trouver les bons arguments à ajouter ;) Vous pouvez vous aider des ressources de ce dépot ou d'Internet.

Créez aussi un dossier portant le même nom à la racine du projet, où vous placerez votre code.
Créez votre fichier de code dans le langage de votre choix (Python par exemple). Faites en sorte que celui-ci affiche `Hello world` à l’exécution.

### Partager les modifications

Toutes ces actions étant faites sur un PC, il faut les partager pour que le second membre du binôme puisse y accéder !
Il faut donc ajouter le fichier à Git et puis faire un commit.
Pensez de bien décrire ce que vous avez fait dans le message de commit ! Il faut ensuite pousser les modifications sur le depot GitHub avec `git push` (lisez bien les messages d'erreur si vous en avez, ils vont aideront à trouver la bonne commande).

Pour voir si le code a bien été partagé, rendez vous sur Github et vérifiez que votre branche est bien apparue, avec votre fichier.

### Récupérer les modifications

Une fois les modifications en ligne, il faut les récupérer sur le second PC.

Si vous essayez `git pull`, vous pouvez constater que cela ne marche pas, vous ne téléchargez pas les nouvelles modifications.

Un rapide coup d'oeil à `git branch` vous donne la liste des branches présentes sur votre pc, ainsi que la branche sur laquelle vous vous trouvez actuellement.
Vous pouvez constater que vous ne possédez que la branche `main`.
En effet, `git pull` récupère les modifications de la branche sur laquelle vous êtes actuellement, mais ne récupère pas de nouvelles branches provenant du depot distant.

Pour cela, vous pouvez utiliser `git fetch`.
Vous pouvez à nouveau consulter la liste de branches pour constater que cette fois-ci, de nouvelles branches sont apparues !

Vous pouvez maintenant vous placer sur votre branche, les modifications sont maintenant récupérées !

### Plus de modifications

C'est maintenant à l'autre membre du binôme de faire des modifications. Changez le message pour ne plus afficher `Hello world` mais `Hello INSA`. Faites en sorte que l'autre membre du binôme récupère les changements.

## Partie 2 : Travail en parallèle

Pour cette partie, vous allez utiliser le template de code. Copiez le fichier `fonctions.py` dans votre dossier, puis faites un commit avant toute modification, pour que les deux membres aient le fichier.

### Commits en parallèle

Un membre du binôme complète la fonction `addition`, et l'autre la fonction `soustraction`. Chacun pousse ensuite ses changements.

La deuxième personne va avoir une surprise : des changements ont été poussés entre temps, et git ne veut pas les écraser !

Il faut donc récupérer les modifications de la première personne et les fusionner.
Pour faire cela, il faut donner une stratégie à Git, nous allons utiliser le rebase. Vous pouvez donc récupérer puis rebase en ajoutant `--rebase` à la commande que vous utilisez pour récupérer les modifications.

### Résolution de conflit

Dans cette partie, les deux membres du binôme vont modifier la même fonction, `noms_binome`, qui doit afficher vos noms sur deux lignes différentes. Chacun rajoute le code pour afficher son nom et seulement son nom. Faites ensuite un commit et pousser vos changements.

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

## Partie 3 : Mettre vos modifications sur la branche main

Avant de continuer, ajoutez les noms de votre binôme dans le fichier `NOMS.txt` à la racine du projet.

Le but est maintenant d'ajouter vos modifications sur la branche `main`. Cette branche étant protégée, vous ne pouvez pas mettre directement le code de votre branche dessus. Pour faire cela, vous devez passer par les **pull requests**.
Créez une pull request, faites bien attention au titre et à la description afin que l'on sache en quoi votre code consiste !

Comme vous avez modifié le fichier `NOMS.txt`, GitHub vous indiquera que vous ne pouvez pas fusionner vos changements avec la branche main car il y a des conflits (les autres binômes on rajouter le leur sur la même ligne). Aidez-vous de l'explication plus haut pour régler ce/ces conflit(s) en utilisant la commande `git rebase main` depuis votre branche binôme.
Une fois cela fait, votre pull request pourra être validée par un administrateur du dépôt GitHub et vos modifications pourront être mises dans la branche `main`.

## Partie bonus : Coder un jeu

Si vous êtes arrivé jusque-là, c'est que vous êtes prêt à utiliser Git pour coder pour de vrai !
Codez un jeu de morpion en vous répartissant bien les tâches, notamment en découpant votre code en fonctions.
