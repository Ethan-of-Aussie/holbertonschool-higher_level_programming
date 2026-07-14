#!/usr/bin/node
const charid = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(character => {
    charid.textContent = character.name;
  })
  .catch(error => console.error('error:', error));
