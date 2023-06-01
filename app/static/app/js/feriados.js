
const diaActual = new Date()


const añoActual = diaActual.getFullYear()



let url = "https://api.control-z.cl/api/feriados"


fetch(url)
.then(function(respuesta){
    return respuesta.json()
})
.then(function(respuesta){
 

    let proximosFeriados = respuesta.filter(feriado => {
        

        return Date.parse(feriado.fecha) > diaActual
    })

    

  
    let feriadoProximo = proximosFeriados[0]

    
    const div_feriado = document.getElementById("feriado")
    div_feriado.innerText = feriadoProximo.nombre
},"json")
