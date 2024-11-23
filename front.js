document.getElementById('predictor-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const age = parseFloat(document.getElementById('age').value);
    const diabetic = parseFloat(document.getElementById('diabetic').value);
    const sugar_consumption = parseFloat(document.getElementById('sugar_consumption').value);

    const intercept = 0.25141231073159376;
    const ageCoef = 0.00233992;
    const diabeticCoef = 0.08285847;
    const sugarCoef = 0.00342582;

    const prediction = ageCoef * age + diabeticCoef * diabetic + sugarCoef * sugar_consumption + intercept;

    const resultDiv = document.getElementById('result');
    if(prediction < 0.500) {
        resultDiv.innerText = "This is preferable to the Diabetic people";
        resultDiv.style.color = 'green';
    } else {
        resultDiv.innerText = "This is not preferable to the Diabetic people";
        resultDiv.style.color = 'red';
    }
});