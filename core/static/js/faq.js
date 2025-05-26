const buttons = document.querySelectorAll('.question button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const answer = button.nextElementSibling;
        const icon = button.querySelector('.d-arrow');

        // Lukk alle andre åpne først
        document.querySelectorAll('.question p.show').forEach(p => {
            if (p !== answer) {
                p.classList.remove('show');
                p.style.maxHeight = null;
                const otherIcon = p.previousElementSibling.querySelector('.d-arrow');
                if (otherIcon) {
                    otherIcon.classList.remove('rotate');
                }
            }
        });

        // Toggle valgt
        answer.classList.toggle('show');
        icon.classList.toggle('rotate');
    });
});
