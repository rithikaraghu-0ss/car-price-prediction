document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');
    const predictedPrice = document.getElementById('predicted-price');
    const resetBtn = document.getElementById('reset-btn');
    const predictBtn = document.getElementById('predict-btn');
    const loader = document.getElementById('btn-loader');
    const btnText = predictBtn.querySelector('span');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Show loading state
        btnText.style.opacity = '0.5';
        loader.style.display = 'block';
        predictBtn.disabled = true;

        const formData = new FormData(form);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.prediction) {
                predictedPrice.textContent = data.prediction;
                resultContainer.style.display = 'flex';
                resultContainer.style.animation = 'fadeIn 0.5s ease forwards';
            } else {
                alert('Error: ' + (data.error || 'Something went wrong'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        } finally {
            // Reset button state
            btnText.style.opacity = '1';
            loader.style.display = 'none';
            predictBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        resultContainer.style.display = 'none';
        form.reset();
    });
});
