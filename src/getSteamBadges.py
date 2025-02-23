import requests
import json
import html

def get_appid_list():
    url = "https://www.steamcardexchange.net/api/request.php?GetInventory"
    response = requests.get(url)
    return response.json().get('data', [])

def load_badges(filename="src/special_badges.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as input_file:
            return json.load(input_file)
    except FileNotFoundError:
        return []

def save_badges(badges, filename="badges.json"):
    # Decodifica as entidades HTML no dicionário
    decoded_badges = json.loads(json.dumps(badges), object_hook=lambda d: {k: html.unescape(v) if isinstance(v, str) else v for k, v in d.items()})

    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(decoded_badges, output_file, ensure_ascii=False)


def save_badge_count(badges, filename="src/badge_count.json"):
    badge_count = {"count": len(badges)}
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(badge_count, output_file, ensure_ascii=False)

def main():
    badges = []
    data = get_appid_list()
    
    for game in data:
        if game[3][0] > 0:
            badges.append({
                'id': 1,
                'appid': game[0][0],
                'name': game[0][1],
                'cards': game[3][0],
                'type': 0
            })

    existing_badges = load_badges()

    for existing_badge in existing_badges:
        for badge in badges:
            if badge['appid'] == existing_badge['appid'] and badge['id'] == existing_badge['id']:
                badge['type'] = existing_badge['type']

    for existing_badge in existing_badges:
        if not any(badge['appid'] == existing_badge['appid'] and badge['id'] == existing_badge['id'] for badge in badges):
            badges.append(existing_badge)

    badges.sort(key=lambda x: x["appid"])

    save_badges(badges)
    save_badge_count(badges)

if __name__ == "__main__":
    main()
