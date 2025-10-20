let hoverTimeout;
let isAnimating = false;

// Split text into characters
function initializeTitle() {
    const title = document.getElementById('title');
    const text = title.textContent;
    title.innerHTML = '';
    
    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const span = document.createElement('span');
        span.classList.add('char');
        span.textContent = char === ' ' ? '\u00A0' : char;
        title.appendChild(span);
        if(i == 9) {
            const br = document.createElement('br');
            title.appendChild(br);
        }
    }
}

document.getElementById('title').addEventListener('mouseenter', function() {
    if (isAnimating) return;
    
    hoverTimeout = setTimeout(() => {
        startEraserAnimation();
    }, 8000);
});

document.getElementById('title').addEventListener('mouseleave', function() {
    clearTimeout(hoverTimeout);
});

function startEraserAnimation() {
    if (isAnimating) return;
    isAnimating = true;
    
    const eraser = document.getElementById('eraser');
    const title = document.getElementById('title');
    const chars = title.querySelectorAll('.char');
    
    // Show eraser
    eraser.style.opacity = '1';
    eraser.style.transition = 'right 14s linear, top 0.3s';
    
    // Get title width
    const titleWidth = title.offsetWidth;
    
    // Move eraser from right to left
    eraser.style.right = (titleWidth + 1000) + 'px';
    
    // Animation timing
    const duration = 5200;
    const startTime = Date.now();
    const charDelay = duration / chars.length;
    
    function animate() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Create wiggle effect
        const wiggle = Math.sin(elapsed * 0.02) * 380;
        eraser.style.top = `calc(50% + ${wiggle}px)`;
        
        // Calculate current character being erased (from right to left)
        const currentCharIndex = chars.length - 1 - Math.floor(progress * chars.length);
        
        chars.forEach((char, index) => {
            if (index > currentCharIndex) {
                // Fully erased (right side characters)
                char.style.clipPath = 'ellipse(50% 30% at 50% 130%)';
            } else if (index === currentCharIndex) {
                // Currently being erased
                const charProgress = (elapsed - ((chars.length - 1 - index) * charDelay)) / charDelay;
                if (charProgress >= 0) {
                    const ellipseProgress = Math.min(Math.max(charProgress, 0), 1);
                    const yPosition = 80 + (ellipseProgress * 50); // Move from 70% to 120%
                    char.style.clipPath = `ellipse(50% 30% at 50% ${yPosition}%)`;
                }
            } else {
                // Not yet erased
                char.style.clipPath = 'ellipse(50% 100% at 50% 40%)';
            }
        });
        
        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
                setTimeout(() => {
                    eraser.style.opacity = '0.5';
                    eraser.style.transition = 'opacity 1s ease-out';
                    isAnimating = false;
                }, 300);
            }
    }
    animate();
}
initializeTitle();
