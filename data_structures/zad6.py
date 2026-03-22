API_OUTPUT = {
    "data": [1, 2, "asd", [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, "120"],
        'analysis_2': [10, 100, "test", 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}

def extract_strings(data:dict):
    result = list()

    if isinstance(data, str):
        return [data]
    elif isinstance(data, list):
        for item in data:
            result.extend(extract_strings(item))
    elif isinstance(data, dict):
        for value in data.values():
            result.extend(extract_strings(value))

    return result

def main():
    print(extract_strings(API_OUTPUT))
if __name__ == '__main__':
    main()