// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', () => {

    // --- Splash Screen Logic ---
    const overlay = document.getElementById('overlay');
    if (overlay) {
        setTimeout(() => {
            overlay.classList.add('hidden');
        }, 2500);
    }

    // --- Modal Logic ---
    const getStartedBtn = document.getElementById('getStartedBtn');
    const loginModal = document.getElementById('loginModal');
    const closeBtn = document.getElementById('closeBtn');

    // Form sections and toggle links
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const showSignup = document.getElementById('showSignup');
    const showLogin = document.getElementById('showLogin');

    // Function to show the modal (and reset to login form)
    const showModal = () => {
        loginModal.classList.add('visible');
        // Always show the login form and hide the signup form by default
        loginForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
    };

    // Function to hide the modal
    const hideModal = () => {
        loginModal.classList.remove('visible');
    };

    // Show modal when "Get Started" is clicked
    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', (event) => {
            event.preventDefault(); // Stop link from navigating
            showModal();
        });
    }

    // Hide modal when the close 'X' button is clicked
    if (closeBtn) {
        closeBtn.addEventListener('click', hideModal);
    }
    
    // Hide modal when clicking on the background/backdrop
    if (loginModal) {
        loginModal.addEventListener('click', (event) => {
            if (event.target === loginModal) {
                hideModal();
            }
        });
    }

    // --- Form Toggling Logic ---
    
    // Switch to Sign Up form
    if (showSignup) {
        showSignup.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.classList.add('hidden');
            signupForm.classList.remove('hidden');
        });
    }

    // Switch back to Login form
    if (showLogin) {
        showLogin.addEventListener('click', (e) => {
            e.preventDefault();
            signupForm.classList.add('hidden');
            loginForm.classList.remove('hidden');
        });
    }
});