const refreshButton = document.getElementsByClassName("refresh")[0];

async function getData() {
    const url = "/get-random-quote/";
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        const quoteh3 = document.getElementById("quote");
        quoteh3.textContent = json.quote;
    } catch (error) {
        console.error(error.message);
    }
}
refreshButton.addEventListener('click', function () {
    getData();
})