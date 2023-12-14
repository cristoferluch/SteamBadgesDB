import json
import re
import os
from bs4 import BeautifulSoup
import requests
import datetime
from tqdm import tqdm
import logging
import time

logging.getLogger('httpx').setLevel(logging.ERROR)
log_file_path = os.path.join(os.getcwd(), 'app_log.txt')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

api_key = os.getenv('API_KEY')
steam_id = os.getenv('STEAM_ID')

# Fetch appids from the Steam APIds
def fetch_steam_appids():
    data = []
    url = f'https://api.steampowered.com/IStoreService/GetAppList/v1/?key={api_key}&max_results=50000'
    try:
        response = requests.get(url, timeout=60.0)
        response_json = response.json()
        data.extend(response_json['response']['apps'])

        while 'have_more_results' in response_json['response'] and response_json['response']['have_more_results']:
            last_app_id = response_json['response']['last_appid']
            url = f'https://api.steampowered.com/IStoreService/GetAppList/v1/?key={api_key}&last_appid={last_app_id}&max_results=50000'
            response = requests.get(url, timeout=60.0)
            response_json = response.json()
            data.extend(response_json['response']['apps'])
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {str(e)}")
        return None    

# Fetch appids related to trading cards
def fetch_trading_cards_appids():
    url = 'https://raw.githubusercontent.com/cristoferluch/SteamBadgesDB/main/trading_cards_appids.json'
    try:
        response = requests.get(url)
        response = response.json()
        return response['data']
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {str(e)}")
        return None 

# Check trading cards of a specific appid
def check_game_trading_cards(appid):
    url = f'https://steamcommunity.com/profiles/{steam_id}/gamecards/{appid}/'

    try:
        response = requests.get(url, timeout=5.0)
        logging.info(f"testing {appid} status_code = {response.status_code}")
        if response.status_code != 200:
            if response.status_code == 302:
                return None
            logging.warning(f"Status Code {response.status_code} to check {appid}")

        if response is None:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        has_cards = bool(soup.find('div', class_='badge_title'))

        if has_cards:
            game_name_element = soup.find('div', class_='badge_title')
            meta_tag = soup.find('meta', {'property': 'og:description'})
            cards = None
            print("test")
            if meta_tag:
                content = meta_tag.get('content')
                match = re.search(r'\b(5|6|7|8|9|10|11|12|13|14|15|16)\b', content)
                if match:
                    cards = match.group()

            if game_name_element:
                game_name = game_name_element.get_text().strip().replace(' Badge', '')
                logging.info(f"Found trading cards for app_id {appid}: Game Name: {game_name}, Cards: {cards}")
                return appid, game_name, cards
            else:
                return None
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data for app_id {appid}: {str(e)}")
        return None

# Save data related to trading cards in a JSON file
def save_trading_cards_json(trading_cards_appids):
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)).replace("Scripts", ""), "trading_cards_appids.json")

    trading_cards_appids.sort(key=lambda x: x["appid"])

    formatted_json = {
        "size": len(trading_cards_appids),
        "data": trading_cards_appids
    }

    with open(json_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(formatted_json, output_file, ensure_ascii=False)

def format_timestamp(timestamp):
    converted_date = datetime.datetime.fromtimestamp(timestamp)
    return converted_date.strftime('%Y-%m-%d')

# Filter appids to be checked
def filter_appids_to_check(appid_list, trading_cards_appids):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y-%m-%d')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    appids_to_check = []
    for item in appid_list:

        date = format_timestamp(item['last_modified'])
        if date == current_date or date == yesterday_date:  
            app_id = item['appid']
            if int(app_id) in [item['appid'] for item in trading_cards_appids]:
                continue

            appids_to_check.append(app_id)
    return appids_to_check

def main():
    print('Fetching steam appids...')
    appids_list = fetch_steam_appids()
    print('Total appids:', len(appids_list))
    trading_cards_appids = fetch_trading_cards_appids()
    print('Total trading cards appids:', len(trading_cards_appids))
    appids_to_check = filter_appids_to_check(appids_list, trading_cards_appids)
    print('Total appids to check:', len(appids_to_check))
    print('\n')
    total = len(appids_to_check)

    pbar = tqdm(total=total)

    trading_cards = []
    for appid in appids_to_check:
        result = check_game_trading_cards(appid)
        if result is not None:
            appid, name, cards = result
            trading_cards.append({'appid': appid, 'name': name, 'cards': cards})
            time.sleep(0.6)
        pbar.update(1)
    pbar.close()

    print("\nAdded appids")
    for item in trading_cards:
        print(item)

    trading_cards_appids.extend(trading_cards)

    save_trading_cards_json(trading_cards_appids)

if __name__ == '__main__':
    main()
