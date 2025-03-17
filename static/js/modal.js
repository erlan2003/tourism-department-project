// Получаем элементы
const modal = document.getElementById("modal");
const openModalBtn = document.getElementById("openModal");
const closeModalBtn = document.querySelector(".close");

// Открытие модального окна
openModalBtn.onclick = function() {
    modal.style.display = "block";
}

// Закрытие модального окна
closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

// Закрытие модального окна при клике вне области окна
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Получаем элементы формы
const form = document.getElementById('contactForm');
const responseMessage = document.getElementById('responseMessage');

// Получаем CSRF токен
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

form.onsubmit = function(event) {
    event.preventDefault();

    const formData = new FormData(form);

    fetch(sendMessageUrl, {  // Используем переданный URL
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,  // CSRF токен
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        responseMessage.textContent = data.message;
        form.reset();
        setTimeout(() => {
            modal.style.display = "none";  // Закрытие модального окна через 3 секунды
        }, 3000);
    })
    .catch(error => {
        console.error("Ошибка при отправке:", error);
        responseMessage.textContent = "Произошла ошибка. Попробуйте еще раз.";
    });
};
