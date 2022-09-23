from flask_dojos_ninjas.config.mysqlconnection import connectToMySQL
from flask_dojos_ninjas.models.ninja import Ninja

# modelar la clase Ninja_Dojo que hereda de la clase Padre Ninja para que herede sus propiedades y metodos
class Ninjas_Dojo(Ninja):
    def __init__( self , data ):
        self.dojo_id = data['d.id']
        self.dojo_name = data['name']
        self.ninja_id = data['id']
        self.ninja_first_name = data['first_name']
        self.ninja_last_name = data['last_name']
        self.ninja_age = data['age']
        self.ninja_created_at = data['created_at']
        self.ninja_updated_at = data['updated_at']

#se agrega a esta clase un unico metodo adicional para lo que se necesita
    @classmethod
    def get_ninjas_by_dojoid(cls,id):
        #armar la consulta con cadenas f

        query= f"SELECT * FROM ninjas n left join dojos d on d.id = n.dojo_id where d.id = %(id)s;"


        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('flask_mysql_coding_dojo').query_db(query,data)

        # crear una lista vacía para agregar nuestras instancias de dojos
        ninjas_dojo = []
        # Iterar sobre los resultados de la base de datos y crear instancias de dojos con cls
        for ninja_dojo in results:
            ninjas_dojo.append( cls(ninja_dojo) )
        return ninjas_dojo


