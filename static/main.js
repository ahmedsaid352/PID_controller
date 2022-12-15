var i=1;
let id;

function refresh_chart(){
id =setInterval(show_pid, 500);
}

function show_pid(){
if (i==60){
clearInterval(id);
}
const chart = document.getElementById('result');
let mystr = 'url(\'../static/images/fig'+i+'.png\')';
chart.style.backgroundImage = mystr;
console.log(mystr);
i+=1;
}

window.addEventListener("load", (event) => {
  refresh_chart()
});


