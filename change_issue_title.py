import os
import requests

if __name__ == '__main__':
    token = os.environ['MY_GITHUB_TOKEN']
    issue_number = os.environ['ISSUE_NUMBER']

    owner = "LEEMINJOO"
    repo = "blog-comments"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    original_title = requests.get(url, auth=("username", token)).json()["title"]
    payload = {
        "title": "[Closed] " + original_title.split('|')[0]
    }
    r = requests.patch(url, auth=("username", token), json=payload)
