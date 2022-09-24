from flask_dojos_ninjas.config.mysqlconnection import connectToMySQL

# modelar la clase después de la tabla usuarioscr de nuestra base de datos
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('flask_mysql_coding_dojo').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de ninjas
        ninjas = []
        # Iterar sobre los resultados de la base de datos y crear instancias de ninjas con cls
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_by_id(cls,id):
        #armar la consulta con cadenas f
        query = f"SELECT * FROM ninjas where id = %(id)s;"
        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('flask_mysql_coding_dojo').query_db(query, data)
        #devolver el primerl registro de los resultados si resultados devuelve algo sino que devuelva None
        return cls(results[0]) if len(results) > 0 else None




    @classmethod
    def save(cls, data):
        query = f"INSERT INTO ninjas (first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        ninja_id = connectToMySQL('flask_mysql_coding_dojo').query_db( query, data )
        return ninja_id



    @classmethod
    def update(cls, data):
        query = f"UPDATE ninjas SET first_name = %(first_name)s , last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('flask_mysql_coding_dojo').query_db( query, data )


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {'id': id}

        print("ejecutando consulta de borrado",end='\n\n')
        print(query)

        resultado = connectToMySQL('flask_mysql_coding_dojo').query_db(query, data)

        return resultado