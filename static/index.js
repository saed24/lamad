
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
	//console.log(A);
	return [A,B];
}

function dividingRoute(route, A, B)
{
	A = Number(route.length * (A/100));
	B = Number(route.length * (B/100));
	
	return route.slice(A,B)
}
var flightPath;
function linearInterpolation(coordinates)
{
		flightPath= new google.maps.Polyline({
		path: coordinates,
		geodesic: true,
		strokeColor: '#696969',
		strokeOpacity: .75,
		strokeWeight: 8,
		map: map
		});
		getSimilarity(removedRoute, coordinates);
}


var mostProbableLine;
function predictRoute()
{
	
	$('#loadingmessage').show();
	$.getJSON('/predict_route', {
		A: AP, B: BP 
		}, function(data) {
				myJson=data;
				//$("#probability").val(data.probability);
				removeLine();
				probablelines()
				$('#loadingmessage').hide();
				document.getElementById("parent_div_1").innerHTML = createCheckboxes(data);
		});
	
}
var newLine;
function originalroute()
{
	newLine = new google.maps.Polyline({
					path: removedRoute,
					strokeColor: "#A9A9A9",
					strokeOpacity: .75,
					strokeWeight: 8,
					geodesic: true,
					map: map});
					
}

var altline;
var counter=0;



function createCheckboxes(data)
{
	var html = "<h4>Options</h1> <label class='container'>Predicted Route"+ 
	"<input type='checkbox' checked='checked' id='checkbox1' onclick='checkboxfunction1()'>" +
	"<span class='checkmark'></span> </label>"  +
	"<label class='container'>Linear Route" +
	"<input type='checkbox' id='checkbox2' onclick='checkboxfunction2()'>" +
	"<span class='checkmark'></span></label>" +
	"<label class='container'>Original Route" +
	"<input type='checkbox' id='checkbox4' onclick='checkboxfunction4()'>"+
	"<span class='checkmark'></span></label>";
	console.log(data.routePrint.length);
	for(var i = 0; i < data.routePrint.length; i++)
	{
		if( i !== data.index_max)
		{
			html += "<label class='container'>Alternative Route " +(i+1)+
			"<input type='checkbox' id='altCheckbox"+i+"'  onclick='alternativeCheckbox("+JSON.stringify(data.routePrint[i])+", "+JSON.stringify(i)+")'>" +
			"<span class='checkmark'></span> </label>" ;
			//altLine=data.routePrint[i];
		}
	}

	return html;
}

function alternativeCheckbox(route,checkBoxNo)
{
	console.log(route);

	var checkBox = document.getElementById("altCheckbox"+checkBoxNo);

  // If the checkbox is checked, display the output text
	if (checkBox.checked == true){
		console.log("true");
		altline = new google.maps.Polyline({
				path: route,
				strokeColor: "#696969",
				strokeOpacity: .75,
				strokeWeight: 8,
				geodesic: true,
				map: map});	
		getSimilarity(removedRoute, myJson.routePrint[checkBoxNo]);
					
					$("#probability").val(myJson.probability[checkBoxNo]);
	} 
	else 
	{
	  altline.setMap(null);
	}
}

function probablelines()
{
					mostProbableLine = new google.maps.Polyline({
					path: myJson.routePrint[myJson.index_max],
					strokeColor: "#008000",
					strokeOpacity: 1,
					strokeWeight: 10,
					geodesic: true,
					map: map});
					console.log("begin");
					//console.log(removedRoute);
					//console.log("###############################################################");
					//console.log(myJson.routePrint[myJson.index_max]);
					//console.log("end");
					getSimilarity(removedRoute, myJson.routePrint[myJson.index_max]);
					drawGrid(myJson.centroids);
					$("#probability").val(myJson.probability[myJson.index_max]);
}

var cityCircle=[];

function drawGrid(coordinates)
{
	for (var i = 0; i < coordinates.length; i++) 
	{
		cityCircle[i] = new google.maps.Circle({
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
function removeGrid(coordinates)
{
	for (var i = 0; i < coordinates.length; i++) 
	{
		cityCircle[i].setMap(null);
		//console.log(i);
				
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
	
	/*$.post(url, {data: dataString})
	.done(function(data){
		console.log(data);
	});
	*/
	httpPostAsync(url, dataString, function(data){ 
	
	var similarityPercent = eval("(" +data+ ")");
	$("#Similarity").val(similarityPercent['similarity']);
	//console.log(similarityPercent['similarity']);
	});

}

function httpPostAsync(url, dataString, callback){
	var request = new XMLHttpRequest();
	request.open('POST', url, true);
	request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	request.onreadystatechange = function() { 
        if (request.readyState == 4 && request.status == 200){
            callback(request.responseText);
		}
    }
	request.send( dataString );
}

function checkboxfunction1() {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox1");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    probablelines();
  } else {
    mostProbableLine.setMap(null);
	removeGrid(myJson.centroids);
  }
}

function checkboxfunction2() {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox2");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    linearInterpolation(myJson.start);
  } else {
    flightPath.setMap(null);
  }
}

function checkboxfunction3() {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox3");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    alternativeroutes();
  } else {
	  altline.setMap(null);
  }
}

function checkboxfunction4() {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox4");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    originalroute();
  } else {
	  newLine.setMap(null);
  }
}

function alternativeroutes()
{
				if(counter == myJson.index_max)
				{
					counter++;
				}
				
				if(counter == myJson.routePrint.length)
				{
				counter=0;
				}
					
				//console.log(counter);
				altline = new google.maps.Polyline({
				path: myJson.routePrint[counter],
				strokeColor: "#696969",
				strokeOpacity: .75,
				strokeWeight: 8,
				geodesic: true,
				map: map});	
				getSimilarity(removedRoute, myJson.routePrint[counter]);
				$("#probability").val(myJson.probability[counter]);
				counter++;
}


