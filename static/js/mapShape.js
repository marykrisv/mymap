var rectangle;

function showShapeInMap() {

    latLng = new google.maps.LatLng(10.29093306343598, 123.87031512969945);

    const bounds = {
        north: center.lat,
        south: center.lat+0.05,
        east: center.lng+0.05,
        west: center.lng,
    };

    rectangle = new google.maps.Rectangle({
        bounds: bounds,
        editable: true,
    });

    rectangle.setMap(map);
}

function hideShapeInMap() {
    rectangle.setMap(null);
}

function getCurrentRectangleBound() {
    var bounds = rectangle.bounds;
    var pos;

    var resInsideRect = [];

    for (var i = 0; i < restaurants.length; i++) {
    pos = restaurants[i].position;

    flag = false;

    if ((pos.lng >= bounds.Sa.i && pos.lng <= bounds.Sa.j) ||
        (pos.lng <= bounds.Sa.i && pos.lng >= bounds.Sa.j)) {
            if ((pos.lat <= bounds.Wa.i && pos.lat >= bounds.Wa.j) ||
                (pos.lat >= bounds.Wa.i && pos.lat <= bounds.Wa.j)) {
                resInsideRect.push(restaurants[i]);
            }
        }       
    }

    setList(resInsideRect);
}

function setList(resInsideRect) {
    $("#listOfRes").empty();

    length = resInsideRect.length;

    if (length == 0) {
        $("#listOfRes").append("< No Restaurant Found >");
    } else {        
        $("#listOfRes").append("<label>No of Restaurants: </label><label>"+length+"</label>");        

        for (var i = 0; i < length; i++) {
            $("#listOfRes").append("<br>"+(i+1)+". "+resInsideRect[i].name);
        }
    }
}