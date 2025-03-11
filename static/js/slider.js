const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const sliderText = document.getElementById('slider-text');
const tourButtons = document.querySelectorAll('.tour-button');
let index = 0;

const texts = [
    "Откройте для себя новые горизонты",
    "Лучшие направления для отдыха",
    "Незабываемые впечатления ждут вас",
    "Путешествуйте с комфортом",
    "Природа, которую стоит увидеть"
];

function showSlide(i) {
    slider.style.transition = "transform 1s ease-in-out";
    slider.style.transform = `translateX(-${i * 100}%)`;
    sliderText.textContent = texts[i];
}

function nextSlide() {
    index = (index + 1) % slides.length;
    showSlide(index);
}

prev.addEventListener('click', () => {
    index = (index === 0) ? slides.length - 1 : index - 1;
    showSlide(index);
});

next.addEventListener('click', () => {
    nextSlide();
});

// Автоматическая смена слайдов каждые 5 секунд
setInterval(() => {
    nextSlide();
}, 5000);

// Стилизация кнопок "Просмотреть туры" при наведении
tourButtons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.background = "#e65b50";
        button.style.transform = "scale(1.1)";
    });
    button.addEventListener('mouseleave', () => {
        button.style.background = "#ff6f61";
        button.style.transform = "scale(1)";
    });
});