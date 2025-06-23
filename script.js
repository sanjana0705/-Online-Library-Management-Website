
// Get modal elements
/*
var loginModal = document.getElementById("loginModal");
var signupModal = document.getElementById("signupModal");
var adminLoginModal = document.getElementById("adminLoginModal"); // Admin login modal

// Get button elements
var loginBtn = document.getElementById("loginBtn");
var signupBtn = document.getElementById("signupBtn");
var adminLoginBtn = document.getElementById("adminLoginBtn"); // Admin login button

// Get close buttons
var closeButtons = document.getElementsByClassName("close");

// Show login modal when clicking "Login"
loginBtn.onclick = function() {
    loginModal.style.display = "flex";
}

// Show signup modal when clicking "Sign Up"
signupBtn.onclick = function() {
    signupModal.style.display = "flex";
}

// Show admin login modal when clicking "Admin Login"
adminLoginBtn.onclick = function() {
    adminLoginModal.style.display = "flex";
}

// Close modal when clicking on the close (X) button
for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].onclick = function(event) {
        event.target.parentElement.parentElement.style.display = "none";
    }
}

// Close modal when clicking outside the modal content
window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    }
    if (event.target == signupModal) {
        signupModal.style.display = "none";
    }
    if (event.target == adminLoginModal) { // Close admin modal if clicked outside
        adminLoginModal.style.display = "none";
    }
}
    */
// Get modal elements
/*
var loginModal = document.getElementById("loginModal");
var signupModal = document.getElementById("signupModal");
var adminLoginModal = document.getElementById("adminLoginModal"); // Get admin modal

// Get button elements
var loginBtn = document.getElementById("loginBtn");
var signupBtn = document.getElementById("signupBtn");
var adminLoginBtn = document.getElementById("adminLoginBtn"); // Get admin login button

// Get close buttons
var closeButtons = document.getElementsByClassName("close");

// Show login modal when clicking "Login"
loginBtn.onclick = function() {
    loginModal.style.display = "flex";
}

// Show signup modal when clicking "Sign Up"
signupBtn.onclick = function() {
    signupModal.style.display = "flex";
}

// Show admin login modal when clicking "Admin Login"
adminLoginBtn.onclick = function() {
    adminLoginModal.style.display = "flex";
}

// Close modal when clicking on the close (X) button
for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].onclick = function(event) {
        event.target.parentElement.parentElement.style.display = "none";
    }
}

// Close modal when clicking outside the modal content
window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    }
    if (event.target == signupModal) {
        signupModal.style.display = "none";
    }
    if (event.target == adminLoginModal) { // Close admin modal if clicked outside
        adminLoginModal.style.display = "none";
    }
};

document.addEventListener("DOMContentLoaded", function () {
    const loginBtn = document.getElementById("loginBtn");
    const signupBtn = document.getElementById("signupBtn");
    const adminLoginBtn = document.getElementById("adminLoginBtn");

    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const adminLoginForm = document.getElementById("adminLoginForm");

    // Function to hide all forms
    function hideAllForms() {
        loginForm.style.display = "none";
        signupForm.style.display = "none";
        adminLoginForm.style.display = "none";
    }

    // Event listeners for buttons
    loginBtn.addEventListener("click", function () {
        hideAllForms();
        loginForm.style.display = "block";
    });

    signupBtn.addEventListener("click", function () {
        hideAllForms();
        signupForm.style.display = "block";
    });

    adminLoginBtn.addEventListener("click", function () {
        hideAllForms();
        adminLoginForm.style.display = "block";
    });
});
*/
document.addEventListener("DOMContentLoaded", function () {
    // Get modal elements
    let loginModal = document.getElementById("loginModal");
    let signupModal = document.getElementById("signupModal");
    let adminLoginModal = document.getElementById("adminLoginModal");

    // Get button elements
    let loginBtn = document.getElementById("loginBtn");
    let signupBtn = document.getElementById("signupBtn");
    let adminLoginBtn = document.getElementById("adminLoginBtn");

    // Get close buttons
    let closeButtons = document.getElementsByClassName("close");

    // Show modals when buttons are clicked
    loginBtn.onclick = function () {
        loginModal.style.display = "block";
    };
    signupBtn.onclick = function () {
        signupModal.style.display = "block";
    };
    adminLoginBtn.onclick = function () {
        adminLoginModal.style.display = "block";
    };

    // Close modals when 'x' is clicked
    for (let btn of closeButtons) {
        btn.onclick = function () {
            loginModal.style.display = "none";
            signupModal.style.display = "none";
            adminLoginModal.style.display = "none";
        };
    }

    // Close modals when clicking outside the modal
    window.onclick = function (event) {
        if (event.target == loginModal) loginModal.style.display = "none";
        if (event.target == signupModal) signupModal.style.display = "none";
        if (event.target == adminLoginModal) adminLoginModal.style.display = "none";
    };
});


