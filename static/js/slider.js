const slides = document.querySelectorAll('.slide');
const controls = document.querySelectorAll('.controlls');
let currentIndex = 0;
let interval;

// Функция показа слайда с анимацией
function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
}

// Функция смены слайда
function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

// Авто-переключение каждые 3 секунды
function startAutoSlide() {
    interval = setInterval(nextSlide, 7000);
}

// Остановка при клике
function stopAutoSlide() {
    clearInterval(interval);
}

// Обработчики кликов для кнопок
controls.forEach(control => {
    control.addEventListener('click', (event) => {
        stopAutoSlide();
        if (event.target.classList.contains('prev')) {
            currentIndex = currentIndex - 1 < 0 ? slides.length - 1 : currentIndex - 1;
        } else if (event.target.classList.contains('next')) {
            currentIndex = (currentIndex + 1) % slides.length;
        }
        showSlide(currentIndex);
        startAutoSlide();
    });
});

// Запуск слайдера
showSlide(currentIndex);
startAutoSlide();
