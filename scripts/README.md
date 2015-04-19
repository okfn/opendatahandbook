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

----

