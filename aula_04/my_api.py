import pickle
from flask import Flask, jsonify

app = Flask(__name__)

my_data = pickle.load(open('serializado.pkl', 'rb'))

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World alterado'

@app.route('/saudacao/<nome>', methods=['GET'])
def saudar(nome):
    return f'Ola, {nome}'

@app.route('/suggestions/<user_id>', methods=['GET', ])
def get_suggestion(user_id):    
    return jsonify(my_data.get(user_id, {}))
