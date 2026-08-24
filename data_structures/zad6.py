from unittest import case
from typing import Any

API_OUTPUT = {
    "data": [1, 2, "asd", [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, "120"],
        'analysis_2': [10, 100, "test", 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}

def extract_strings(data:Any):

    match data:
        case str():
            return [data]
        case list():
            return [x for item in data for x in extract_strings(item)]
        case dict():
            return [x for value in data.values() for x in extract_strings(value)]
        case _:
            return []

    # if isinstance(data, str):
    #     return [data]
    # elif isinstance(data, list):
    #     return [x for item in data for x in extract_strings(item)]
    # elif isinstance(data, dict):
    #     return [x for value in data.values() for x in extract_strings(value)]
    #
    # return result

def main():
    print(extract_strings(API_OUTPUT))
if __name__ == '__main__':
    main()