function decodeGeneratedString() {
    const tableCell = document.querySelector('table tbody tr td:nth-child(2)');
    const responseBody = tableCell.innerHTML;

    const generatedStringMatch = responseBody.match(/Generated String:\s*([^<]+)<br>/);
    const shiftMatch = responseBody.match(/Shift:\s*(-?\d+)/);

    if (!generatedStringMatch || !shiftMatch) {
        return;
    }

    const generatedString = generatedStringMatch[1].trim();
    const shift = parseInt(shiftMatch[1], 10);
    const generatedNumbers = generatedString.match(/(\d+)/g).map(Number).filter(num => !isNaN(num));

    if (generatedNumbers.length === 0 || isNaN(shift)) {
        return;
    }

    const shiftedNumbers = generatedNumbers.map(number => number - shift);
    const decodedASCII = shiftedNumbers.map(num => String.fromCharCode(num)).join('');

    document.querySelector('input[name="solution"]').value = decodedASCII;
    document.querySelector('input[name="submitbutton"]').click();
}

decodeGeneratedString();

// Author TGrozdanovski