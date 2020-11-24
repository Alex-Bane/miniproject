from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    animal = requests.get("http://34.105.177.201:5001/animal")
    noise = requests.post("http://34.105.177.201:5001/animal/noise", data=animal.text)

    return render_template('index.html', animal=animal.text, noise=noise.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
