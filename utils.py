import json


def read_examples_from_json(examples: {}) -> [str]:
    return list(map(lambda s: s["text"], examples["examples"]))


def read_location_from_json() -> [[str]]:
    result_dict = {}
    # source: https://gist.github.com/duhaime/1d6d5a8dc77c86128fcc1a05a72726c9
    # british-cities-to-counties
    with open('resource/uk_cities.json') as f:
        location_dict = json.load(f)
        for city, county in location_dict.items():
            if county in result_dict:
                result_dict[county].append(city)
            else:
                result_dict[county] = [city]
    return list(result_dict.items())


if __name__ == '__main__':
    print(read_location_from_json())
