Scripts for working with the Handbook.

# translate.py

This was a script for migrating content from the old system (restructured text / sphinx).

Two functions:

* `translate`: Take restructred text source files in english and use the
  translations in the po files to generate a translated source file (still in
  restructured text)
* `convert` Convert restructured text to markdown

Requirements:

* Install pandoc
* `pip install requirements.txt`

Tests: for tests to work you will need to run them in the opendatahandbook base directory.

----

Usage:

    # check out the old opendatahandbook repo into e.g. a parallel directory
    # then do
    python scripts/translate.py ../opendatahandbook ./

    # resulting output in ./en/guide/ ./de/guide/ ./{lang}/guide ...

