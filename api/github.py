import os
import requests

API_TOKEN = os.environ['GH_API_TOKEN']
API_USER = os.environ['GH_API_USER']
API_REPO = os.environ['GH_API_REPO']


def get_issues():
    url = f'https://api.github.com/repos/{API_USER}/{API_REPO}/issues?per_page=100&state=all'
    headers = {'Authorization': 'token ' + API_TOKEN}
    resp = requests.get(url, headers=headers)
    print("returned issue list")
    return resp.json()


def post_issue(title, body, **kwargs):
    url = f'https://api.github.com/repos/{API_USER}/{API_REPO}/issues'
    headers = {'Authorization': 'token ' + API_TOKEN}
    data = {'title': title, 'body': body}
    data.update(kwargs)
    resp = requests.post(url, headers=headers, json=data)
    print(f"created issue {title}")
    return resp.json()


def patch_issue(issue_id, **kwargs):
    url = f'https://api.github.com/repos/{API_USER}/{API_REPO}/issues/{issue_id}'
    headers = {'Authorization': 'token ' + API_TOKEN}
    resp = requests.patch(url, headers=headers, json=kwargs)
    print(resp.json())
    print(f"patched issue {issue_id}, {kwargs}")
    return resp.json()
