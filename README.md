# TP Git

### Qu'est-ce que Git ?

Git est un logiciel de gestion de versions. C'est-à-dire qu'il vous aide à gérer les différentes versions de votre code, ainsi qu'à collaborer à plusieurs sur un même projet.

### Installation de git

Sur Linux, git est installé par défaut sur le système.
Pour ce qui est de Windows et MacOS, il suffit de se rendre sur <https://git-scm.com/downloads> et de suivre les instructions de Windows / MacOS selon votre système.

### Créer un compte Github
Vous avez besoin d'un compte Github pour ce TP.
Si vous ne possédez pas encore de compte github, vous pouvez le créer sur <https://github.com/join>.

### Objectifs du TP

L'objectif de ce TP est de créer en binome un Plus Ou Moins pour vous apprendre à collaborer avec Git.
Le choix du langage de programmation est complètement libre.

### Cloner le dépot

Pour récupérer ce dépot en local sur votre pc.

**Attention** l'URL du dépot n'est pas l'URL dans la barre de navigation !

### Créer une branche et un dossier

Chaque binome travaille sur sa propre branche. Créez chez un membre votre propre branche (nommée `prémom1-prénom-2`) puis placez vous sur celle-ci.
Créez aussi un dossier du portant le même nom à la racine du projet, votre code sera placé dans ce dossier.

### Hello, world

Une fois ce dossier créé, créez votre fichier de code, faites en sorte que celui-ci affiche `Hello, world` à l'éxécution.

### Partager les modifications

Toutes ces actions étant faites sur un PC, il faut les partager pour que le second membre du binome puisse y accéder !
N'oubliez pas de bien décrire que que vous avez fait dans le message de commit !
Pour vérifier que les modifications que vous avez faites ont bien été partagées, rendez vous sur Github et vérifiez que votre branche est bian apparue et qu'elle contient bien vos modifications.

### Récupérer les modifications

Une fois les modifications en ligne, il faut les récupérer sur le second PC.

Si vous essayez `git pull`, vous pouvez constater que cela ne marche pas, vous ne télécharger pas les nouvelles modifications.

Un rapide coup d'oeil à `git branch` vous donne la liste des branches présentes sur votre pc, ainsi que la branche sur laquelle vous-vous trouvez actuellement.
Vous pouvez constater que vous ne possédez que la branche `main`.
En effet, `git pull` récupère les modifications de la branche sur laquelle vous êtes actuellement, mais ne récupère pas de nouvelles branches provenant du dépot distant.

Pour cela, vous pouvez utiliser `git fetch`.
Pous pouvez à nouveau consulter la liste de branches pour constater que cette fois-ci, de nouvelles branches sont apparues !

Vous pouvez maintenant vous placer sur votre branche, le modifications sont maintenant récupérées !

### Coder le jeu

C'est le moment de coder la logique du jeu. Pour bien utiliser les possibilités que vous offre git, pensez à répartir le travail entre les membres du binôme !

### Fusionner votre travail

Une fois que chacun a fini son travail il faut fusionnez le travail des deux membres du binômes afin d'obtenir un programme (normalement) fonctionnel.

Avez-vous une idée de comment faire ?

`push` les modifications est un bon début, mais vous allez vite rencontrer un obstacle. En effet, git ne sait pas comment réconcilier les modifications des deux personnes !
Il faut donc l'aider !

Si tout s'est bien passé, au moins une personne a pu `push` (n'oubliez pas de `add` et `commit` avant) ses modifications, mais la deuxième personne se voit refuser le droit de partager les siennes.
La deuxième personne doit donc récupérer les modification de la première et fusionner les modifications.
Pour faire cela, il faut donner une stratégie à Git, nous allons utiliser le rebase, vous pouvez donc récupérer puis rebase en faisant `git pull --rebase`.

Si vous avez de la chance, git sait automatiquement fusionner les modification du fichier source.
Avec moins de chance, il faut faire manuellement le travail de fusion des deux codes.
Si il y a un conflit, git génère dans le fichier de nouvelles lignes pour vaus aider à comprendre où sont les problèmes. Les lignes se présentent sous ce type :
```cpp
<<<<<<< HEAD
int a = 1;
=======
int a = 2;
>>>>>>> branche_a_merge 
```

Réglez tous les conflits et effaces ces lignes ajoutées par git. Une fois cela fait, terminez le rebase avec `git rebase --continue`.

Une fois le rebase terminé, pous devriez enfin pouvoir `push` vos modifications.

Comment auriez-vous pu faire pour avoir moins de difficultés à fusionner ? 

### Mettre vos modifications dans la branche main

La branche `main` étant protégée, vous ne pouvez pas mettre directement le code de votre branche dessus. Pour faire cela, vous devez passer par les **pull requests**.
Créez une pull request, faites bien attention au titre et à la description afin que l'on sache en quoi votre code consiste !
Une fois cela fait, vos modifications pourront être mises dans la branche `main` par un administrateur du dépot sur Github.

