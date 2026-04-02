document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registerForm");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const email = document.getElementById("regEmail").value;
        const password = document.getElementById("regPassword").value;

        // Save user data to browser memory
        localStorage.setItem("userEmail", email);
        localStorage.setItem("userPassword", password);

        alert("Registration Successful ✅");

        // Redirect to login page
        window.location.href = "login.html";
    });
});