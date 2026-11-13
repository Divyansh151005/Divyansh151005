"""Regenerate the merged-contributions section of README.md from GitHub search."""

import json
import os
import re
import urllib.parse
import urllib.request
from collections import defaultdict

USER = "Divyansh151005"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
START = "<!--START_SECTION:merged-->"
END = "<!--END_SECTION:merged-->"


def search_merged_prs():
    query = f"is:pr is:merged author:{USER} -user:{USER}"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    items, page = [], 1
    while True:
        params = urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        req = urllib.request.Request(f"https://api.github.com/search/issues?{params}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            batch = json.load(resp)["items"]
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def render(items):
    by_repo = defaultdict(list)
    for item in items:
        repo = item["repository_url"].removeprefix("https://api.github.com/repos/")
        merged_at = item["pull_request"].get("merged_at") or item["closed_at"]
        by_repo[repo].append((merged_at, item["number"], item["title"], item["html_url"]))

    for prs in by_repo.values():
        prs.sort(reverse=True)
    repos = sorted(by_repo.items(), key=lambda kv: kv[1][0][0], reverse=True)

    total = sum(len(prs) for prs in by_repo.values())
    lines = [
        '<p align="center">',
        f'  <img src="https://img.shields.io/badge/Merged_PRs-{total}-334155?style=for-the-badge&logo=git-merge&logoColor=white" alt="{total} merged PRs"/>',
        f'  <img src="https://img.shields.io/badge/Repositories-{len(by_repo)}-475569?style=for-the-badge&logo=github&logoColor=white" alt="{len(by_repo)} repositories"/>',
        "</p>",
        "",
        "<table>",
    ]
    for repo, prs in repos:
        owner = repo.split("/")[0]
        pr_lines = "<br/>".join(
            f'<a href="{url}">#{num}</a> {escape(title)} <sub>· {merged_at[:10]}</sub>'
            for merged_at, num, title, url in prs
        )
        lines += [
            "<tr>",
            f'<td width="64" align="center"><img src="https://github.com/{owner}.png?size=80" width="40" alt="{owner}"/></td>',
            f'<td><b><a href="https://github.com/{repo}">{repo}</a></b> <sub>· {len(prs)} merged</sub><br/>{pr_lines}</td>',
            "</tr>",
        ]
    lines += [
        "</table>",
        "",
        '<p align="right"><sub>Auto-updated daily from GitHub search</sub></p>',
    ]
    return "\n".join(lines)


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("`", "")


def main():
    with open(README, encoding="utf-8") as f:
        readme = f.read()
    section = f"{START}\n{render(search_merged_prs())}\n{END}"
    updated = re.sub(f"{re.escape(START)}.*?{re.escape(END)}", lambda _: section, readme, flags=re.S)
    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)


if __name__ == "__main__":
    main()
