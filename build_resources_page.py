import argparse
import getpass
import gspread



#def to_markdown_table(worksheet):
#    for row_number, rows in enumerate(worksheet):
#        yield u'|' + u'|'.join(rows) + u'|\n'
#        if row_number == 0:
#            yield u'|-' * len(rows) + u'|\n'

def linkify(string):
    '''Returns an html link if it starts with http/https'''
    if string.startswith('http'):
        return u'<a href="{0}">{0}</a>'.format(string)
    else:
        return string


def to_html_table(worksheet):
    yield '<table>\n'
    for row_number, rows in enumerate(worksheet):
        if row_number == 0:
            yield u'<tr>\n'
            for col in rows:
                col = linkify(col)
                yield u'<th>{0}</th>\n'.format(col)
        else:
            yield u'<tr>\n'
            for col in rows:
                col = linkify(col)
                yield u'<td>{0}</td>\n'.format(col)
    yield '</table>'

parser = argparse.ArgumentParser(description='Convert "Resources for the library" google doc into html')
parser.add_argument('google_apps_email', help='google apps email address', action='store')
args = parser.parse_args()

scope = ['https://spreadsheets.google.com/feeds', 'https://docs.google.com/feeds']
password = getpass.getpass('Enter you google account password: ')

print 'Logging into google docs'
gc =  gspread.login(args.google_apps_email, password)

print 'Fetching Google doc spreadsheet'
spreadsheet = gc.open_by_key('1MVVxdfZJyW-WRxKMSPC3h6A13CdkycrHFwRkJcV7Og4')
worksheet = spreadsheet.sheet1

print 'Writing doc to html file'
markdown = to_html_table(worksheet.get_all_values())
with open('_includes/resources.html', 'w') as f:
    for line in markdown:
        f.write(line.encode('utf-8'))

print 'Done.'
