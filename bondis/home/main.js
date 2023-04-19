var map = L.map('map').setView([-34.6037,-58.3816], 12);

L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


map.locate({setView: true, maxZoom: 16});


function onLocationFound(e) {
    var radius = e.accuracy;

    L.circle(e.latlng, 10).addTo(map);
}

map.on('locationfound', onLocationFound);