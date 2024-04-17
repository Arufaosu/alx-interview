#!/usr/bin/node
// star wars

const request = require('request');

const mainURL = 'https://swapi-api.alx-tools.com/api';

function fetchCharacters (movieID) {
  return new Promise((resolve, reject) => {
    request.get(mainURL + '/films/' + movieID, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const movie = JSON.parse(body);
          resolve(movie.characters);
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}

function displayCharactersNames (charactersURLs) {
  const charactersPromises = [];

  for (const url of charactersURLs) {
    const promise = new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          try {
            const character = JSON.parse(body);

            resolve(character.name);
          } catch (parseError) {
            resolve(parseError);
          }
        }
      });
    });

    charactersPromises.push(promise);
  }

  Promise.all(charactersPromises).then((charactersNames) => {
    for (const name of charactersNames) {
      console.log(name);
    }
  });
}

const movieID = process.argv[2];

fetchCharacters(movieID)
  .then((charactersURLs) => displayCharactersNames(charactersURLs))
  .catch((error) => console.log(error));
