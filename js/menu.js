
let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

menu.addEventListener("click", function(){
    
    if(header.style.height == "70px" || header.offsetHeight == 70) {
        header.style.height = 70 + nav.offsetHeight + "px"
    } else {
        header.style.height = "70px"
    }



})