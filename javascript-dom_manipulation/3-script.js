#!/usr/bin/node

const element = document.querySelector('header');

const id = document.querySelector('#toggle_header');
id.addEventListener('click', function () {
    if (!element.classList.contains('red') && !element.classList.contains('green')) {
        element.classList.add('red');
    }
    if (element.classList.contains('red')) {
        element.classList.replace('red', 'green');
    } else if (element.classList.contains('green')) {
        element.classList.replace('green', 'red');
    }
});
