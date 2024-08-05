/* songs/static/songs/js/scripts.js */

document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.card-container');
    let isDown = false;
    let startX;
    let scrollLeft;
    const audio = document.getElementById('audio-player');
    const nextButton = document.querySelector('.next-button');

    if (audio && nextButton) {
        audio.addEventListener('ended', function() {
            window.location.href = nextButton.href; // Redirect to the next song
        });
    }

    container.addEventListener('mousedown', (e) => {
        isDown = true;
        container.classList.add('active');
        startX = e.pageX - container.offsetLeft;
        scrollLeft = container.scrollLeft;
    });

    container.addEventListener('mouseleave', () => {
        isDown = false;
        container.classList.remove('active');
    });

    container.addEventListener('mouseup', () => {
        isDown = false;
        container.classList.remove('active');
    });

    container.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - container.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        container.scrollLeft = scrollLeft - walk;
    });
});