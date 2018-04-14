
function initMap() {
	
	var directionsService = new google.maps.DirectionsService;
	var directionsDisplay = new google.maps.DirectionsRenderer;
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 11,
		center: {lat: 62.6010, lng: 29.7636},
		minZoom: 5,
		maxZoom: 20
	});
	directionsDisplay.setMap(map);
	
	
}

function drawRoute(){	
	var jsonParameters={};
	
	jsonParameters["request_type"]="get_route";

	var path;
	para=JSON.stringify(jsonParameters);	
	
	$.post("server.php", { data: para })
    .done(function(data) {
		var paths= eval("(" + data + ")");
		console.log(paths.length);
        var line = new google.maps.Polyline({
		path: paths,
		strokeColor: "#FF0000",
		strokeOpacity: 1.0,
		strokeWeight: 10,
		geodesic: true,
		map: map});
    });
	
	
}
