#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_acascraper
----------------------------------

Tests for `acascraper` module.
"""

import unittest

from acascraper import acascraper
from acascraper import seleniumscraper


class TestAcascraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_simple_profile_researchgate(self):
        url = "https://www.researchgate.net/profile/Andrew_Stretton2"
        parser = acascraper.ResearchGateScraper()
        data = parser.get_simple_profile(url)
        print data

    def test_get_simple_profile_academia(self):
        url = "https://pdx.academia.edu/CameronMSmith"
        parser = acascraper.AcademiaEduScraper()
        data = parser.get_simple_profile(url)
        print data



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()