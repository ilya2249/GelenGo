const slider = document.querySelector('.boxesFacts');
let indexSlider = 0;
const box_next = document.querySelector(".box-next");
const box_previous = document.querySelector(".box-previous");
const slide = Array.from(slider.querySelectorAll('.box'));
const slideCount = slide.length;

box_previous.addEventListener('click', showPreviousSlide);
box_next.addEventListener('click', showNextSlide);
function showPreviousSlide() {
   indexSlider = (indexSlider - 1 + slideCount) % slideCount;
   updateSlider();
}
function showNextSlide() {
   indexSlider = (indexSlider + 1 + slideCount) % slideCount;
   updateSlider();
}
function updateSlider() {
   slide.forEach((slide, index) => {

   
      if (indexSlider==index){
         slide.style.display = "block";
      }
      else {
         slide.style.display = "none";
      }
   });}

updateSlider()