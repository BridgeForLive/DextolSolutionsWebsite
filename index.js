function createStar() {
    const star = document.createElement('div');
    star.className = 'star';

    const size = Math.random() * 2 + 1;
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;

    star.style.top = `${Math.random() * 100}%`;
    star.style.left = `${Math.random() * 100}%`;
    star.style.animationDuration = `${Math.random() * 5 + 5}s`;
    document.body.appendChild(star);
    setTimeout(() => {
        star.remove();
    }, 10000); // Adjust to match the animation duration
}


setInterval(createStar, 50);
