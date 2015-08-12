import polib
import os
import shutil
import codecs
import subprocess
import re

###########################################
# Translate

def info(lang):
    fp = 'translation/%s/LC_MESSAGES/all.po' % lang

    po = polib.pofile(fp)
    print po.percent_translated()
    entries = po.translated_entries()
    print entries[0].msgid
    print entries[0].msgstr


def translate(instr, po_entries_sorted):
    '''
    Algorithm:

    Sort translation msgids from longest to shortest so that we match larger
    segments before shorter segments.

    for each msgid:
        do simple find and replace on source using msgid and msgstr

    Adjustment:

    Problem: pofile and source file may break lines at different lengths
    meaning a simple find and replace will not work

    we can use structure of pofile source which is that sphinx breaks msgid
    paragraph so we always know that a msgid in pofile will never be more than
    a paragraph.  We can therefore split source file by paragraph and do
    matching that way
    '''
    paras = instr.split('\n\n')
    outparas = []
    nomatch = []
    for para in paras:
        out = match_paragraph(para, po_entries_sorted)
        if out == para:
            nomatch.append(para)
        outparas.append(out)
    outstr = '\n\n'.join(outparas)
    if len(nomatch) > 0:
        print('Failed to match %s paragraphs' % len(nomatch))
    return outstr

def match_paragraph(para, po_entries_sorted):
    for entry in po_entries_sorted:
        out = para.replace(entry.msgid, entry.msgstr)
        if out != para:
            return out
        # no match so eliminate line breaks and try replace again
        # also eliminate leading spaces - esp relevant where we have bullet
        # points e.g.
        # * xxxx
        #   xxxx
        else:
            tmp = re.sub(r'\s+', ' ', para)
            msgid = entry.msgid.replace('\n', ' ').replace('  ', ' ')
            out = tmp.replace(msgid, entry.msgstr)
            if out != tmp: # we had a match
                return out
            else: # reset out to para
                out = para
    return out
    
def get_po_entries(lang, basepath=''):
    path = '%stranslation/%s/LC_MESSAGES/all.po' % (basepath, lang)
    po = polib.pofile(path)
    entries = po.translated_entries()
    def comparator(x,y):
        return cmp(len(x.msgid), len(y.msgid))
    newentries = sorted(entries, comparator, reverse=True)
    return newentries

def translate_all(lang, source, dest):
    poentries = get_po_entries(lang)
    files = get_all_source_files(source)
    for path in files:
        fullpath = os.path.join(source, path)
        fo = codecs.open(fullpath, encoding='utf8')
        out = translate(fo.read(), poentries)
        destpath = os.path.join(dest, os.path.splitext(path)[0] + '.md')
        parentdir = os.path.dirname(destpath)
        if not os.path.exists(parentdir):
            os.makedirs(parentdir)
        with codecs.open(destpath, 'w', encoding='utf8') as fout:
            fout.write(out)

###########################################
# Convert to Markdown

def convert_to_markdown(instr):
    # first process :term:`....` so that they do not get removed by pandoc
    instr = re.sub(r':term:`([^`]*)`', r'{term:\1}', instr)
    # now do ref
    # :ref:`this previous section <what-data-can-be-open>`.
    # note there is in fact only one ref in the entire source so we hard code
    # the link
    # instr = re.sub(r':ref:`([^<]*) <([^`]*)>`', r'[\1](#\2)', instr)
    instr = re.sub(r':ref:`([^<]*) <([^`]*)>`', r'[\1](../what-is-open-data/)', instr)

    # special hack
    instr = re.sub(r':doc:`(.*) <introduction/index.html>`', r'[\1](introduction/)', instr)

    # finally extend rst heading lines to fix fact that with translation some
    # headings may extnend beyond their heading line which messes up pandoc

    for char in ['=', '-', '~']:
        instr = re.sub(char * 5 + '*', char * 100, instr)

    PANDOC_PATH = '/usr/local/bin/pandoc'
    p = subprocess.Popen(
        [PANDOC_PATH,
            '--from=%s' % 'rst',
            '--to=%s' % 'markdown',
            '--atx-headers',
            '--no-wrap'
        ],
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE
    )
    instr = instr.encode('utf8')
    output = p.communicate(instr)[0]
    output = output.decode('utf8')

    # ok now let's clean stuff up

    # pandoc seems to have many spaces for bullet points e.g. -   Now my bullet
    # NOTE: we disable at present since we would need to unindent whole
    # paragraph and that is not easy
    # output = output.replace('-   ', '- ')
    # output = output.replace(':   ', ': ')
    return output


###########################################
# Bulk processing 

def get_all_source_files(basepath):
    allthefiles = []
    for dirname, subdirs, files in os.walk(basepath):
        if '/_' in dirname:
            continue
        files = [ os.path.join(dirname, f)[len(basepath):].lstrip('/') for f in files if f.endswith('.rst') ]
        allthefiles.extend(files)
    return allthefiles


langs = [
    'de',
    'el',
    'en',
    'es',
    'fr',
    'he',
    'hr',
    'id',
    'is',
    'it',
    'ja',
    'ko',
    'lt',
    'lv',
    'nl_BE',
    'pt_BR',
    'ro',
    'ru',
    'zh_CN',
    'zh_TW'
    ]


