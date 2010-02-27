autobib
=======

This is a simple but time saving script that automatically creates a 
bibxtex bibliography from from your scientific papers, books or similar 
documents in pdf format. Parses the pdf-files in the given path and 
searches google scholar for bibtex info and creates a bibtex.bib file. 

Dependencies
------------
-    python
-    beautifulsoup
-    pdftotext 

Debian/Ubuntu install depedencies:
----------------------------------
To install depenencies on Debian and Ubuntu

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

