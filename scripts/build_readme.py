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
IN_REVIEW_REPOS = ["meta/pyrefly", "google/guava"]


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


def pulls_link(repo, state):
    query = f"is:pr is:{state} author:{USER} repo:{repo}"
    return f"[{repo}](https://github.com/pulls?q={urllib.parse.quote_plus(query)})"


def oss_section():
    merged = defaultdict(list)
    for item in search_prs(f"is:pr is:merged is:public author:{USER} -user:{USER}"):
        merged[item["repository_url"].removeprefix(f"{API}/repos/")].append(item["closed_at"])
    in_review = {
        repo: len(search_prs(f"is:pr is:open author:{USER} repo:{repo}"))
        for repo in IN_REVIEW_REPOS
        if repo not in merged
    }
    in_review = {repo: n for repo, n in in_review.items() if n}

    merged_rows = sorted(merged.items(), key=lambda kv: (len(kv[1]), max(kv[1])), reverse=True)
    top = max([len(v) for v in merged.values()] + list(in_review.values()))
    total_merged = sum(len(v) for v in merged.values())

    lines = [
        f"**🌍 {total_merged} Merged Pull Requests Across {len(merged)} Upstream Projects**",
        "",
        "```text",
    ]
    lines += [f"{repo:<38}{f'{len(prs)} merged':<14}{bar(len(prs) / top)}" for repo, prs in merged_rows]
    lines += [f"{repo:<38}{f'{n} in review':<14}{bar(n / top)}" for repo, n in sorted(in_review.items(), key=lambda kv: -kv[1])]
    lines += ["```", ""]

    links = [pulls_link(repo, "merged") for repo, _ in merged_rows]
    links += [pulls_link(repo, "open") for repo in in_review]
    lines.append(f"<sub>{' · '.join(links)}</sub>")
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
