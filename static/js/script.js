let submit = document.getElementById('save');

submit.addEventListener('click', function(e) {
    alert('Operator added Successfully');
});

//mapclick
var map = L.map('map', {doubleClickZoom: false}).locate({setView: true, maxZoom: 16});
map.on('click', function(e){
    var marker = new L.marker(e.latlng).addTo(map);
});

var marker;
map.on('locationfound', function(ev){
    var marker = new L.marker(e.latlng).addTo(map);
    marker.setLatLng(ev.latlng);
    marker.addTo(map);
})

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    id: 'examples.map-i875mjb7',
    noWrap : true
}).addTo(map);
