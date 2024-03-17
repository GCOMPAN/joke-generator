from flask import Flask, request, render_template
import requests

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
    joke = "Click the button to get a joke..."
    if request.method == 'POST':
        category = request.form.get('category', 'Any')
        lang = request.form.get('lang', 'en')
        joke_type = request.form.get('type', 'any')
        blacklistFlags = request.form.get('blacklistFlags', '')

        url = f"https://v2.jokeapi.dev/joke/{category}?lang={lang}&type={joke_type}&blacklistFlags={blacklistFlags}"
        response = requests.get(url)
        joke_data = response.json()

        if not joke_data.get('error'):
            if 'like' in request.form:
                # Sauvegarder la blague likée
                with open('liked_jokes.txt', 'a') as file:
                    file.write("-------------------\n")
                    file.write(f"{request.form['joke']}\n")
            if joke_data.get('type') == 'single':
                joke = joke_data.get('joke', "Joke not found.")
            elif joke_data.get('type') == 'twopart':
                setup = joke_data.get('setup', "Setup not found.")
                delivery = joke_data.get('delivery', "Delivery not found.")
                joke = f"{setup} ... {delivery}"
        else:
            # Improved error handling
            error_message = joke_data.get('message', 'An error occurred, but no specific message was provided.')
            joke = f"Error retrieving joke: {error_message}"

    categories = get_categories()
    return render_template('index.html', categories=categories, joke=joke)


if __name__ == '__main__':
    app.run(debug=True)