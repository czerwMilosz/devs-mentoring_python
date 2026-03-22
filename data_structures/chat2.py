from collections import defaultdict

events = [
    ["Tom", "login"],
    ["Tom", "view"],
    ["Tom", "view"],
    ["Tom", "purchase"],
    ["Clare", "login"],
    ["Clare", "purchase"],
    ["Rich", "view"],
    ["Rich", "view"],
]

#OUTPUT
"""
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
"""

def create_event_template():
    return {
        "actions": [],
        "counts": defaultdict(int),
        "has_purchase": False
    }

def summarize_events(events: list[list[str,str]]) -> dict:
    event_summary = defaultdict(create_event_template)
    for person, action in events:
        event_summary[person]["actions"].append(action)
        event_summary[person]["counts"][action] += 1

        if action == "purchase":
            event_summary[person]["has_purchase"] = True

    for person in event_summary:
        event_summary[person]["counts"] = dict(event_summary[person]["counts"])
    return dict(event_summary)

def main():
    log_summary = summarize_events(events)
    print(log_summary)

if __name__ == "__main__":
    main()

