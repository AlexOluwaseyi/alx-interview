#!/usr/bin/node

const request = require('request');
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films/';
/*
if (process.argv.length === 3) {
  const movieId = process.argv[2];
  const url = apiEndpoint + movieId;

  request.get(url, async (error, response, body) => {
    if (error) {
      return;
    }
    const data = JSON.parse(body);
    // await console.log(body['characters']);
    const charactersList = data.characters;

    charactersList.forEach(characterUrl => {
      console.log(characterUrl);
      request.get(characterUrl, async (error, response, body) => {
        if (error) {
          return;
        }
        const characterBody = JSON.parse(body);
        console.log(`${characterUrl} - ${characterBody.name}`);
      });
    });
  });
};
*/
const { promisify } = require('util');
const requestGet = promisify(request.get);

if (process.argv.length === 3) {
  const movieId = process.argv[2];
  const url = apiEndpoint + movieId;

  (async () => {
    try {
      const response = await requestGet(url);
      const data = JSON.parse(response.body);
      const charactersList = data.characters;

      for (const characterUrl of charactersList) {
        try {
          const characterResponse = await requestGet(characterUrl);
          const characterBody = JSON.parse(characterResponse.body);
          return `${characterBody.name}`;
        } catch (characterError) {
          console.error('Error fetching character data:', characterError);
        }
      }
    } catch (error) {
      console.error('Error fetching movie data:', error);
    }
  })();
}
