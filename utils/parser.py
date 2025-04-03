import requests


from .cookies import cookies, headers, data


base_url = 'https://tickets.hclokomotiv.ru/poster'


def get_events():
    response = requests.post(base_url, cookies=cookies, headers=headers, data=data)
    try:
        events = response.json()['items']
        events_json = []
        for event in events:
            event_json = {}
            event_json['hall'] = event['hall']
            event_json['name'] = event['name']
            event_json['datetime'] = event['startTimestampStr']
            event_json['unit'] = event['unitName']
            events_json.append(event_json)
        return events_json
    except Exception as e:
        print(f'Exception in get_events: {e}')
        return None
