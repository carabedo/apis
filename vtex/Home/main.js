// // listener del form 
// window.addEventListener("load", function () {
//     let busqueda = document.querySelector("form");
//     // miro el evento submit
//     busqueda.addEventListener("submit", function (e) {
//     e.preventDefault()

//     // evito que mande el formulario al backend

//     (async () => {
//     let producto = document.getElementById("input").value
//     await fetchProductos(producto);
//     console.log(productosData);
//     })();
//     // fetch siempre tiene 2 then, en el segundo va la accion con la data



//     });
//   });

let productosData


const fetchProductos = async (producto) => {
    
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json")
    // myHeaders.append('Access-Control-Allow-Origin','*')
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
      };
    const response = await fetch('https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q='+producto, requestOptions);
    const json = await response.json();
    productosData = json;
};

const btnBusca = document.getElementById('boton');
btnBusca.addEventListener('click', async (e) => {
  e.preventDefault()
  let producto = document.getElementById("input").value

  await fetchProductos(producto);
  console.log(productosData);
  for(var key in productosData) {
    var node = document.createElement("li");
    var textnode = document.createTextNode(productosData[key].name+' dia: '+productosData[key].precio_dia+'$ carrefour: '+productosData[key].precio_carrefour+'$ chango: '+productosData[key].precio_chango);
    node.appendChild(textnode);
    document.getElementById("lista").appendChild(node);
   }
});