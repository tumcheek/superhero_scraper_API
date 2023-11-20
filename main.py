import requests
from utils import get_hero_by_id, write_hero_info_to_csv
from scraper import process_hero_response

if __name__ == '__main__':
    hero_numbers = int(input('number of heroes='))
    start_from = int(input('start='))
    csv_name = input('csv file name=')
    for hero_number in range(start_from, hero_numbers + start_from):
        try:
            hero_info = process_hero_response(get_hero_by_id(hero_number))
            write_hero_info_to_csv(hero_info, csv_name)

        except requests.exceptions.HTTPError as err:
            print(err)
            break
    print('All data saved to csv')

