// Simple JavaScript for interactivity

document.addEventListener('DOMContentLoaded', function() {
    console.log('Java Web Application loaded!');
    
    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Form validation
    const form = document.querySelector('.form');
    if (form) {
        const input = form.querySelector('input[name="message"]');
        if (input) {
            input.addEventListener('focus', function() {
                this.style.borderColor = '#667eea';
            });
            
            input.addEventListener('blur', function() {
                this.style.borderColor = '#e0e0e0';
            });
        }
    }

    // Log page load time
    window.addEventListener('load', function() {
        const loadTime = performance.now();
        console.log('Page fully loaded in ' + loadTime.toFixed(2) + 'ms');
    });
});
