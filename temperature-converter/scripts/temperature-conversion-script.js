const inputs = document.getElementsByClassName('inputs');
const farenheitValue = document.getElementById('farenheit');
const celciusValue = document.getElementById('celsius');

for (let i = 0; i < inputs.length; i++) {
  let input = inputs[i];

  input.addEventListener('input', function (e) {
    let value = parseFloat(e.target.value);

    switch (e.target.name) {
      case 'farenheit':
        celciusValue.value = farenheitToCelsius(value);
        break;
        
      case 'celsius':
        farenheitValue.value = celsiusToFarenheit(value);
        break;
    }
  });
}

celsiusToFarenheit = (celsius) => Math.round((celsius * 9 / 5 + 32) * 100) / 100;
farenheitToCelsius = (farenheit) => Math.round(((5 / 9) * (farenheit - 32)) * 100) / 100;
// Rounded the results for this task, although I understand similar programs would not do this for precision's sake.