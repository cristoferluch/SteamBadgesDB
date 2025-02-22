[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github-actions&logoColor=white)](https://github.com/features/actions "Go to GitHub Actions homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![Steam](https://img.shields.io/badge/Steam-profile-blue.svg?logo=steam)](https://steamcommunity.com/id/cristoferluch/)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcristoferluch%2FSteamBadgesDB%2Fmain%2Fsrc%2Fbadge_count.json&query=%24.count&label=Badges&logo=steam)

<br><br>
<p align="center">
   <img src="https://github.com/cristoferluch/assets/blob/main/logo_steam.svg" alt="steam_logo" width="500">
</p>

<br><br>
# Steam Badge DB

The [badges.json](https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/badges.json) file contains an up-to-date list of all Steam badges.
- type 0: Games
- type 1: Event Badges
- type 2: Special Badges
- type 3: Seasonal Badges

Badges are updated daily through GitHub Actions.

````shel

[
    {
        "id": 1,
        "appid": 220,
        "name": "Half-Life 2",
        "cards": 8,
        "type": 0
    },
    {
        "id": 1,
        "appid": 300,
        "name": "Day of Defeat: Source",
        "cards": 6,
        "type": 0
    },
    {
        "id": 1,
        "appid": 440,
        "name": "Team Fortress 2",
        "cards": 9,
        "type": 0
    },
    {
        "id": 1,
        "appid": 550,
        "name": "Left 4 Dead 2",
        "cards": 8,
        "type": 0
    },
   ... more content ... 
]

````


## Usage

#### Python

````shel
import requests

response = requests.get("https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/badges.json")
badges = response.json()

print(badges)
````
#### Node.js

````shel
const axios = require('axios');

axios.get('https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/badges.json')
  .then(response => {
    const badges = response.data;
    console.log(badges);
  })
  .catch(error => {
    console.error(error);
  });
````

API provided by [GermanDarknes](https://github.com/GermanDarknes).

#### Made by [cristoferluch](https://steamcommunity.com/id/cristoferluch/)
