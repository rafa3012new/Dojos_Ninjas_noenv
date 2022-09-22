#se importa el app
from unittest import result
from flask_dojos_ninjas import app
#se importa el modelo que contiene la clase
from flask_dojos_ninjas.models.dojo import Dojo
from flask_dojos_ninjas.models.ninja import Ninja
#se importa las funciones de flask
from flask import render_template, redirect, request, session, flash, jsonify
#se importan el modulo de fechas
from datetime import datetime


@app.route("/limpiar")
def limpiar():
   session.clear()
   flash("se limpio la session","info")
   return redirect("/")

#Funcion para obtener los registros de todos los dojos
# obtiene todos los dojos y las devuelve en una lista de objetos de los dojos
@app.route('/')
def mostrar_dojos():
  return render_template('main_dojos.html',dojos=Dojo.get_all())


#Funcion para crear un dojo en la db con los datos que vienen de un formulario
#Merodo Post para recibir los datos de un formulario o popupinput
@app.route('/creardojo',methods=['POST'])
def crear_dojo():

   data = {"name" : request.form['nombre_dojo'],
           "created_at" : datetime.today(),
           "updated_at" : datetime.today()}

   resultado = Dojo.save(data)

   if resultado == False:
    flash(f"Exito al crear el Dojo {data['name']}","success")
   else:
    flash(f"Error al crear el Dojo {data['name']}","error")

   return redirect('/limpiar')


#Funcion para editar un Dojo en la db con los datos que vienen de un formulario o popupinput
#Metodo Post para recibir los datos de un formulario o popupinput
@app.route("/actualizardojo", methods=["POST"])
def actualizar_dojo():

   #la variable data obtiene via request.jason la variable data enviada por fetch desde javascript
   data =  request.json
   print(data,flush=True)

   resultado = Dojo.update(data)
   resultado = data
   #print("respuesta de la actializacion desde el save del archivo modelo Dojos:",flush=True)
   print(resultado,flush=True)

   if resultado == False:
      mensaje = f"Error al actualizar el Dojo {data['name']}"
      flash(mensaje,"error")
   else:
      mensaje = f"Exito al actualizar el Dojo {data['name']}!!!"
      flash(mensaje,"success")

   return jsonify(message=mensaje)


#Funcion para eliminar un Dojo en la base de datos
@app.route('/eliminardojo/<int:id>')
def eliminar_dojo(id):

   #se elimina en el el objeto de la clase Dojo
   resultado = Dojo.delete(id)

   if resultado == False:
      flash(f"Error al eliminar el Dojo {id}","error")
   else:
      flash(f"Exito al eliminar el Dojo {id}","success")


   return redirect('/limpiar')


#Funcion para obtener los registros de todos los ninjas filtrados por dojo
@app.route('/mostrarninjaspordojo/<int:id>')
def mostrar_ninjas_dojo(id):
   resultado = dojos=Dojo.get_ninjas_by_id(id)
   if resultado == False:
     flash("Error al obtener el registro de ninjas por dojo","error")
   else:
     flash("Se ha obtenido el registro de ninjas por dojo con exito","success")

   return render_template('submain_ninjas.html',result)


#Funcion para insertar un nuevo ninja
# se llama al formulario para insertar
@app.route('/insertarninja')
def insertar_ninja():
   return render_template("ninja_insertar.html")


#Funcion para crear un registro de un ninja
#Metodo Post
@app.route('/editarninja/<int:id>')
def editar_ninja(id):
   return render_template("ninja_editar.html", ninja=Ninja.get_by_id(id))


#Funcion para crear un ninja en la db con los datos que vienen de un formulario
#Metodo Post para recibir los datos de un formulario o popupinput
@app.route('/crearninja',methods=['POST'])
def crear_ninja():

  data = {"first_name" : request.form['nombre_ninja'],
          "created_at" : datetime.today(),
          "updated_at" : datetime.today()}

  resultado = Ninja.save(data)

  if resultado == False:
     flash(f"Error al eliminar el Dojo {data['first_name']} {data['last_name']}","error")
  else:
     flash(f"Exito al crear el Dojo {data['last_name']} {data['last_name']}","success")

  return redirect('/limpiar')



#Funcion para editar un ninja en la db con los datos que vienen de un formulario
#Metodo Post para recibir los datos de un formulario o popupinput
@app.route('/actualizarninja',methods=['POST'])
def actualizar_ninja():

  data = {"first_name" : request.form['nombre_ninja'],
         "created_at" : datetime.today(),
         "updated_at" : datetime.today()}

  resultado = Ninja.save(data)

  if resultado == False:
     flash(f"Error al eliminar el Dojo {data['first_name']} {data['last_name']}","error")
  else:
     flash(f"Exito al crear el Dojo {data['last_name']} {data['last_name']}","success")

  return redirect('/limpiar')


#Funcion para eliminar un Ninja en la base de datos
@app.route('/eliminarninja/<int:id>')
def eliminar_ninja(id):

   #se elimina en el el objeto de la clase Ninja
   resultado = Dojo.delete(id)

   if resultado == False:
      flash(f"Error al eliminar el Ninja {id}","error")
   else:
      flash(f"Exito al eliminar el Ninja {id}","success")


   return redirect('/limpiar')