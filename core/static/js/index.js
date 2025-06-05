// Swiper slider
const swiper = new Swiper(".mySwiper", {
  loop: true,
  slidesPerView: 3,
  spaceBetween: 10,
  grabCursor: true,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    600: {
      slidesPerView: 2,
    },
    900: {
      slidesPerView: 3,
    }
  }
});

// Egne piler
document.getElementById("left").addEventListener("click", () => {
  swiper.slidePrev();
});

document.getElementById("right").addEventListener("click", () => {
  swiper.slideNext();
});

// Navigasjonsmeny
const navBar = document.getElementById("navBar");

function showMenu() {
  navBar.style.right = "0";
  document.querySelector(".fa-bars").style.display = "none";
}

function hideMenu() {
  navBar.style.right = "-240px";
  document.querySelector(".fa-bars").style.display = "block";
}




function toggleFAQ(id) {
  const answer = document.getElementById(`answer-${id}`);
  const plus = document.getElementById(`icon-plus-${id}`);
  const minus = document.getElementById(`icon-minus-${id}`);
  const isOpen = !answer.classList.contains("hidden");

  // Lukk alle andre
  document.querySelectorAll(".faq-answer").forEach(el => el.classList.add("hidden"));
  document.querySelectorAll("[id^='icon-plus-']").forEach(el => el.classList.remove("hidden"));
  document.querySelectorAll("[id^='icon-minus-']").forEach(el => el.classList.add("hidden"));

  // Åpne valgt hvis den ikke var åpen
  if (!isOpen) {
    answer.classList.remove("hidden");
    plus.classList.add("hidden");
    minus.classList.remove("hidden");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".faq-toggle").forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-id");
      toggleFAQ(id);
    });
  });
});


document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.getElementById("review-carousel");
  const cards = document.querySelectorAll(".review-card");
  let currentIndex = 0;

  function updateCarousel() {
    const cardWidth = cards[0].offsetWidth + 30; // kort + gap
    carousel.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
  }

  window.nextReview = function () {
    if (currentIndex < cards.length - 2) {
      currentIndex++;
      updateCarousel();
    }
  };

  window.prevReview = function () {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  };
});
