import os
import requests

API_UID = os.environ['FT_API_UID']
API_SECRET = os.environ['FT_API_SECRET']
API_URL = 'https://api.intra.42.fr/'


def get_oauth_token():
    url = API_URL + 'oauth/token'
    post_data = {
        'grant_type': 'client_credentials',
        'client_id': API_UID,
        'client_secret': API_SECRET
    }
    resp = requests.post(url, data=post_data)
    print("returned oauth token")
    return resp.json()['access_token']


def get_events(token, campus_id=None, cursus_id=None):
    url = API_URL + 'v2'
    if campus_id is not None:
        url += '/campus/' + str(campus_id)
    if cursus_id is not None:
        url += '/cursus/' + str(cursus_id)
    url += '/events'
    headers = {'Authorization': 'Bearer ' + token}
    resp = requests.get(url, headers=headers)
    print("returned event list")
    return resp.json()
