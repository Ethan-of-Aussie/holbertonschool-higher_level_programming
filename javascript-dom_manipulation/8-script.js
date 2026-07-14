#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloElement = document.querySelector('#hello');
      helloElement.textContent = data.hello;
    });
});
