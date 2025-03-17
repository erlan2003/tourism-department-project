const slides = document.querySelectorAll('.slide');
const controls = document.querySelectorAll('.controlls');
let currentIndex = 0;
let interval;
let scrollPosition = 0;

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = currentIndex - 1 < 0 ? slides.length - 1 : currentIndex - 1;
    showSlide(currentIndex);
}

function startAutoSlide() {
    interval = setInterval(nextSlide, 7000);
}

function stopAutoSlide() {
    clearInterval(interval);
}

function handleScroll(event) {
    if (window.scrollY > scrollPosition) {
        // Прокрутка вниз - следующий слайд
        nextSlide();
    } else {
        // Прокрутка вверх - предыдущий слайд
        prevSlide();
    }
    scrollPosition = window.scrollY; // Обновляем позицию прокрутки
}

// Обработчик прокрутки
window.addEventListener('scroll', handleScroll);

controls.forEach(control => {
    control.addEventListener('click', (event) => {
        stopAutoSlide();
        if (event.target.classList.contains('prev')) {
            prevSlide();
        } else if (event.target.classList.contains('next')) {
            nextSlide();
        }
        startAutoSlide();
    });
});

showSlide(currentIndex);
startAutoSlide();
