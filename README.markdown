autobib
=========

This is a simple script to automatically create a bibxtex file
for bibliography from research papers etc. in pdf format. Parses 
all pdf-files in the given path and use google scholar to get 
bibtex info that is written to bibtex.bib. 

Dependencies
------------
-    python 2.5
-    BeautifulSoup
-    pdftotext

Running
-------
To run the program
    $ python autobib.py <path to your pdf's>

Installing
----------
To install autbib globally you need to run the setup script

    $ sudo python setup.py install

Once installed, run the program like this:

    $ autobib <path to your pdf's>

Author
------
Joacim Alvergren <joacim.alvergren@gmail.com>

