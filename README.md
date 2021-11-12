# P7_DE-MATTEIS_Ludovic
Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python

## 1. Téléchargement du projet

### Export du programme

- Télécharger le projet à partir de la commande suivante :

`

`

- Se rendre dans le dossier concerné :

`

`
### Installation du programme
- Installer et activer l'environnement virtuel :

`
$ python3 -m venv env
$ source env/bin/activate
`

- Installer les requirements :

`
$ pip install -r requirements.txt
`
### Lancement du programme 

- Pour le programme de force brute 

`$ time python bruteforce.py`

- Pour le programme optimisé 

`$ time python optimized.py`

### Comparaison avec les datasets de Sienna (supplément)

Afin de pouvoir consulter l'éxécution et les résultats de l'algorithme "optimized.py" avec les différents dataset 
de Sienna, veuillez remplacer le mot "source" à la ligne 11 du programme par "dataset1" ou "dataset2"

Exemple:

`data = pd.read_csv(source)`
remplacé par 
`data = pd.read_csv(dataset1)`