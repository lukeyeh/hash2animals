import sys
import json
import hashlib


def get_animal_names(filename="animals.json"):
    return json.load(open(filename))['animals'][:128]


def number_to_animal(animals):
    return {i: animals[i] for i in range(128)}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("not enough arguments")
        sys.exit(0)

    message = sys.argv[1]
    m = hashlib.sha256()
    m.update(message.encode('utf-8'))

    animals = get_animal_names()
    n_to_a = number_to_animal(animals)
    for byte in m.digest()[:3]:
        print(n_to_a[byte & 0b01111110])
