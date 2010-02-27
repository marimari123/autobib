autobib
=========

This is a simple but time saving script to automatically create a 
bibxtex bibliography from from scientific papers etc. in pdf 
format. Parses pdf-files in the given path and search google 
scholar for bibtex info and creates a bibtex.bib. 

Dependencies
------------
-    python
-    BeautifulSoup
-    pdftotext 

Debian/Ubuntu install depedencies:
----------------------------------
    $ sudo apt-get install poppler-utils python-beautifulsoup

Running
-------
To run the program
    $ python autobib.py <path to your pdf's>

Installing
----------
To install autobib globally you need to run the setup script

    $ sudo python setup.py install

Once installed, run the program like this:

    $ autobib <path to your pdf's>

Author
------
Joacim Alvergren <joacim.alvergren@gmail.com>

