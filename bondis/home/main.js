var map = L.map('map').setView([-34.6037,-58.3816], 12);

L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


map.locate({setView: true, maxZoom: 15});


function onLocationFound(e) {
    var radius = e.accuracy;

    L.circle(e.latlng,  {
        color: 'red',
        fillColor: 'red',
        fillOpacity: 1,
        radius: 10
    }).addTo(map);
    lat=e.latlng['lat']
    lon=e.latlng['lon']
    radio=0.01
    getBondis(lat,lon,radio,map)

}

map.on('locationfound', onLocationFound);


function getBondis(lat,lon,radio,map){

    lat=-34.654756208531126
    lon= -58.34646820091482
    radio=0.01

    url_base='http://cuandosubo.sube.gob.ar/onebusaway-api-webapp/api/where/'
    url_endpoint='trips-for-location.json?'
    url=url_base+url_endpoint+'lat='+lat.toString()+'&lon='+lon.toString()+'&latSpan='+ radio.toString() + '&lonSpan='+radio.toString()+'&app_ver=137&includeStatus=true&app_uid=786390b9-e7a3-44b6-bc1e-4ce5eed18b52&version=2&key=CuandoSUBO-Android-9b8a8543-b111-4caf-80b0-b81978707a0c'


    L.circle([lat,lon], {
        color: 'black',
        fillColor: 'black',
        fillOpacity: 0.5,
        radius: 5
    }).addTo(map).bindTooltip("culito2 ");

}