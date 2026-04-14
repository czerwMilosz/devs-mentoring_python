import json


def load_data(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def print_interface_status(data: dict) -> None:
    interfaces = data.get("imdata", [])

    print("Interface Status")
    print()
    print("=" * 78)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
    print("-" * 78)

    for item in interfaces:
        attributes = item.get("l1PhysIf", {}).get("attributes", {})

        dn = attributes.get("dn", "")
        description = attributes.get("descr", "")
        speed = attributes.get("speed", "")
        mtu = attributes.get("mtu", "")

        print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")


def main() -> None:
    data = load_data("data.json")
    print_interface_status(data)


if __name__ == "__main__":
    main()