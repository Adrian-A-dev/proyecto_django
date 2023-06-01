let fechaHoy = new Date()
console.log(fechaHoy)
var diaActual = fechaHoy.getDate() + "/" + ("0"+(fechaHoy.getMonth()+1)).slice(-2) + "/" + fechaHoy.getFullYear()
console.log(diaActual)


$.validator.addMethod("terminaCon", function(value, element, parametro) {
    
    if(value.endsWith(parametro)) {
        return true;
    }

    return false;

}, "Debe terminar con {0}")


$.validator.addMethod("fecha", function(value, element, parametro) {


    if(Date.parse(value) < parametro ){
        return true;
    }
    else

    return false;

}, "Debe ser menor al {0}")





$("#formulario_registro").validate({
    rules: {
        rut: {
            required: true,
            minlength: 9,
            maxlength: 10,
               
        },
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 80
        },
        apellido: {
            required: true,
            minlength: 3,
            maxlength: 80
        },
        email: {
            required: true,
            terminaCon: "alumnos.duoc.cl"
        },
        fecha_nacimiento: {
            required: true,
            fecha: diaActual
            

        },
        usuario: {
            required: true,
            minlength: 8


        },
        contraseña: {
            required :true,
            minlength: 8
        }

    }
})


$("#formulario_insumos").validate({
    rules: {
        nombre_insumo:{
            required :true,
            minlength:3,
            maxlength:300

        },

        precio:{
            required :true,
            min: 1
        },

        descripcion:{
            minlength:3,
            maxlength:300
        }

    }
})





$("#guardarInsumo").click(function(){
    if($("#formulario_insumos").valid() == false){
        
        return;
    }
    let nombre_insumo = $("#nombre_insumo").val()
    let precio = $("#precio").val()
    let descripcion = $("#descripcion").val()

})

let fecha = document.getElementById("fecha")

fecha.addEventListener("click", function(){
    let fechaNacimiento = document.getElementById("fecha_nacimiento").value
    
    fechaNacimiento = fechaNacimiento.split("-").reverse().join("/")

    console.log(fechaNacimiento)
})



$("#guardar").click(function(){
    
    if($("#formulario_registro").valid() == false){
        
        return;
    }
    
    let rut = $("#rut").val()
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let email = $("#email").val()
    let fecha_nacimiento = $("#fecha_nacimiento").val()
    fecha_nacimiento = fecha_nacimiento.split("-").reverse().join("/")
    let usuario = $("#usuario").val()
    let contraseña = $("#contraseña").val()
    
    
})
