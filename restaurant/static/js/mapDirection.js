function goHere(goto_lat, goto_lng) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
        (position) => {
            const dest_pos = {
            lat: goto_lat,
            lng: goto_lng
            }
            const orig_pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
            };
            
            calculateAndDisplayRoute(orig_pos, dest_pos);
        },
        () => {
            handleLocationError(true, infoWindow, map.getCenter());
        }
        );
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

function calculateAndDisplayRoute(orig_pos, dest_pos) {       
    directionsService.route(
        {
        origin: orig_pos,
        destination: dest_pos,
        travelMode: google.maps.TravelMode.DRIVING,
        },
        (response, status) => {
        if (status === "OK") {
            directionsRenderer.setDirections(response);
        } else {
            window.alert("Directions request failed due to " + status);
        }
        }
    );
}