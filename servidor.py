from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user='Fernando', password='Cuauhtli', database='invernadero')
cursor = conexion.cursor()

usuarioBD = Usuario(conexion, cursor)
@app.route('/')
def hola():
	return "Hola"
	
@app.route('/login/', methods=['GET'])
def login():
	if request.method == 'GET':
		u = request.args.get('user')
		p = request.args.get('pwd')
		print (u)
		print (p)
		return str(usuarioBD.login(u, p))
		
	#return "Login"
	
@app.route('/invernaderos/', methods=['POST'])
def invernaderos():
	if request.method == 'POST':
		
		objeto = [{
			'id' : 0,
			'ubicacion' : 'Revolucion',
			'nombre' : 'CUCEI',
			'cultivos' : 0
		},{
			'id' : 1,
			'ubicacion' : 'El Salto',
			'nombre' : 'Verde',
			'cultivos' : 5
		}]
		
		return jsonify(objeto)
	
app.run()