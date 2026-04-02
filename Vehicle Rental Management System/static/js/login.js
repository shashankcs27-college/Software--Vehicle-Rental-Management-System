document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("loginForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // 1. Capture inputs
        const emailInput = document.querySelector("input[type='email']").value;
        const passwordInput = document.querySelector("input[type='password']").value;

        // 2. Get registered data from storage
        const registeredEmail = localStorage.getItem("userEmail");
        const registeredPassword = localStorage.getItem("userPassword");

        // 3. ADMIN CHECK
        if (emailInput === "admin@gmail.com" && passwordInput === "123") {
            localStorage.setItem("currentUserRole", "admin"); // Save role for later
            alert("Admin Login Successful ✅");
            
            // Redirect to a specific Admin Page
            window.location.href = "admin-dashboard.html"; 
        } 
        
        // 4. NORMAL USER CHECK
        else if (emailInput === registeredEmail && passwordInput === registeredPassword) {
            localStorage.setItem("currentUserRole", "user"); // Save role for later
            alert("User Login Successful ✅");
            
            // Redirect to the regular Home Page
            window.location.href = "index.html"; 
        } 
        
        // 5. ERROR HANDLING
        else {
            alert("Invalid Email or Password ❌");
        }
    });
});