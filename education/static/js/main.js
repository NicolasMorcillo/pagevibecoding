/**
 * main.js - Proyecto Educativo sobre IA
 * Implementación de efectos interactivos avanzados y revelación de contenido.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Inicializar la animación de descubrimiento en el scroll
    initScrollReveal();
});

/**
 * Utiliza la API de IntersectionObserver para observar elementos con la clase
 * '.scroll-reveal' e inyectar la clase '.visible' cuando entran en pantalla,
 * generando un efecto suave de descubrimiento o fade-in.
 */
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.scroll-reveal');
    
    if (revealElements.length === 0) return;

    // Configuración del Observer: 
    // Se activa cuando al menos el 10% del elemento es visible en el viewport
    // El margen inferior (-80px) asegura que el elemento tenga que subir un poco
    // antes de revelarse, acentuando el efecto de descubrimiento.
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -80px 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Agregar la clase de CSS que acciona la transición
                entry.target.classList.add('visible');
                
                // Dejar de observar el elemento una vez que se ha revelado
                // para mantenerlo fijo en pantalla y optimizar el rendimiento.
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Adjuntar todos los elementos seleccionados al observador
    revealElements.forEach(element => {
        observer.observe(element);
    });
}
