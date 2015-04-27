import csv
import requests
from slugify import slugify
import yaml


spreadsheet_url = 'https://docs.google.com/a/okfn.org/spreadsheets/d/1MVVxdfZJyW-WRxKMSPC3h6A13CdkycrHFwRkJcV7Og4/export?gid=0&format=csv'


def titleize(string):
    return string.lower().replace(' ', '_').replace(',', '')


if __name__ == '__main__':
    data = []
    r = requests.get(spreadsheet_url)
    for i, row in enumerate(csv.DictReader(r.iter_lines())):
        extra = row.pop('', None)
        if extra:
            row['Notes'] = ' '.join([row['Notes'],  extra])
        data.append(row)

        title = slugify(unicode(row['Title']))
        file_name ='_resources/{0}-{1}.yaml'
        with open(file_name.format(i, title), 'w') as resource_file:
            resource_file.write('---\n')
            resource_file.write(yaml.dump(row, default_flow_style=False))
            resource_file.write('---')
