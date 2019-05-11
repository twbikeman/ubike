$("#update").on({
    click: function(){update()}
});

$("document").ready(function() {
    update();
});


function update() {

    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if(xhr.status == 200) {document.getElementById('content').innerHTML = xhr.responseText}
        else console.log('fail!')
    };
    xhr.open('GET','/queryUbike.html',true);
    xhr.send(null);
    

    var xhr2 = new XMLHttpRequest();
    xhr2.onload = function() {
        if(xhr2.status == 200) {
        var responseObject = JSON.parse(xhr2.responseText);
        var newContent = '';
        for (var i = 0; i < responseObject.events.length; i++) {
            newContent += responseObject.events[i].location + "<br>";
            }   
        }    
        document.getElementById('content2').innerHTML = newContent;
    };
    xhr2.open('GET','/data/data.json',true);
    xhr2.send(null);
}


