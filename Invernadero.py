class Invernadero:
	def __init__(self, conexion, cursor):
		self.c = conexion
		self.cur = cursor
	
	def agregarInvernadero(self, ubicacion, nombre, iddue):
		insertar = ("insert into invernadero (ubicacion, nombre, id_dueno) values (%s, %s, %s)")
		self.cur.execute(insertar, (ubicacion, nombre, iddue))
		self.c.commit()
		
	def agregarDueno(self, nombre, apellido):
		insertar = ("insert into dueno (nombre, apellido) values (%s, %s)")
		self.cur.execute(insertar, (nombre, apellido))
		self.c.commit()
		
	def buscarInvernadero(self, nombre):
		buscar = ("select * from invernadero where nombre like %s")
		self.cur.execute(buscar, ('%' + nombre + '%',))
		resultados = self.cur.fetchall()
		
		return resultados
		
	def getInvernaderos(self, user, password):
		select_usuario = \
			("SELECT id FROM usuario WHERE username = %s AND password = %s")
		self.cur.execute(select_usuario, (user, password))
		id = self.cur.fetchall()
		lista = []
		
		if id:
			id = id[0][0]
			print("ID usuario: ", id)
			
			select_usuario_invernadero = \
				("SELECT id_invernadero FROM usuario_invernadero WHERE id_usuario = %s")
			self.cur.execute(select_usuario_invernadero, (id, ))
			invernaderos_id = self.cur.fetchall()
			
			print('id_invernadero: ', invernaderos_id)
			
			for i in invernaderos_id:
				print (i[0]);
				inver = i[0];
				
				select_invernadero = \
					("SELECT * FROM invernadero WHERE id = %s")
				self.cur.execute(select_invernadero, (inver, ))
				res = self.cur.fetchall()
				print(res)
				
				if res:
					select_plantas = \
						("SELECT COUNT(id) FROM planta WHERE id_invernadero = %s")
					self.cur.execute(select_plantas, (res[0][0], ))
					plantas = self.cur.fetchall()
					
					inverna = {
						'id' : res[0][0],
						'ubicacion' : res[0][1],
						'nombre' : res[0][2],
						'cultivos' : plantas
					}
					
					lista.append(inverna)
			
			return lista
		