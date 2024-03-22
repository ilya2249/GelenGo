let list = document.getElementById('list2');
let input = document.getElementsByClassName('search-input');
list.classList.add('hide');
document.querySelector('#elastic').oninput = function () {

    list.classList.remove('hide');

    let val = this.value.trim();
    if (val != "") {
        elasticItems = document.querySelectorAll('.elastic li')
        elasticItems.forEach(function (elem) {
            if (elem.innerText.search(val) == -1) {
                elem.classList.add('hide');
            } else {
                elem.classList.remove('hide');
            }
        });
    } else {
        elasticItems.forEach(function (elem) {
            elem.classList.remove('hide');
            // elem.innerHTML = elem.innerText;
            list.classList.add('hide');
        })
    };
}


//     function markLetter(string, pos, len) {

//         return  string.slice(0, pos) + '<mark>' + string.slice(pos, pos + len) + '</mark>' + string.slice(pos + len);
//     }
// 
function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('show');
        } else {
            change.target.classList.remove('show');
        }
    });
}
let options = {
    threshold: [0.3]
};
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.second_page');
for (let elm of elements) {
    observer.observe(elm);
}
const changer = document.getElementById("toggle_checkbox");
let videoD = document.getElementById('day');
let videoN = document.getElementById('night');
let search = document.getElementById('elastic');
let mt = document.getElementById('mt');
let gl = document.getElementById('gl');
let c2 = document.getElementById('c2');
let cn = document.getElementById('cn');
let line = document.querySelectorAll('nav > ul > li > a');
let colorTextHover = document.querySelectorAll('nav > ul > li');
let border = document.querySelectorAll('.container-not-image');
let list3 = document.querySelectorAll('nav > ul > li > ul > li > .list3');
let list4 = document.querySelectorAll('nav > ul > li > ul');
changer.addEventListener("click", function () {
    videoD.classList.toggle('hide');
    document.body.classList.toggle('dark-theme');
    videoN.classList.toggle('hide');
    search.classList.toggle('hide');
    mt.classList.toggle('hide');
    gl.classList.toggle('hide');
    document.body.classList.toggle('dark-back-color');
    c2.classList.toggle('hide');
    cn.classList.toggle('hide');
    border.forEach(function (elem) {
        elem.classList.toggle('hide');
    });
    line.forEach(function (elem) {
        elem.classList.toggle('hide');
    });
    list3.forEach(function(elem) {
        elem.classList.toggle('hide');
    })
    list4.forEach(function(elem) {
        elem.classList.toggle('hide');
    })
});
