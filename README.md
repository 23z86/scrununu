# scrununu
Web scrapper for kununu.com
State: in development
Imports: sys, lxml, os, requests
OS: Linux

file functions.py
------------------
Contains the functions.

file globals.py
------------------
Contains the vars like the xpaths and the url.

Description
------------------
This simple tool reads the data from kununu.com based on xPath.
At the moment not all elements are read out as the amout of data is pretty high.
In the current version the company name, rating title, date, stars, rating score and recommendation are read out.

Until now the UI has not been implemented, works fine from the terminal.
