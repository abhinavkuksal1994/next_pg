document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Intersection Observer for scroll animations
    const fadeElements = document.querySelectorAll('.fade-in-up');
    
    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    fadeElements.forEach(element => {
        appearOnScroll.observe(element);
    });

    // Hero Slider
    const slides = document.querySelectorAll('.hero-slider .slide');
    let currentSlide = 0;
    let slideInterval;

    const nextSlide = () => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    };

    const prevSlide = () => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        slides[currentSlide].classList.add('active');
    };

    if (slides.length > 0) {
        slideInterval = setInterval(nextSlide, 4000); // Change slide every 4 seconds
        
        // Touch support for swiping
        const heroSlider = document.querySelector('.hero');
        let touchStartX = 0;
        let touchEndX = 0;
        
        heroSlider.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        }, {passive: true});
        
        heroSlider.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, {passive: true});
        
        const handleSwipe = () => {
            const threshold = 50;
            if (touchEndX < touchStartX - threshold) {
                // Swiped left
                clearInterval(slideInterval);
                nextSlide();
                slideInterval = setInterval(nextSlide, 4000);
            }
            if (touchEndX > touchStartX + threshold) {
                // Swiped right
                clearInterval(slideInterval);
                prevSlide();
                slideInterval = setInterval(nextSlide, 4000);
            }
        };
    }
});
