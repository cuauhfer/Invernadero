import hashlib

class Usuario:
	
	def ingresar(self):
		insertar = ("insert into usuario(username, password, id_tipo) values(%s, %s, %s)")
		h = hashlib.new('sha1', bytes(contra, 'utf-8'))
		contra = h.hexdigest()
		self.cur.executte(insertar, (user, contra, tipo))
	
	def login (self, u, p):
		pass_hash = hashlib.new('sha1', bytes(p, 'utf-8'))
		pass_hash = pass_hash.hexdigest()
		
		select = ("select * from usuario where username = %s ans password = %s")
		self.cur.execute(select, (u, pass_hash))
		resultado = self.cur.fetchall()
		
		if resultado:
			return True
		else:
			return False
		
		return resultados
	
class menu:
	def login(self):
		nombre = input("Nombre de usuario: ")
		password = getpass.getpass("Password: ")
		
		l = self.usuario.login(nombre, password)
		
		if l == True:
			print('Usuario Logeado')
		else:
			print('Usuario inexistente o contraseña erronea')
