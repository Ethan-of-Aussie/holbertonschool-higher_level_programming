#!/usr/bin/node

const element = document.querySelector('.my_list');

const id = document.querySelector('#add_item');
id.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  element.appendChild(newItem);
});
