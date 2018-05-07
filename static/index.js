
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
				currentRoute = data.result;
				//console.log(currentRoute.length);
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
		removeLine();
		var newRoute = dividingRoute(currentRoute, A, B);
		
		removedRoute = newRoute;
		
		
		line = new google.maps.Polyline({
			path: newRoute,
			strokeColor: "#FF0000",
			strokeOpacity: 1.0,
			strokeWeight: 10,
			geodesic: true,
			map: map});
	}
	
	
	
	
}

function outerRoute(route, A, B)
{
	A=dividingRoute(route,1,A);
    B=dividingRoute(route,B,100);
    var mergelist= A+B;
	//console.log(A);
	return mergelist;
}

function dividingRoute(route, A, B)
{
	A = Number(route.length * (A/100));
	B = Number(route.length * (B/100));
	
	return route.slice(A,B)
}

function predictRoute()
{
	
	var newLine = new google.maps.Polyline({
					path: removedRoute,
					strokeColor: "#A9A9A9",
					strokeOpacity: 1.0,
					strokeWeight: 10,
					geodesic: true,
					map: map});
	
/*	$.ajax({
		//progressbar start
		xhr: function () {
        var xhr = $.ajaxSettings.xhr();
        xhr.onprogress = function e() {
            // For downloads
            if (e.lengthComputable) {
                console.log(e.loaded / e.total);
            }
        };
        xhr.upload.onprogress = function (e) {
            // For uploads
            if (e.lengthComputable) {
                console.log(e.loaded / e.total);
            }
        };
        return xhr;
		},
		//progressbar end
		dataType: "json",
		url: '/predict_route',
		data: {A: AP, B: BP},
		success: function(data) {
			$("#probability").val(data.probability);
			removeLine();
			console.log(data);
			var mostProbableLine = new google.maps.Polyline({
				path: data.routePrint,
				strokeColor: "#008000",
				strokeOpacity: 1.0,
				strokeWeight: 10,
				geodesic: true,
				map: map});
					
			var altline = new google.maps.Polyline({
				path: data.altRoute,
				strokeColor: "#0000ff",
				strokeOpacity: 1.0,
				strokeWeight: 10,
				geodesic: true,
				map: map});	
				//getSimilarity(removedRoute, data.routePrint);
				}
	});
*/
	$.getJSON('/predict_route', {
		A: AP, B: BP 
		}, function(data) {
				$("#probability").val(data.probability);
				removeLine();
				console.log(data);
				var mostProbableLine = new google.maps.Polyline({
					path: data.routePrint,
					strokeColor: "#008000",
					strokeOpacity: 1.0,
					strokeWeight: 10,
					geodesic: true,
					map: map});
					
				var altline = new google.maps.Polyline({
					path: data.altRoute,
					strokeColor: "#0000ff",
					strokeOpacity: 1.0,
					strokeWeight: 10,
					geodesic: true,
					map: map});	
					//getSimilarity(removedRoute, data.routePrint);
				console.log(data.start);

				//var flightPlanCoordinates = data.first.concat(data.second);
				//var flightPlanCoordinates = data.start+data.end;
				var flightPath = new google.maps.Polyline({
					path: data.start,
					geodesic: true,
					strokeColor: '#FF0000',
					strokeOpacity: 1.0,
					strokeWeight: 2
					});

					flightPath.setMap(map);

				});
				
	
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