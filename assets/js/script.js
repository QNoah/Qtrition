hamburger = document.getElementById('hamburger');
sidebar = document.getElementById('sidebar');

function show_nav() {
    sidebar.classList.toggle('active');
}
    let slide_image = document.getElementById('slide-home-images');


    setInterval(function() {
    if(slide_image.src.match("slide-1.jpg")) {
        slide_image.src = "./assets/imgs/slide-2.jpg";
    } else if(slide_image.src.match("slide-2.jpg")) {
        slide_image.src = "./assets/imgs/slide-3.jpg";
    } else {
        slide_image.src = "./assets/imgs/slide-1.jpg";
    }
    }, 3000);




    // let images = ['./assets/imgs/slide-1.jpg', './assets/imgs/slide-2.jpg', './assets/imgs/slide-3.jpg']
    // setInterval(function(){
    //     let random = Math.floor(Math.random() * images.length);
    //     slide_image.src = images[random];
    // }, 800);
