hamburger = document.getElementById('hamburger');
mobile_nav = document.getElementById('mobile-nav');

function show_mobile_nav() {
    console.log("Hello");
    if (mobile_nav.style.display === "none") {
        hamburger.src = './imgs/cross.png';
        mobile_nav.style.display = "block";
    } else {
        mobile_nav.style.display= "none";
        hamburger.src = './imgs/hamburger.png';
    }
}