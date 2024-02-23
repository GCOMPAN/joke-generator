from flask import Flask, request, render_template
import requests
import yaml

with open("config.yml", "r") as config_file:
    config_data = yaml.safe_load(config_file)

app = Flask(__name__)

# Endpoint pour obtenir les catégories
CATEGORIES_ENDPOINT = "https://v2.jokeapi.dev/categories"

# Fonction pour récupérer les catégories disponibles
def get_categories():
    response = requests.get(CATEGORIES_ENDPOINT)
    data = response.json()
    return data['categories']

# Route principale pour afficher le formulaire et les blagues
@app.route('/', methods=['GET', 'POST'])
def index():
    joke = None
    if request.method == 'POST':
        if 'like' in request.form:
            # Sauvegarder la blague likée
            with open('liked_jokes.txt', 'a') as file:
                file.write("-------------------\n")
                file.write(f"{request.form['joke']}\n")
        else:
            # Obtenir une blague de la catégorie sélectionnée
            category = request.form.get('category')
            joke_response = requests.get(f"https://v2.jokeapi.dev/joke/{category}")
            joke_data = joke_response.json()
            if joke_data['type'] == 'single':
                joke = joke_data['joke']
            else:
                joke = f"{joke_data['setup']} ... {joke_data['delivery']}"
    categories = get_categories()
    return render_template('index.html', categories=categories, joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
