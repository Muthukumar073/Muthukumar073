function calculateMaturityAmount() {
    const principle= parseFloat(document.getElementById("principle").value);
    const interest=parseFloat(document.getElementById("interest").value);
    const tenure=parseFloat(document.getElementById("tenure").value);

    const maturityAmount = principle + (principle * interest * tenure)/100;

    document.getElementById('result').innerText = `Maturity Amount: ${maturityAmount.toFixed(2)}`;



}
document.getElementById('calculate-btn').addEventListener('click',calculateMaturityAmount);