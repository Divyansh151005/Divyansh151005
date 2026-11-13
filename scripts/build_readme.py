"""Regenerate the open source section of README.md from public GitHub data."""

import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict

USER = "Divyansh151005"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
API = "https://api.github.com"


def get(path, params=None):
    url = f"{API}{path}" + (f"?{urllib.parse.urlencode(params)}" if params else "")
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code < 500 or attempt == 2:
                raise
        time.sleep(2 ** attempt)


def search_prs(query):
    items, page = [], 1
    while True:
        batch = get("/search/issues", {"q": query, "per_page": 100, "page": page})["items"]
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def bar(fraction, width=20):
    filled = round(fraction * width)
    return "█" * filled + "░" * (width - filled)


def repo_of(item):
    return item["repository_url"].removeprefix(f"{API}/repos/")


def landed_by_bot(item):
    """Meta (ShipIt) and Google (Copybara) land PRs internally, then a bot closes them with the commit."""
    events = get(f"/repos/{repo_of(item)}/issues/{item['number']}/events", {"per_page": 100})
    return any(
        e["event"] == "closed" and e.get("commit_id") and (e.get("actor") or {}).get("login", "").endswith("[bot]")
        for e in events
    )


def oss_section():
    scope = f"is:pr is:public author:{USER} -user:{USER}"
    merged = defaultdict(list)
    for item in search_prs(f"{scope} is:merged"):
        merged[repo_of(item)].append(item["closed_at"])
    for item in search_prs(f"{scope} is:closed is:unmerged"):
        if landed_by_bot(item):
            merged[repo_of(item)].append(item["closed_at"])

    rows = sorted(merged.items(), key=lambda kv: (len(kv[1]), max(kv[1])), reverse=True)
    top = max(len(v) for v in merged.values())
    total = sum(len(v) for v in merged.values())

    lines = [f"**🌍 {total} Merged Pull Requests Across {len(merged)} Upstream Projects**", "", "```text"]
    lines += [f"{repo:<38}{f'{len(prs)} merged':<12}{bar(len(prs) / top)}" for repo, prs in rows]
    lines += ["```"]
    return "\n".join(lines)


def replace(readme, name, body):
    start, end = f"<!--START_SECTION:{name}-->", f"<!--END_SECTION:{name}-->"
    return re.sub(f"{re.escape(start)}.*?{re.escape(end)}", lambda _: f"{start}\n{body}\n{end}", readme, flags=re.S)


def main():
    with open(README, encoding="utf-8") as f:
        readme = f.read()
    readme = replace(readme, "oss", oss_section())
    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
