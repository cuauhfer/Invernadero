from flask import Flask, request, jsonify

app = Flask(__name__)

import mysql.connector
from usuario import Usuario
from Invernadero import Invernadero

conexion = mysql.connector.connect(user='Fernando', password='Cuauhtli', database='invernadero')
cursor = conexion.cursor()

usuarioBD = Usuario(conexion, cursor)
invernaderoBD = Invernadero(conexion, cursor)
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
		
		if request.is_json:
			json = request.get_json()
			print(json)
			
			u = json['user']
			p = json['pwd']
			
			print(u, p)
		objeto = invernaderoBD.getInvernaderos(u, p)
			
		return jsonify(objeto)
	
app.run()