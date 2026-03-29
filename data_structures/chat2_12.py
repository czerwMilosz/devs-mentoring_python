# 12. Wyciągnij wszystkie stringi (bez rekurencji)

DATA = {
    "data": [1, 2, "asd", [2, 3, 4, "hello"]],
    "nested_analysis": {
        "analysis_1": [1, 10, "world"],
        "analysis_2": [10, 100, "test", 200]
    },
    "probes": [["probe_1", "probe_2"], "probe_3"]
}

def extract_strings(data) -> list[str]:
    result = []
    stack = [data]
    while stack:
        current = stack.pop()

        if isinstance(current, str):
            result.append(current)

        elif isinstance(current, list):
            stack.extend(current)

        elif isinstance(current, dict):
            stack.extend(current.values())

    return result


def main():
    print(extract_strings(DATA))

if __name__ == "__main__":
    main()