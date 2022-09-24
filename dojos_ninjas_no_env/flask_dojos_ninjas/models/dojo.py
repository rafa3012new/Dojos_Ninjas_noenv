from flask_dojos_ninjas.config.mysqlconnection import connectToMySQL
from flask_dojos_ninjas.models import ninja

# modelar la clase después de la tabla dojos de nuestra base de datos
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #propiedad del obejto Dojo que almacenara los objetos Ninja por cada Dojo (relacion 1 a muchos)
        self.ninjas = []



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('flask_mysql_coding_dojo').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de usuarioscr
        dojos = []
        # Iterar sobre los resultados de la base de datos y crear instancias de dojos con cls
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_by_id(cls,id):
        #armar la consulta con cadenas f
        query = f"SELECT * FROM dojos where id = %(id)s;"
        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('flask_mysql_coding_dojo').query_db(query, data)
        #devolver el primerl registro de los resultados si resultados devuelve algo sino que devuelva None
        return cls(results[0]) if len(results) > 0 else None


    @classmethod
    def save(cls, data):
        query = f"INSERT INTO dojos (name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        dojo_id = connectToMySQL('flask_mysql_coding_dojo').query_db( query, data )
        return dojo_id



    @classmethod
    def update(cls, data):
        query = f"UPDATE dojos SET name = %(name)s , updated_at = NOW() WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('flask_mysql_coding_dojo').query_db( query, data )


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        data = {'id': id}
        resultado = connectToMySQL('flask_mysql_coding_dojo').query_db(query, data)
        return resultado


    @classmethod
    def Get_Dojo_With_Ninjas(cls, data):

        query = f"SELECT * FROM dojos d left join ninjas n on d.id = n.dojo_id where d.id = %(id)s;"

        resultado = connectToMySQL('flask_mysql_coding_dojo').query_db(query, data)

        #Aunque devuelva muchos registros solo importa 1 valor de dojo porque todos los registros de esta consulta son del mismo dojo
    	#se toma el primer registro de dojo para alamacenar
        dojo = cls(resultado[0])

        #iteramos ahora todos los resultados de dojo
        for row_from_db in resultado:

            #creamos la estrucutura de datos tipos diccionario para almacenarla dentro de Dojo
            #colocando ninjas.elcampo en plural como el nombre que esta arriba en la propiedad de Dojo llamada ninjas (self.nijas)
            ninja_data = {
                "id" : row_from_db["n.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db["dojo_id"],
                "created_at" : row_from_db["n.created_at"],
                "updated_at" : row_from_db["n.updated_at"]
            }

            #el primer registro tomado arriba la propiedad ninjas, que es un alista vacia
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )

        return dojo
