[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github-actions&logoColor=white)](https://github.com/features/actions "Go to GitHub Actions homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![Steam](https://img.shields.io/badge/Steam-profile-blue.svg?logo=steam)](https://steamcommunity.com/id/cristoferluch/)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcristoferluch%2FSteamBadgesDB%2Fmain%2Ftrading_cards_appids.json&query=%24.size&label=Badges&logo=steam)

<br><br>
<p align="center">
   <img src="https://github.com/cristoferluch/assets/blob/main/logo_steam.svg" alt="steam_logo" width="500">
</p>

<br><br>
# Steam Badge DB

This Python script is designed to search for all Steam games that have collectible [trading cards](https://steamcommunity.com/tradingcards) and maintain an up-to-date list of these games in a JSON file. It utilizes cutting-edge technologies and libraries for efficient data retrieval and automation. Moreover, the JSON file is automatically updated every 8 hours through GitHub Actions, ensuring the data remains fresh and up-to-date

- **Beautiful Soup**: This library is employed for web scraping and extracting information from web pages.


#### trading_cards_appids.json

The [trading_cards_appids.json](https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/trading_cards_appids.json) file contains an up-to-date list of Steam games that offer collectible trading cards. Each entry in the file includes important details, such as the application ID (appid), game name, and the number of available cards.

Example data structure in the file:


````shel
{
    "size": 12522,
    "data": [
      {
        "appid": 220,
        "name": "Half-Life 2",
        "cards": 8
      },
      {
        "appid": 300,
        "name": "Day of Defeat: Source",
        "cards": 6
      },
      {
        "appid": 440,
        "name": "Team Fortress 2",
        "cards": 9
      },
      {
        "appid": 550,
        "name": "Left 4 Dead 2",
        "cards": 8
      }
      ... more content ... 
    ]
}
````


## Usage

#### Python

````shel
import requests

response = requests.get("https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/trading_cards_appids.json")
badges = response.json()

print(badges)
````
#### Node.js

````shel
const axios = require('axios');

axios.get('https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/trading_cards_appids.json')
  .then(response => {
    const badges = response.data;
    console.log(badges);
  })
  .catch(error => {
    console.error(error);
  });
````

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


#### Made by [cristoferluch](https://steamcommunity.com/id/cristoferluch/)
