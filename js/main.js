// Create info popup on each feature
function addInfoPopup(feature, layer) {
    if (feature.properties ) {
        var content = "<table class='table'>";
        for (var key in feature.properties) {
            content += "</tr><td>"+key+"</td><td>"+feature.properties[key]+"</td></tr>"
        }
        content += "</table>"
        layer.bindPopup(content);
    }
}

$(function() {
    var map = L.map('map', {
        center: [-0.4963315, 104.3971294],
        zoom: 11,
        layers: []
    });

    var tileLayer =  L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var dataset = {
        administrative: './data/singkep-administrative.geojson',
        coastline: './data/singkep-coastline.geojson',
        lahanKritis: './data/singkep-lahan-kritis.geojson',
        mountain: './data/singkep-mountain.geojson',
        village: './data/singkep-village.geojson'
    };

    var overlayMaps = {};
    var count = 0;

    $.each(dataset, function(key, value) {
        $.getJSON(value, function(geojsonFeature) {
            var layer = L.geoJSON(geojsonFeature, {
                onEachFeature: addInfoPopup
            });
            overlayMaps[key] = layer;
            count++;
            // If all layer has been initilalized
            if(count === Object.keys(dataset).length) {
                console.log(overlayMaps);
                L.control.layers(null, overlayMaps, {collapsed:false}).addTo(map);
            }
        });
    });
});
