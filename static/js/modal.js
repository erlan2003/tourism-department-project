document.addEventListener("DOMContentLoaded", function () {
    console.log("Скрипт загружен!");

    const modal = document.getElementById("modal");
    const closeModalBtn = document.querySelector(".close");
    const openModalBtns = document.querySelectorAll(".openModal");

    // Проверяем, есть ли модальное окно и кнопки
    if (!modal || openModalBtns.length === 0) {
        console.warn("❌ Модальное окно или кнопки открытия не найдены!");
        return;
    }

    // Гарантируем, что модальное окно закрыто при загрузке
    modal.style.display = "none";

    // Добавляем обработчик на каждую кнопку
    openModalBtns.forEach(btn => {
        btn.addEventListener("click", function () {
            console.log("Кнопка нажата:", btn);
            modal.style.display = "block";
        });
    });

    // Закрытие окна
    closeModalBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Закрытие при клике вне окна
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    // Форма отправки
    const form = document.getElementById("contactForm");
    const responseMessage = document.getElementById("responseMessage");

    if (!form) {
        console.error("❌ Форма не найдена!");
        return;
    }

    // CSRF токен (ждём, пока страница загрузится)
    const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    const csrfToken = csrfTokenElement ? csrfTokenElement.value : "";

    form.onsubmit = function (event) {
        event.preventDefault();
        
        const formData = new FormData(form);

        fetch(sendMessageUrl, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            responseMessage.textContent = data.message;
            form.reset();
            setTimeout(() => {
                modal.style.display = "none";
            }, 3000);
        })
        .catch(error => {
            console.error("Ошибка при отправке:", error);
            responseMessage.textContent = "Произошла ошибка. Попробуйте еще раз.";
        });
    };
});
