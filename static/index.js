
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

function drawLine()
{
	
        line = new google.maps.Polyline({
		path: currentRoute,
		strokeColor: "#000000",
		strokeOpacity: .75,
		strokeWeight: 8,
		geodesic: true,
		map: map});
		
}
function selectRoute()
{
	$.getJSON('/select_route', {
		route: $("#route").val()
		}, function(data) {
				currentRoute = data.result;
				drawLine();
				
		});

	if(line != null)
	{
		removeLine();
	}
}

function removeLine() 
{
	line.setMap(null);
}



function cutRoute(A, B)
{
	
	if(line != null)
	{
		if(aline != null && bline != null)
		{
			aline.setMap(null);
			bline.setMap(null);
		}
		removeLine();
		var newRoute = outerRoute(currentRoute, A, B);
		
		removedRoute = dividingRoute(currentRoute,A,B);
		aline = new google.maps.Polyline({
			path: newRoute[0],
			strokeColor: "#000000",
			strokeOpacity: .75,
			strokeWeight: 8,
			geodesic: true,
			map: map});
			
		bline = new google.maps.Polyline({
			path: newRoute[1],
			strokeColor: "#000000",
			strokeOpacity: .75,
			strokeWeight: 8,
			geodesic: true,
			map: map});
			
		customMarkers(newRoute[0], newRoute[1]);
	}
}

function customMarkers(A, B)
{
	var iconBase = '/static/';
	
	var iconA = {
    url: iconBase + 'markerA.png', // url
    scaledSize: new google.maps.Size(40, 40), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
	};
	
	var iconB = {
    url: iconBase + 'markerB.png', // url
    scaledSize: new google.maps.Size(40,40), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
	};
	


	
	if(markerA != null && markerB != null)
	{
		markerA.setMap(null);
		markerB.setMap(null);
	}
	
	markerA = new google.maps.Marker({
            position: A[A.length-1],
            icon: iconA,
            map: map
          });
	markerB = new google.maps.Marker({
            position: B[0],
            icon: iconB,
            map: map
          });	
}

function outerRoute(route, A, B)
{
	A=dividingRoute(route,1,A);
    B=dividingRoute(route,B,100);
    var mergelist= A.concat(B);
	console.log(A);
	return [A,B];
}

function dividingRoute(route, A, B)
{
	A = Number(route.length * (A/100));
	B = Number(route.length * (B/100));
	
	return route.slice(A,B)
}

function linearInterpolation(coordinates)
{
	var flightPath = new google.maps.Polyline({
		path: coordinates,
		geodesic: true,
		strokeColor: '#696969',
		strokeOpacity: .75,
		strokeWeight: 8,
		map: map
		});
}

function predictRoute()
{
	var newLine = new google.maps.Polyline({
					path: removedRoute,
					strokeColor: "#A9A9A9",
					strokeOpacity: .75,
					strokeWeight: 8,
					geodesic: true,
					map: map});

	$('#loadingmessage').show();
	$.getJSON('/predict_route', {
		A: AP, B: BP 
		}, function(data) {
				$("#probability").val(data.probability);
				removeLine();
				//console.log(data);
					
				for(var i = 0; i < data.routePrint.length; i++){
				if(i != data.index_max){
				var altline = new google.maps.Polyline({
					path: data.routePrint[i],
					strokeColor: "#696969",
					strokeOpacity: .75,
					strokeWeight: 8,
					geodesic: true,
					map: map});	
				}
				}
				var mostProbableLine = new google.maps.Polyline({
					path: data.routePrint[data.index_max],
					strokeColor: "#008000",
					strokeOpacity: 1,
					strokeWeight: 10,
					geodesic: true,
					map: map});
					//getSimilarity(removedRoute, data.routePrint);

				$('#loadingmessage').hide();
		
				linearInterpolation(data.start);
				
				drawGrid(data.centroids);
				console.log(data.centroids)
		});
}

function drawGrid(coordinates)
{
	for (var i = 0; i < coordinates.length; i++) 
	{
		var cityCircle = new google.maps.Circle({
		strokeColor: '#FF0000',
		strokeOpacity: 0.8,
		strokeWeight: 2,
		fillColor: '#FF0000',
		fillOpacity: 0.35,
		map: map,
		center: coordinates[i],
		radius: 25
		});
				
	}
}

function getSimilarity(r1, r2)
{
	var url='https://cs.uef.fi/mopsi/routes/similarityApi/index.php';
	var param={
	  measure:"C-SIM",
	  A:r1,
	  B:r2,
	  threshold:25
	}
	
	var dataString="param="+JSON.stringify(param);
	
	$.post(url, {data: dataString})
	.done(function(data){
		console.log(data);
	});

}