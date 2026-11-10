#!/usr/bin/env python3
"""AI Shelf tally: turns runs.csv into a leaderboard.

Usage:
    python3 tally.py runs.csv
    python3 tally.py runs.csv --brand "Your Brand" --sources sources.csv

runs.csv columns: engine,run,position,brand  (one row per brand named, in answer order)
No dependencies, Python 3.8+.
"""
import argparse
import csv
import sys
from collections import defaultdict


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    need = {"engine", "run", "position", "brand"}
    if not rows or not need.issubset(rows[0].keys()):
        sys.exit(f"{path}: expected columns {sorted(need)}")
    rows = [r for r in rows if (r.get("brand") or "").strip()]
    if not rows:
        sys.exit(f"{path}: no brands logged yet")
    return rows


def main():
    p = argparse.ArgumentParser(description="AI Shelf leaderboard")
    p.add_argument("csv")
    p.add_argument("--brand", help="highlight your brand (and show it even at 0)")
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--sources", help="sources.csv: also rank the sources the AIs cited")
    a = p.parse_args()

    rows = load(a.csv)
    answers = sorted({(r["engine"], r["run"]) for r in rows})
    engines = sorted({e for e, _ in answers})
    total = len(answers)

    named = defaultdict(set)          # brand -> {(engine, run)}
    firsts = defaultdict(int)         # brand -> times listed #1
    per_engine = defaultdict(lambda: defaultdict(set))
    runs_per_engine = defaultdict(set)
    for r in rows:
        key = (r["engine"], r["run"])
        b = r["brand"].strip()
        runs_per_engine[r["engine"]].add(r["run"])
        if b == "-":  # answer named no brand: counts as an answer, not a brand
            continue
        named[b].add(key)
        per_engine[b][r["engine"]].add(r["run"])
        if str(r["position"]).strip() == "1":
            firsts[b] += 1

    winners = {b for b, n in firsts.items() if n}
    print(f"\nAI SHELF  {total} answers · {len(engines)} AIs · {len(named)} brands named · {len(winners)} different #1s\n")

    board = sorted(named, key=lambda b: (-len(named[b]), -firsts[b], b))
    if a.brand and a.brand not in named:
        board.append(a.brand)
    shown = board[: a.top]
    if a.brand and a.brand not in shown:
        shown.append(a.brand)

    short = {"Google AI Mode": "AI Mode", "Perplexity": "Perplex"}
    labels = [short.get(e, e)[:10] for e in engines]
    cw = max(len(l) for l in labels) + 2
    w = max(len(b) for b in shown + ["BRAND"]) + 2
    width = 10
    head = "".join(l.ljust(cw) for l in labels)
    print(f"{'BRAND'.ljust(w)}{'NAMED':<7}{'':<{width + 2}}{'#1':<4}{head.rstrip()}")
    for b in shown:
        n = len(named.get(b, ()))
        bar = "█" * int(width * n / total + 0.5) if total else ""
        cells = "".join(
            f"{len(per_engine[b][e])}/{len(runs_per_engine[e])}".ljust(cw) for e in engines
        )
        mark = " ◀" if a.brand and b == a.brand else ""
        print(f"{b.ljust(w)}{f'{n}/{total}':<7}{bar.ljust(width)}  {firsts[b]:<4}{cells.rstrip()}{mark}")
    print()

    if a.sources:
        with open(a.sources, newline="", encoding="utf-8-sig") as f:
            src = list(csv.DictReader(f))
        need = {"engine", "run", "source"}
        if not src or not need.issubset(src[0].keys()):
            sys.exit(f"{a.sources}: expected columns {sorted(need)}")
        src = [r for r in src if (r.get("source") or "").strip()]
        if not src:
            sys.exit(f"{a.sources}: no sources logged yet")
        hits = defaultdict(set)
        ais = defaultdict(set)
        for r in src:
            s = r["source"].strip()
            hits[s].add((r["engine"], r["run"]))
            ais[s].add(r["engine"])
        top = sorted(hits, key=lambda s: (-len(ais[s]), -len(hits[s]), s))[: a.top]
        sw = max(len(s) for s in top + ["SOURCE"]) + 2
        print(f"{'SOURCE'.ljust(sw)}{'ANSWERS':<10}AIs")
        for s in top:
            print(f"{s.ljust(sw)}{f'{len(hits[s])}/{total}':<10}{', '.join(sorted(ais[s]))}")
        print()


if __name__ == "__main__":
    main()
