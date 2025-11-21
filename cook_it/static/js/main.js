let slides = [];
let slideIndex = 0;
let intervalId = null;

document.addEventListener("DOMContentLoaded", () => {
    slides = document.querySelectorAll(".slides img");
    initializeSlider();
});

function initializeSlider() {
    if (slides.length > 0) {
        slides[slideIndex].classList.add("displaySlide");
        intervalId = setInterval(nextSlide, 5000);
    }
}

function showSlide(index) {
    slideIndex = (index + slides.length) % slides.length; // wrap around
    slides.forEach(slide => slide.classList.remove("displaySlide"));
    slides[slideIndex].classList.add("displaySlide");
}

function restartInterval() {
    clearInterval(intervalId);
    intervalId = setInterval(nextSlide, 5000);
}

function prevSlide() {
    slideIndex--;
    showSlide(slideIndex);
    restartInterval();
}

function nextSlide() {
    slideIndex++;
    showSlide(slideIndex);
    restartInterval();
}
