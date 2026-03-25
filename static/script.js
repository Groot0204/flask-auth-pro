const container = document.getElementById('container');

const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

const mobileRegister = document.getElementById('mobile-register');
const mobileLogin = document.getElementById('mobile-login');

if (registerBtn) {
    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });
}

if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });
}

/* Mobile toggle */
if (mobileRegister) {
    mobileRegister.addEventListener('click', (e) => {
        e.preventDefault();
        container.classList.add("active");
    });
}

if (mobileLogin) {
    mobileLogin.addEventListener('click', (e) => {
        e.preventDefault();
        container.classList.remove("active");
    });
}

document.querySelectorAll('.flash-container').forEach(flash => {
    setTimeout(() => {
        flash.style.opacity = '0';
        setTimeout(() => flash.remove(), 500);
    }, 3000);
})

document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", () => {

        const btn = form.querySelector("button[type='submit']");

        if (btn) {
            btn.innerText = "Please wait...";

            // disable AFTER small delay so submit still works
            setTimeout(() => {
                btn.disabled = true;
            }, 100);
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {

    function checkStrength(password) {
        let strength = 0;

        if (password.length >= 8) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[!@#$%^&*]/.test(password)) strength++;

        return strength;
    }

    function updateStrength(inputId, barId, textId) {
        const input = document.getElementById(inputId);
        const bar = document.getElementById(barId);
        const text = document.getElementById(textId);

        if (!input || !bar || !text) return;

        input.addEventListener("input", () => {
            const val = input.value;
            const strength = checkStrength(val);

            let width = (strength / 5) * 100;
            bar.style.width = width + "%";

            if (strength <= 2) {
                bar.style.background = "#ff4b2b";
                text.innerText = "Weak";
            } else if (strength <= 4) {
                bar.style.background = "#f1c40f";
                text.innerText = "Medium";
            } else {
                bar.style.background = "#2ecc71";
                text.innerText = "Strong";
            }
        });
    }

    updateStrength("signup-password", "signup-strength-bar", "signup-strength-text");
    updateStrength("reset-password", "reset-strength-bar", "reset-strength-text");

});

console.log("Script loaded successfully!");