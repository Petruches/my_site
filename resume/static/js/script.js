var d = new Date();
var n = d.toLocaleTimeString();

//console.log(n)

function time() {
    let clock = document.getElementById('clock');
    setInterval(function() {
        let dt = new Date();
        clock.innerText = dt.toLocaleTimeString();
    }, 1000)
};
time()
