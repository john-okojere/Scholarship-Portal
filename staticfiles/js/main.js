// main.js

document.addEventListener("DOMContentLoaded", function () {
    // Bootstrap's built-in JS for handling navbar collapse
    const navbarToggle = document.querySelector('.navbar-toggler');
    if (navbarToggle) {
        navbarToggle.addEventListener('click', function () {
            const navbarCollapse = document.querySelector('.navbar-collapse');
            navbarCollapse.classList.toggle('show');
        });
    }

    // Smooth scroll to sections using Bootstrap (scrollspy)
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Adjust according to the Bootstrap fixed header height
                    behavior: 'smooth'
                });
            }
        });
    });

    // Bootstrap form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Example to toggle visibility using Bootstrap classes
    const toggleButton = document.getElementById('toggle-more-info');
    const moreInfo = document.getElementById('more-info');

    if (toggleButton && moreInfo) {
        toggleButton.addEventListener('click', function () {
            moreInfo.classList.toggle('d-none');
        });
    }
});

// AJAX Example (for dynamic loading or form submission)
function sendAjaxRequest(url, method, data, callback) {
    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Django-specific CSRF token handling
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => callback(data))
    .catch(error => console.error('Error:', error));
}

// CSRF Token Helper for Django (Django-specific)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
