import os
import io
import shutil


def run():

    guide_pages = []
    glossary_pages = []

    for root, dirs, files in os.walk('guide'):
        all_paths = [os.path.join(root, f) for f in files if f.endswith('.md')]
        guide_pages.extend(all_paths)

    for root, dirs, files in os.walk('glossary'):
        all_paths = [os.path.join(root, f) for f in files if f.endswith('.md')]
        glossary_pages.extend(all_paths)

    for filepath in guide_pages:

        tmp_filepath = filepath + '.tmp'

        with io.open(filepath, mode='r+t', encoding='utf-8') as stream, io.open(tmp_filepath, mode='w+t', encoding='utf-8') as out:

            root, ext = os.path.splitext(filepath)
            parts = root.split('/')
            if len(parts) == 3:
                namespace, lang, index = root.split('/')
                basename = None
                redirect_from = '/'.join([lang, 'index.html'])
            else:
                namespace, lang, basename, index = root.split('/')
                redirect_from = '/'.join([lang, basename, 'index.html'])

            print redirect_from

            next(stream)
            content = stream.read()
            addition = '---\nredirect_from: /{0}\n'.format(redirect_from)
            out.write(addition + content)

        shutil.copy2(tmp_filepath, filepath)
        os.remove(tmp_filepath)

    for filepath in [g for g in glossary_pages if not '/terms/' in g]:

        tmp_filepath = filepath + '.tmp'

        with io.open(filepath, mode='r+t', encoding='utf-8') as stream, io.open(tmp_filepath, mode='w+t', encoding='utf-8') as out:

            root, ext = os.path.splitext(filepath)
            parts = root.split('/')
            namespace, lang, index = root.split('/')
            redirect_from = '/'.join([lang, namespace + '.html'])

            print redirect_from

            next(stream)
            content = stream.read()
            addition = '---\nredirect_from: /{0}\n'.format(redirect_from)
            out.write(addition + content)

        shutil.copy2(tmp_filepath, filepath)
        os.remove(tmp_filepath)


if __name__ == '__main__':
    run()
