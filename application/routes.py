from flask import render_template, redirect, url_for, request, jsonify
from application.models import Animals
import random 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/animal')
def animal():
   random_animal = random.randint(0,4) 
    if random_animal == 0:
       animal = "cow"
    elif random_animal == 1:
       animal = "Dog"
    elif random_animal == 2:
       animal = "Cat"
    elif random_animal == 3:
        animal = "Sheep"
    else:
        animal = "Hotse"
    sound = Animals.animals[animal]
    
    return render_template("animals.html", animal = animal, noise = sound)

