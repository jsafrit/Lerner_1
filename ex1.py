from collections import defaultdict


def trip_report(log):
    sorted_countries = sorted(log.keys())
    for visited_country in sorted_countries:
        print(visited_country)
        for visited_city in sorted(log[visited_country]):
            print('\t{}'.format(visited_city))


if __name__ == '__main__':
    travel_log = defaultdict(list)

    while True:
        place = input('Tell me where you went: ')
        if not place:
            break
        if ',' in place:
            city, country = place.split(',', maxsplit=1)
            travel_log[country.strip()].append(city.strip())
        else:
            print("That's not a legal city, state combination")

    trip_report(travel_log)
