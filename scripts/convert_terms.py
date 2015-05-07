import os
import io
import re
import shutil


def run():

    lookup = {}

    files_to_mine = []
    files_to_act_on = []

    for root, dirs, files in os.walk('glossary'):
        all_paths = [os.path.join(root, f) for f in files
                     if f.endswith('.md') and 'terms' in root]
        files_to_mine.extend(all_paths)

    for root, dirs, files in os.walk('guide'):
        all_paths = [os.path.join(root, f) for f in files if f.endswith('.md')]
        files_to_act_on.extend(all_paths)

    for root, dirs, files in os.walk('glossary'):
        all_paths = [os.path.join(root, f) for f in files if f.endswith('.md')]
        files_to_act_on.extend(all_paths)

    for source in files_to_mine:
        _path, ext = os.path.splitext(source)
        slug = '/{0}/'.format(os.path.dirname(_path))
        with io.open(source, mode='r+t', encoding='utf-8') as stream:
            for line in stream:

                # leaving this, but we are actually going to use language in
                # the file we act on, so that glossary links always go to the
                # current language, even if the term itself is not translated
                # when it is used
                # eg: if a ch_TW page has a term "open data", link to
                # /glossary/ch_TW/terms/open-data/ and not /glossary/en/terms/open-data/

                if line.startswith('lang:'):
                    lang = line.split(': ')[1].rstrip('\n')

                elif line.startswith('title:'):
                    title = line.split(': ')[1].lower().rstrip('\n')

        lookup.update({
            title: {
                'slug': slug,
                'lang': lang
            }
        })

    current_pattern = '({term:(.+?)})'
    new_pattern = '[{0}]({1})'

    # also was run with this, to catch newer stuff that didn't use terms:
    # current_pattern = '( {(.+?)})'
    # new_pattern = ' [{0}]({1})'

    for filepath in files_to_act_on:

        tmp_filepath = filepath + '.tmp'

        with io.open(filepath, mode='r+t', encoding='utf-8') as stream, io.open(tmp_filepath, mode='w+t', encoding='utf-8') as out:

            lang = None

            for line in stream:

                if line.startswith('lang:'):
                    lang = line.split(': ')[1].rstrip('\n')

                matches = re.findall(current_pattern, line)
                for m in matches:
                    if lookup.get(m[1].lower()):
                        print 'IN THIS FILE ::'
                        print filepath
                        print '\nthis current line ::'
                        print line

                        assumed_slug = lookup[m[1].lower()]['slug']
                        if lang not in assumed_slug:
                            # use the actual language of the file we are acting on
                            parts = assumed_slug.split('/')
                            parts[2] = lang
                            slug = '/'.join(parts)
                        else:
                            slug = assumed_slug
                        will_replace = new_pattern.format(m[1], slug)
                        line = re.sub(m[0], will_replace, line)

                        print 'becomes this new line ::'
                        print line

                out.write(line)
        shutil.copy2(tmp_filepath, filepath)
        os.remove(tmp_filepath)


if __name__ == '__main__':
    run()
