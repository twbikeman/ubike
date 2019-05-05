var dataset = {};

// d3.json("{{ url_for('static',filename='test.json') }}").then(function(d){ console.log(d); dataset = d;});
// -------------------
function draw(dataset) {
    console.log(dataset);
// var dataset = {a:1,b:2,c:3,d:1,e:2,f:3,g:1,h:2,i:3};
var color = d3.scaleOrdinal(d3.schemeCategory10); 
var pie = d3.pie().value(function(d){return d.value})
var mypie = pie(d3.entries(dataset));
var w = 300, h =300;
var outerRadius = w / 2;
var innerRadius = 0;
var arc = d3.arc()
            .innerRadius(innerRadius)
            .outerRadius(outerRadius);
var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h)
var arcs = svg.selectAll("g.arc")
                .data(mypie)
                .enter()
                .append("g")
                .attr("transform","translate(" + outerRadius + "," + outerRadius + ")");
arcs.append("path")
    .attr("fill", function(d, i){return color(i);})
    .attr("d", arc);
arcs.append("text")
    .attr("transform", function(d) {return "translate(" + arc.centroid(d) +")"})
    .attr("text-anchor","middle")
    .text(function(d){return d.data.key + ' ' + d.data.value;});
}

$.ajax({
    cache: false,
    success: function(data) {
        draw(data);
        },
    url: "{{ url_for('static', filename = 'test.json') }}"
});
