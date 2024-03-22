const circles = document.querySelectorAll('.category-btn.a');

circles.forEach(circle => {
    circle.addEventListener('click', () => {
        circles.forEach(otherCircle => {
            otherCircle.classList.remove('selected');
        });
        circle.classList.add('selected');
    });
});



const circles_c = document.querySelectorAll('.category-btn.c');

circles_c.forEach(circle => {
    circle.addEventListener('click', () => {
        circles_c.forEach(otherCircle => {
            otherCircle.classList.remove('selected');
        });
        circle.classList.add('selected');
    });
});
const circles_d = document.querySelectorAll('.category-btn.d');
circles_d.forEach(circle => {
    circle.addEventListener('click', () => {
        circles_d.forEach(otherCircle => {
            otherCircle.classList.remove('selected');
        });
        circle.classList.add('selected');
    });
});

let list1 = document.getElementById('list1');
list1.classList.add('hide');

let list3 = document.getElementById('list3');
list3.classList.add('hide');
let list4 = document.getElementById('list4');
list4.classList.add('hide');

let circle = document.getElementById('button');

let background = document.getElementById('back');
let margin = document.getElementById('margin');
let caret1 = document.getElementById('caret_a');

let caret3 = document.getElementById('caret_c');
let caret4 = document.getElementById('caret_d');

document.querySelector('.text1').onclick = function () {
    list1.classList.toggle('hide');


    background.classList.add('hide');
    caret1.classList.toggle('hide');
    if (list1.classList.contains('hide')&& list3.classList.contains('hide')&& list4.classList.contains('hide')) {
        background.classList.remove('hide');

    }
}




document.querySelector('.text3').onclick = function () {

    list3.classList.toggle('hide');
    caret3.classList.toggle('hide');
    background.classList.add('hide');
    if (list1.classList.contains('hide') && list3.classList.contains('hide')&& list4.classList.contains('hide')) {
        background.classList.remove('hide');
    }
}

document.querySelector('.text4').onclick = function () {

    list4.classList.toggle('hide');
    caret4.classList.toggle('hide');
    background.classList.add('hide');
    if (list1.classList.contains('hide') && list3.classList.contains('hide')&& list4.classList.contains('hide')){
        background.classList.remove('hide');
    }
}

const curentFilters = {
    type: "all",
    location: "all",
    date: "all"
};
const filterBox = document.querySelectorAll('.box');
const categoryButtons = document.querySelectorAll(".category-btn");
for (const btn of categoryButtons) {
    btn.addEventListener('click', event => {
        if (event.target.tagName !== 'SPAN') return;
        let filterClass = event.target.dataset.category;
        const filterType = event.target.parentNode.parentNode.parentNode.dataset.category;
        curentFilters[filterType] = filterClass;
        console.log(curentFilters);

        filterBox.forEach(elem => {

            elem.classList.remove('filter');
            //Если элемент не содержит тип type.//Если элемент не содержит тип location.//Если элемент не содержит тип category
            if (!((elem.classList.contains(curentFilters.type) || curentFilters.type ===
                        'all') &&
                    (elem.classList.contains(curentFilters.location) || curentFilters
                        .location === 'all') &&
                    (elem.classList.contains(curentFilters.date) || curentFilters
                        .date === 'all'))) {

                elem.classList.add('filter');
            }
        });

    });

}

let target = document.getElementById('place_screen');


document.querySelector('#white_house').onclick = function () {
    target.classList.toggle('hide');

}