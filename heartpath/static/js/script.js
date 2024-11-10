let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.header .navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

var swiper = new Swiper(".home-slider", {
    loop:true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
 });

let loadMoreBtn = document.querySelector('.packages .load-more .btn');
let currentItem = 3;

loadMoreBtn.onclick = () =>{
    let boxes = [...document.querySelectorAll('.packages .box-container .box')];
    for(var i = currentItem; i< currentItem + 3; i++){
        boxes[i].style.display = 'inline-block';
    }
    currentItem += 3;
    if(currentItem >= boxes.length){
        loadMoreBtn.style.display = 'none';
    }
}


function validateForm(form) {
    var name = form.name.value;
    var email = form.email.value;
    var phone = form.phone.value;
    var address = form.address.value;
    var destination = form.destination.value;
    var guests = form.guests.value;
    var arrival = form.arrival.value;
    var departure = form.departure.value;
    var nameRegex = /^[a-zA-Z\s]*$/;
    var phoneRegex = /^\d{10}$/;
    var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    var errorMessage = "";

    if (!nameRegex.test(name)) {
        errorMessage += "Invalid name\n";
    }

    if (!emailRegex.test(email)) {
        errorMessage += "Invalid email\n";
    }

    if (!phoneRegex.test(phone)) {
        errorMessage += "Invalid phone number\n";
    }

    if (address == "") {
        errorMessage += "Address is required\n";
    }

    if (destination == "") {
        errorMessage += "Destination is required\n";
    }

    if (guests == "") {
        errorMessage += "Number of guests is required\n";
    }

    if (arrival == "") {
        errorMessage += "Arrival date is required\n";
    }

    if (departure == "") {
        errorMessage += "Departure date is required\n";
    }

    if (errorMessage != "") {
        alert(errorMessage);
        return false;
    } else {
        alert("Thank You for Booking");
        return true;
    }
}
