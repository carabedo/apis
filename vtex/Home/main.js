function search(){
    console.log('hola')
}

let json 

const getProductos = async (producto) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
    const response = await fetch('https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q='+producto, requestOptions);
    const json = await response.json();
  
    return json;
  };
// listener del form 
window.addEventListener("load", function () {
    let busqueda = document.querySelector("form");
    // miro el evento submit
    busqueda.addEventListener("submit", function (e) {
      // evito que mande el formulario al backend
      e.preventDefault();
      let producto = document.getElementById("input")
 
      json=getProductos(producto)

      // fetch siempre tiene 2 then, en el segundo va la accion con la data



    });
  });
  
  