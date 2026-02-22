// printer.js
const urlParams = new URLSearchParams(window.location.search);
const model = urlParams.get("model");

if (model && printers[model]) {
  document.getElementById("modelName").textContent = model;
  document.getElementById("modelType").textContent = printers[model].type;
  document.getElementById("modelSpeed").textContent = printers[model].speed;
  document.getElementById("modelResolution").textContent = printers[model].resolution;
  document.getElementById("modelInterfaces").textContent = printers[model].interfaces;
  document.getElementById("modelExtra").textContent = printers[model].extra;
  document.getElementById("modelImage").src = `img/home/${model}.jpg`;
} else {
  document.getElementById("printer-details").innerHTML = "<p>Модель не найдена</p>";
}