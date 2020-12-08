var resId;

function goHere(goto_lat, goto_lng, id) {
    resId = id;
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
                console.log("Browser doesn't support Geolocation");
            }
        );
    } else {
        // Browser doesn't support Geolocation
        console.log("Browser doesn't support Geolocation");
    }
}

function addStopButton() {
    $("#"+resId).append("<button id='stopButton' class='btn btn-warning' onclick='stopDirection()'>Stop</button>");
}

function stopDirection() {
    directionsRenderer.setMap(null);
    $("#stopButton").remove();
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
                addStopButton();
            } else {
                window.alert("Directions request failed due to " + status);
            }
        }
    );
}