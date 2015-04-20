import csv
import yaml
import requests


spreadsheet_url = 'https://docs.google.com/a/okfn.org/spreadsheets/d/1MVVxdfZJyW-WRxKMSPC3h6A13CdkycrHFwRkJcV7Og4/export?gid=0&format=csv'


def titleize(string):
    return string.lower().replace(' ', '_').replace(',', '')


if __name__ == '__main__':
    data = []
    r = requests.get(spreadsheet_url)
    for  row in csv.DictReader(r.iter_lines()):
        extra = row.pop('', None)
        if extra:
            row['Notes'] = ' '.join([row['Notes'],  extra])
        data.append(row)

    with open('_data/resources.yaml', 'w') as topic_file:
        yaml.dump(data, topic_file, default_flow_style=False)
