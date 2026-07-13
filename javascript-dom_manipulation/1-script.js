#!/usr/bin/node

const id = document.querySelector('#red_header');

id.addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
