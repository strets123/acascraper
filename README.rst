===============================
Acascraper
===============================

.. image:: https://badge.fury.io/py/acascraper.png
    :target: http://badge.fury.io/py/acascraper
    
.. image:: https://travis-ci.org/strets123/acascraper.png?branch=master
        :target: https://travis-ci.org/strets123/acascraper

.. image:: https://pypip.in/d/acascraper/badge.png
        :target: https://pypi.python.org/pypi/acascraper


Academic social network scraper package

* Free software: BSD license
* Documentation: http://acascraper.rtfd.org.

Features
--------

The acascraper can read data from academia based social networks.

Currently covers profile URLs on researchgate.net and academia.edu.

Academia.edu requires the firefox browser, this can be installed on Centos as follows:

	yum install xorg-x11-server-Xvfb
	yum install firefox


Firefox is run in headless mode using the xvfb package so that we can browse to the website in an automated way and pull down the profile information. Selenium is used to initiate the browser but the whole selenium package is not required.

