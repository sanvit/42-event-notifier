import api.ft as ft_api
import api.github as gh_api
from datetime import datetime


def init():
    oauth_token = ft_api.get_oauth_token()
    events = ft_api.get_events(oauth_token, campus_id=29)
    issues = gh_api.get_issues()
    for event in events:
        issue = get_or_create_issue(event, issues)
        # start_time = parse_time(event['begin_at'])
        if issue['state'] == 'open':
            end_time = parse_time(event['end_at'])
            if (event['max_people'] and event['nbr_subscribers'] >= event['max_people']) or end_time < datetime.now():
                gh_api.patch_issue(issue['number'], state='closed')


def get_or_create_issue(event, issues):
    for issue in issues:
        if issue['title'].startswith(f"[{event['id']}]"):
            return issue
    issue = gh_api.post_issue(
        f"[{event['id']}] {event['name']}", event['description'])
    return issue


def parse_time(time):
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')


init()
