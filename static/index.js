
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

function drawLine(data)
{
		console.log(data);
		
        line = new google.maps.Polyline({
		path: data,
		strokeColor: "#FF0000",
		strokeOpacity: 1.0,
		strokeWeight: 10,
		geodesic: true,
		map: map});
		
}
function selectRoute()
{
	$.getJSON('/select_route', {
		route: $("#route").val()
		}, function(data) {
				drawLine(data.result);
		});

	removeLine();
}

function removeLine() 
{
        line.setMap(null);
}

