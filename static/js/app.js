document.addEventListener('DOMContentLoaded', function() {
    // Initialize floating labels
    document.querySelectorAll('.form-group').forEach(formGroup => {
        const input = formGroup.querySelector('input');
        const floatLabel = formGroup.querySelector('.float-label');

        if (!input || !floatLabel) return;

        // Initial check for pre-filled values
        if (input.value.trim() !== '') {
            floatLabel.classList.add('active');
        }

        // Focus/blur handlers
        input.addEventListener('focus', () => {
            floatLabel.classList.add('active');
        });

        input.addEventListener('blur', () => {
            if (input.value.trim() === '') {
                floatLabel.classList.remove('active');
            }
        });

        // Real-time input tracking
        input.addEventListener('input', () => {
            floatLabel.classList.toggle('active', input.value.trim() !== '');
        });
    });

    // Enhanced password toggle
    document.querySelectorAll('.password-toggle').forEach(toggle => {
        const input = toggle.closest('.password-wrapper')?.querySelector('input[type="password"], input[type="text"]');
        if (!input) return;

        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const isPassword = input.type === 'password';
            
            input.type = isPassword ? 'text' : 'password';
            this.classList.replace(isPassword ? 'fa-eye' : 'fa-eye-slash', 
                                 isPassword ? 'fa-eye-slash' : 'fa-eye');
            
            // Animation
            this.style.transform = 'translateY(-50%) scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'translateY(-50%)';
            }, 200);
        });
    });

    // Form submission handler
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                // Save original button content
                if (!submitBtn.dataset.originalHtml) {
                    submitBtn.dataset.originalHtml = submitBtn.innerHTML;
                }
                
                submitBtn.innerHTML = `
                    <span class="btn-loader"></span>
                    Processing...
                `;
                submitBtn.disabled = true;
                
                // Re-enable button if form submission fails
                window.setTimeout(() => {
                    submitBtn.innerHTML = submitBtn.dataset.originalHtml;
                    submitBtn.disabled = false;
                }, 5000);
            }
        });
    });

    // Auto-focus first invalid input
    const invalidInput = document.querySelector('.form-group input:invalid');
    if (invalidInput) {
        invalidInput.focus();
    }
});