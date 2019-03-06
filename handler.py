import requests
import os


def notify_slack(event, context):
  request_to_git = requests.get(url=os.environ['REPO_URL'],
                                headers={'Authorization': 'token ' + os.environ['GITHUB_TOKEN']})

  pull_requests = request_to_git.json()

  opened_pull_requests_urls = dict()
  for pull_request in pull_requests:
    if pull_request['state'] == 'open':
      detail = dict()
      detail['title'] = pull_request['title']
      detail['assignee'] = 'None' if pull_request['assignee'] is None else pull_request['assignee']['login']
      opened_pull_requests_urls[pull_request['html_url']] = detail

  text = str()
  for key in opened_pull_requests_urls:
    text += '\n*' + opened_pull_requests_urls[key]['title'] + '* \n' + key + ' (Assignee: ' + \
            opened_pull_requests_urls[key]['assignee'] + ')\n'

  request_to_slack = requests.post(
    url='https://slack.com/api/chat.postMessage?token=' + os.environ['SLACK_TOKEN'] + '&channel=' +
        os.environ['SLACK_CHANNEL'] + '&text=<!here> [GitHub Report] 以下のPull RequestのステータスがOpenです：\n' + text,
    headers={'Content-Type': 'application/x-www-form-urlencoded'})

  return request_to_slack.json()
