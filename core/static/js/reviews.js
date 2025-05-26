document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".review-card");
  let current = 0;

  window.nextReview = function () {
    cards[current].classList.remove("active");
    current = (current + 1) % cards.length;
    cards[current].classList.add("active");
  };

  window.prevReview = function () {
    cards[current].classList.remove("active");
    current = (current - 1 + cards.length) % cards.length;
    cards[current].classList.add("active");
  };
});
