document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("loginBtn").addEventListener("click", function () {
        event.preventDefault(); 
        console.log("Login Button Clicked")
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
    
        const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    
        fetch("/login-view/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect to dashboard on success
                window.location.href = data.redirect_url;
            } else {
                alert(data.message || "Invalid credentials");
            }
        });
    });
    
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});