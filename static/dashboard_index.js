$("#update").on({
    click: function(){update()}
    
});

$("document").ready(function() {
    update();
    // $.ajaxSetup ({
    //     cache: false
    // });
});


function update() {

    // var xhr1 = new XMLHttpRequest();
    // xhr1.onload = function() {
    //     if(xhr1.status == 200) {
    //         document.getElementById('content1').innerHTML = xhr1.responseText;
    //         console.log(xhr.responseText);
    //     }
    //     else console.log('fail!')
    // };
    // xhr1.open('GET','/bar3.html',true);
    // xhr1.send(null);
    
    // $.ajaxSetup ({
    //     // Disable caching of AJAX responses
    //     cache: false
    // });


    $("#content1").load("/bar3.html");

    // $.get('/bar3.html', function(data){$('#content1').html(data)})

    $("#content2").load("/queryOneUbike.html");


    

    var xhr2 = new XMLHttpRequest();
    xhr2.onload = function() {
        if(xhr2.status == 200) {
        var responseObject = JSON.parse(xhr2.responseText);
        var newContent = '';
        for (var i = 0; i < responseObject.events.length; i++) {
            newContent += responseObject.events[i].location + "<br>";
            }   
        }    
        document.getElementById('content3').innerHTML = newContent;
    };
    xhr2.open('GET','/data/data.json',true);
    xhr2.send(null);


    
}


