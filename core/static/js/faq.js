function toggleFAQ(id) {
  const answer = document.getElementById(`answer-${id}`);
  const plus = document.getElementById(`icon-plus-${id}`);
  const minus = document.getElementById(`icon-minus-${id}`);
  const isOpen = !answer.classList.contains("hidden");

  // Lukk alle først
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
