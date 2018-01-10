import time

from factories import driver_factory
from utils import *


def check_parcel_status(parcel_id, url, driver):
    with driver as d:
        d.get('https://{url}'.format(url=url))
        input_field = d.find_element_by_id('ItemCode')
        input_field.send_keys(parcel_id)

        d.find_element_by_id('btn-ItemCode').click()
        time.sleep(2)

        if 'error' in input_field.get_attribute('class'):
            return 'incorrect parcel number'

        return d.find_element_by_id('dyntable').text


def main():
    args = parse_input()
    config = load_config()
    driver = driver_factory(config['driver'])
    print(check_parcel_status(parcel_id=args.id, url=config['url'], driver=driver))


if __name__ == '__main__':
    main()
