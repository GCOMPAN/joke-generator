# Générateur de Blagues
Ce projet est un générateur de blagues web basé sur Flask, permettant aux utilisateurs de découvrir des blagues aléatoires dans différentes langues et catégories. Les utilisateurs peuvent également soumettre leurs propres blagues.

## Installation
Pour exécuter ce projet, vous aurez besoin de Python et de pip installés sur votre ordinateur. Après avoir cloné le dépôt, installez les dépendances nécessaires :

```bash
git clone https://github.com/GCOMPAN/joke-generator.git
cd joke-generator
pip install -r requirements.txt
```
## Utilisation
Pour lancer l'application, exécutez la commande suivante dans le dossier du projet :

```bash
flask run
```
Accédez à http://127.0.0.1:5000/ dans votre navigateur pour utiliser l'application.

## Fonctionnalités
Génération de blagues aléatoires.
Filtre des blagues par catégorie, langue, type et contenu sensible.
Soumission de nouvelles blagues par les utilisateurs. (l'api est down depuis une semaine pour cette partie la)
## Tests
Le projet inclut des tests unitaires réalisés avec Pytest. Pour exécuter les tests et générer un rapport de couverture, utilisez les commandes suivantes :

```bash
pytest
pytest --cov=.
```
Cela exécutera les tests et affichera un rapport de couverture pour le projet.