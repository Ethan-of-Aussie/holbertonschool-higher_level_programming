#!/usr/bin/node

const element = document.querySelector('header');

const id = document.querySelector('#update_header');
id.addEventListener('click', function () {
  element.textContent = 'New Header!!!';
});
