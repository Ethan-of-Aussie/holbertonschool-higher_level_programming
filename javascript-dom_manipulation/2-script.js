#!/usr/bin/node
const element = document.querySelector('header');

const id = document.querySelector('#red_header');
id.addEventListener('click', function () {
  element.classList.toggle('red');
});