DEBUG = False
def run_it_all(handbookdir, dest):
    source = os.path.join(handbookdir, 'source')
    files = get_all_source_files(source)
    for lang in langs:
        print('Processing language: %s' % lang)
        poentries = get_po_entries(lang, handbookdir.rstrip('/') + '/') if lang != 'en' else None

        for path in files:
            fullpath = os.path.join(source, path)
            fo = codecs.open(fullpath, encoding='utf8')

            out = translate(fo.read(), poentries) if lang != 'en' else fo.read()
            
            if DEBUG:
                # write trans
                destpath = os.path.join(dest, lang, os.path.splitext(path)[0] + '.rst')
                parentdir = os.path.dirname(destpath)
                if not os.path.exists(parentdir):
                    os.makedirs(parentdir)
                with codecs.open(destpath, 'w', encoding='utf8') as fout:
                    fout.write(out)

            # write markdown
            out = convert_to_markdown(out)

            # final tweak to put in jekyll headings
            out = out.strip()
            lines = out.split('\n')
            out = '---\ntitle: %s\n---\n' % lines[0].replace('# ', '')
            out += '\n'.join(lines[1:])

            destpath = os.path.join(dest, lang, 'guide', os.path.splitext(path)[0] + '.md')
            parentdir = os.path.dirname(destpath)
            if not os.path.exists(parentdir):
                os.makedirs(parentdir)
            with codecs.open(destpath, 'w', encoding='utf8') as fout:
                fout.write(out)



###########################################
# Tests

class TestItAll(object):
    def test_get_po_entries(self):
        entries = get_po_entries('de')
        assert len(entries) > 300
        assert len(entries[0].msgid) > len(entries[1].msgid)

    def test_match_paragraph(self):
        para = \
'''**This handbook discusses the legal, social and technical aspects of 
open data.** It can be used by anyone but is especially 
designed for those seeking to **open up** data. It discusses the 
**why, what and how** of open data -- why to go open, what open is, 
and the how to 'open' data.'''
        entries = get_po_entries('de')
        out = match_paragraph(para, entries)
        assert out.startswith('**Dieses Handbuch'), out

    def test_match_paragraph_2(self):
        entries = get_po_entries('de')
        para = '''Table of Contents
================='''
        exp = '''Inhaltsverzeichnis
================='''
        out = match_paragraph(para, entries)
        assert out == exp, out

    def test_match_paragraph_3(self):
        entries = get_po_entries('de')
        para = '''2. **Apply an open license.**'''
        exp = '''2. **Vergeben sie eine offene Lizenz.**'''
        out = match_paragraph(para, entries)
        assert out == exp, out

    def test_translate(self):
        fpath = 'source/index.rst'
        entries = get_po_entries('de')
        out = translate(codecs.open(fpath, encoding='utf8').read(), entries)
        assert out
        assert '**Dieses Handbuch' in out, out

    def test_translate_2(self):
        fpath = 'source/how-to-open-up-data/index.rst'
        entries = get_po_entries('de')
        out = translate(codecs.open(fpath, encoding='utf8').read(), entries)
        assert 'Halten sie es einfach' in out, out[:500]
        assert "**Vergeben sie eine offene Lizenz.**" in out, out

    def test_get_all_source_files(self):
        out = get_all_source_files('source')
        assert 'index.rst' in out, out
        assert 'introduction/index.rst' in out
    
    def test_translate_all(self):
        testdir = '/tmp/handbook-translate'
        if os.path.exists(testdir):
            shutil.rmtree(testdir)
        os.makedirs(testdir)
        translate_all('de', 'source', testdir)
        indexpath = os.path.join(testdir, 'index.md')
        assert os.path.exists(indexpath), indexpath
        content = open(indexpath).read()
        assert 'Das Open Data Handbuch' in content, content
    
    def test_convert_to_markdown(self):
        instr = \
'''
Make Data Available
===================

Thus, **if you are planning to make your data available you should put a
license on it** - be `open`_ as we do.

.. _open: http://opendefinition.org/
.. _Open Definition: open_

Use the `Open Definition`_ and marked as suitable.

* http://opendatacommons.org/guide/

:term:`Open data` needs to be technically open as well as legally open.
:term:`machine-readable` format.

Available
  Data should be priced at no more than a reasonable cost of reproduction.

see :ref:`this previous section <what-data-can-be-open>`.

see :doc:`Einfuhrung <introduction/index.html>`

Inhaltsverzeichnis
================= 
'''
        exp = \
'''# Make Data Available

Thus, **if you are planning to make your data available you should put a license on it** - be [open](http://opendefinition.org/) as we do.

Use the [Open Definition](open_) and marked as suitable.

-   <http://opendatacommons.org/guide/>

{term:Open data} needs to be technically open as well as legally open. {term:machine-readable} format.

Available

:   Data should be priced at no more than a reasonable cost of reproduction.

see [this previous section](../what-is-open-data/).

see [Einfuhrung](introduction/)

# Inhaltsverzeichnis
'''
        import difflib
        d = difflib.Differ()
        out = convert_to_markdown(instr)
        assert out == exp, '\n'.join(d.compare(exp.split('\n'), out.split('\n')))


import sys
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python translate.py handbook-dir dest')
    run_it_all(sys.argv[1], sys.argv[2])

