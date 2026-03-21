NAMES = ["Adam", "Stanisław", "Joanna", "Kornelia", "Kacper", "Adam"]

def generate_name_pairs(names:list[str]):
    """
        Generates unique pairs of names using index tracking and sorting.

        This function avoids duplicate pairs (e.g., [A, B] and [B, A])
        by storing already processed index pairs.
    """
    pairs = []
    indices_pairs = []
    for i, first_person in enumerate(names):
        for j, second_person in enumerate(names):
            indices_pair = sorted([i,j])
            pair = sorted([first_person, second_person])
            if i == j or indices_pair in indices_pairs:
                continue
            indices_pairs.append(indices_pair)
            pairs.append(pair)
    return pairs

def generate_names_v2(names:list[str]):
    """Generates all unique pairs of names without duplicates.

    Each pair is created only once (no reversed duplicates like [B, A]).
    Works correctly even if the same name appears multiple times,
    because pairing is based on indices, not values."""
    
    pairs = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pair = [names[i], names[j]]
            pairs.append(pair)
    return pairs


def main():
    print(generate_name_pairs(NAMES))
    print(generate_names_v2(NAMES))

if __name__ == "__main__":
    main()
