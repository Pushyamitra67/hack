document.addEventListener('DOMContentLoaded', () => {

    // --- Get all the elements we need to animate ---
    const overlay = document.getElementById('overlay');
    const navbar = document.querySelector('.navbar');
    const content = document.querySelector('.content');
    const loginModal = document.getElementById('loginModal');
    const getStartedBtn = document.getElementById('getStartedBtn');
    const closeBtn = document.getElementById('closeBtn');

    // --- 1. Entry Animation Sequence ---
    if (overlay && navbar && content) {
        // After 2.5 seconds...
        setTimeout(() => {
            // Hide the splash screen
            overlay.classList.add('hidden');

            // Add the 'visible' class to trigger the animations
            // for the navbar and the main content.
            navbar.classList.add('visible');
            content.classList.add('visible');
        }, 2500); // 2.5 second delay
    }

    // --- 2. Login Modal Logic (no changes needed here) ---
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const showSignup = document.getElementById('showSignup');
    const showLogin = document.getElementById('showLogin');

    const showModal = () => loginModal.classList.add('visible');
    const hideModal = () => loginModal.classList.remove('visible');

    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', (event) => {
            event.preventDefault();
            showModal();
        });
    }
    if (closeBtn) {
        closeBtn.addEventListener('click', hideModal);
    }
    if (loginModal) {
        loginModal.addEventListener('click', (event) => {
            if (event.target === loginModal) {
                hideModal();
            }
        });
    }
    if (showSignup) {
        showSignup.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.classList.add('hidden');
            signupForm.classList.remove('hidden');
        });
    }
    if (showLogin) {
        showLogin.addEventListener('click', (e) => {
            e.preventDefault();
            signupForm.classList.add('hidden');
            loginForm.classList.remove('hidden');
        });
    }
});