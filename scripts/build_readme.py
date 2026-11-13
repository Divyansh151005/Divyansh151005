"""Regenerate the auto-updated sections of README.md from public GitHub data."""

import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

USER = "Divyansh151005"
TZ = ZoneInfo("Asia/Kolkata")
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


def paginate(path, params=None, key=None):
    page = 1
    while True:
        data = get(path, {**(params or {}), "per_page": 100, "page": page})
        batch = data[key] if key else data
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def bar(pct, width=25):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def row(label, value, pct):
    return f"{label:<25}{value:<20}{bar(pct)}   {pct:05.2f} % "


def commit_times(repos):
    times = []
    for repo in repos:
        try:
            for c in paginate(f"/repos/{repo['full_name']}/commits", {"author": USER}):
                stamp = c["commit"]["author"]["date"]
                times.append(datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(TZ))
        except urllib.error.HTTPError as err:
            if err.code not in (404, 409) and err.code < 500:
                raise
    return times


def analytics_section(repos):
    times = commit_times(repos)
    total = len(times) or 1

    buckets = Counter()
    for t in times:
        buckets["morning" if 6 <= t.hour < 12 else "daytime" if t.hour < 18 and t.hour >= 12 else "evening" if t.hour >= 18 else "night"] += 1
    early = buckets["morning"] + buckets["daytime"] >= buckets["evening"] + buckets["night"]
    periods = [("🌞 Morning", "morning"), ("🌆 Daytime", "daytime"), ("🌃 Evening", "evening"), ("🌙 Night", "night")]

    days = Counter(t.strftime("%A") for t in times)
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    best_day = max(week, key=lambda d: days[d])

    langs = Counter(r["language"] for r in repos if r["language"] and not r["fork"])
    lang_total = sum(langs.values()) or 1

    lines = ["**I'm an Early 🐤**" if early else "**I'm a Night 🦉**", "", "```text"]
    lines += [row(label, f"{buckets[key]} commits", buckets[key] / total * 100) for label, key in periods]
    lines += ["```", "", f"**📅 I'm Most Productive on {best_day}**", "", "```text"]
    lines += [row(d, f"{days[d]} commits", days[d] / total * 100) for d in week]
    lines += ["```", "", f"**💬 I Mostly Code in {langs.most_common(1)[0][0]}**", "", "```text"]
    lines += [
        row(lang, f"{n} repo{'s' if n > 1 else ''}", n / lang_total * 100)
        for lang, n in langs.most_common(6)
    ]
    lines += ["```"]
    return "\n".join(lines)


def oss_section():
    items = list(paginate("/search/issues", {"q": f"is:pr is:merged is:public author:{USER} -user:{USER}"}, key="items"))
    by_repo = defaultdict(list)
    for item in items:
        by_repo[item["repository_url"].removeprefix(f"{API}/repos/")].append(item["closed_at"])
    repos = sorted(by_repo.items(), key=lambda kv: (len(kv[1]), max(kv[1])), reverse=True)
    top = max(len(v) for v in by_repo.values())

    lines = [f"**🌍 {len(items)} Merged Pull Requests Across {len(by_repo)} Upstream Projects**", "", "```text"]
    for repo, merged in repos:
        n = len(merged)
        lines.append(f"{repo:<38}{f'{n} merged':<12}{bar(n / top * 100, 20)}")
    lines += ["```"]
    links = " · ".join(
        f"[{repo}](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3A{USER}+repo%3A{urllib.parse.quote(repo, safe='')})"
        for repo, _ in repos
    )
    lines += ["", f"<sub>{links}</sub>"]
    return "\n".join(lines)


def replace(readme, name, body):
    start, end = f"<!--START_SECTION:{name}-->", f"<!--END_SECTION:{name}-->"
    return re.sub(f"{re.escape(start)}.*?{re.escape(end)}", lambda _: f"{start}\n{body}\n{end}", readme, flags=re.S)


def main():
    repos = list(paginate(f"/users/{USER}/repos", {"type": "owner"}))
    with open(README, encoding="utf-8") as f:
        readme = f.read()
    readme = replace(readme, "oss", oss_section())
    readme = replace(readme, "analytics", analytics_section(repos))
    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
