document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelector(".popup-wrapper").classList.add("show-popup");
    }, 2000); // Show after 2 seconds (2000ms)

    // Close the popup when the close button is clicked
    document.querySelector(".close-popup").addEventListener("click", function () {
        document.querySelector(".popup-wrapper").classList.remove("show-popup");
    });
});