document.addEventListener("DOMContentLoaded", function () {
  const productSelect = document.getElementById("id_product");
  const priceOutput = document.getElementById("price-output");
  const totalInput = document.getElementById("id_total_price");

  function updatePrice() {
    const selectedOption = productSelect.options[productSelect.selectedIndex];
    const price = selectedOption.getAttribute("data-price");

    if (price) {
      priceOutput.textContent = parseInt(price);
      totalInput.value = price;
    } else {
      priceOutput.textContent = "-";
      totalInput.value = "";
    }
  }

  updatePrice();
  productSelect.addEventListener("change", updatePrice);
});
