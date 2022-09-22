function updatePostName(id) {
    var name = prompt('Introduzca el nombre del Dojo:','Actualziando el Dojo');

        if(name != null && name != "")
        {
         if (confirm("Desea actualizar el nombre del dojo?")){

            var fecha = new Date()
            //se envia la informacion del prompt via ajax usando fetch


            //se arma una variable json
            let data = {
                "id": id,
                "name": name,
                "updated_at":fecha
            }
            //se ejecuta el fetch de tipo POST y la promesa
            fetch("/actualizardojo", {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body":  JSON.stringify(data),
           }).then(function(response){
                 return response.json()
                 //return name;
             })
             .then(function(data){
                 alert(response.json())
             });

            //return old_name;
        }
    }
}