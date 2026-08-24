# 6. Podsumowanie eventów użytkowników
'''{
    "Tom": {
        "actions": ["login", "view", "view", "purchase"],
        "counts": {
            "login": 1,
            "view": 2,
            "purchase": 1
        },
        "has_purchase": True
    },
    ...
}'''
from collections import defaultdict

EVENTS = [
    ["Tom", "login"],
    ["Tom", "view"],
    ["Tom", "view"],
    ["Tom", "purchase"],
    ["Clare", "login"],
    ["Clare", "purchase"],
    ["Rich", "view"],
    ["Rich", "view"],
]

def log_structure():
    return {"actions": [],
            "counts": {},
            "has_purchase": False}

def summarize_events(events: list[list[str]]) -> dict:
    d = defaultdict(log_structure)
    for person, action in events:
        d[person]["actions"].append(action)
        d[person]["counts"][action] = d[person]["counts"].get(action, 0) + 1

        if action == "purchase":
            d[person]["has_purchase"] = True

    return dict(d)

def main():
    print(summarize_events(EVENTS))

if __name__ == '__main__':
    main()

