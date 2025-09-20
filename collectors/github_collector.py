from github import Github
import os
from dotenv import load_dotenv
load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

def fetch_github(query="leak", limit=5):
    repos = g.search_repositories(query=query)
    results = []
    for repo in repos[:limit]:
        results.append({
            "platform": "github",
            "user": repo.owner.login,
            "timestamp": str(repo.created_at),
            "text": repo.description or "",
            "url": repo.html_url
        })
    return results
