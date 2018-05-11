Hi, really nice job. You can all consider having passed the course with grade one. Now, to get it up to 5, here are some comments:

//1. Add a progress indicator when pressing predict. Things will happen which take time (google request, your grid processing). User needs to know something is happening.

2. Too many colors. In the beginning, route can be thick and black. The middle part (that you select to be removed) should become invisible. The end points of the missing region could be green - red dots. Something like here:

The alternatives can be gray and the best alternative (Only) can be highlighted in some color (blue or green).

3. Make modes for testing. There can be checkboxes for each.
Now you should have about 4 already!
//A. Straight line interpolation
//B. Google directions
B.1. Shortest path
//B.2. Fastest path? (check which you are using right now)
//B.3. Include alternatives

All results: straight line, shortest, fastest and any google alternatives should be shown in gray (see above) and scored! You may add more like:
C. OSRM
D. Use movement type
E. Estimate missing travel distance and get alternative matching that
F. Use weather data
G. Use time of day type of information, etc...
These can be selected before pressing Predict.

//4. Compute 'Typicality' for the missing segment. Is the removed segment itself scoring high? Add it to the list of alternatives in 3.

//5. Code for the similarity API call using POST. The getPostAsync function you take from our demo on multiple APIs:
var url='https://cs.uef.fi/mopsi/routes/similarityApi/index.php';
var r1=[{lat:62.6067,lng:29.76060},{lat:62.6057,lng:29.76060},{lat:62.6057,lng:29.76160}];
var r2=[{lat:62.6067,lng:29.76060},{lat:62.6057,lng:29.76060},{lat:62.6057,lng:29.75960}];
var param={
  measure:"C-SIM",
  A:r1,
  B:r2,
  threshold:25
}
var dataString="param="+JSON.stringify(param);
httpPostAsync(url,dataString,function(res){console.log(res)})

//6. Try displaying the cells on the map, at least for the alternatives, but would be useful to see them inside a query region. Then we can know if the way we generate alternative would need work.

7. Make the testing in bulk function.