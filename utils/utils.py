import argparse
import json


def parse_input():
    parser = argparse.ArgumentParser(description='Get parcel status')
    parser.add_argument('id', type=str, help='Valid parcel id')
    return parser.parse_args()


def load_config():
    with open('config.json') as file:
        return json.load(file)
