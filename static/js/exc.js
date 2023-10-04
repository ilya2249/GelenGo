function rangeSlider(value){
    document.getElementById('rangeValue').innerHTML = value;
    document.getElementById('fillRangeValue').style.width = +value+"%";
    console.log(value);
}