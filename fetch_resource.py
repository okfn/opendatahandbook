from collections import defaultdict
import csv
import yaml
import requests


spreadsheet_url = 'https://docs.google.com/a/okfn.org/spreadsheets/d/1MVVxdfZJyW-WRxKMSPC3h6A13CdkycrHFwRkJcV7Og4/export?gid=0&format=csv'


def titleize(string):
    return string.lower().replace(' ', '_').replace(',', '')


if __name__ == '__main__':
    by_topic = defaultdict(list)
    r = requests.get(spreadsheet_url)
    for  row in csv.DictReader(r.iter_lines(), restkey='Notes'):
        extra = row.pop('', None)
        if extra:
            row['Notes'] = row['Notes'] + extra
        by_topic[row['Topic'].strip()].append(row)

    for topic, vs in by_topic.items():
        if topic == '':
            topic = 'no_topic'
            print 'Warning: "Topic" column contains an empty entry'
        with open('_data/resources/{0}.yaml'.format(titleize(topic)), 'w') as topic_file:
            yaml.dump(vs, topic_file, default_flow_style=False)
