markers = []

function populateRestaurants (res) {
    restaurants = [];

    for (var i = 0; i < res.length; i++) {
      det = {
        id: res[i].id,
        name: res[i].name,
        position: {
          lat: +res[i].lat, 
          lng: +res[i].lng
        },
        foodSpecialty: res[i].food_specialty,
        type: res[i].restaurant_type_name
      }
      restaurants.push(det);
    }
}
    
function setMarkers() {
    var marker, i,
    infowindow = new google.maps.InfoWindow();

    clearAllMarkers();

    for (i = 0; i < restaurants.length; i++) { 
        marker = new google.maps.Marker({
            position: restaurants[i].position,
            map: map,
        });

        markers.push(marker);

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                info = 
                "<div id="+restaurants[i].id+"><div><label><b>Name</b></label>: "+
                restaurants[i].name+" </div>"+
                "<div><label><b>Food Specialty</b></label>: "+
                restaurants[i].foodSpecialty+" </div>"+
                "<div><label><b>Type</b></label>: "+
                restaurants[i].type+" </div>"+
                "<div><button id='goHereButton' class='btn btn-info pull-right' onclick=goHere("+
                    restaurants[i].position.lat+","+
                    restaurants[i].position.lng+","+
                    restaurants[i].id+")>Go Here</button></div></div>";

                infowindow.setContent(info);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }
}

function clearAllMarkers() {
    for (var i = 0; i < markers.length; i++ ) {
        markers[i].setMap(null);
    }
    markers.length = 0;
}