# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from . import seleniumscraper

HEADERS = {
    'User-Agent': 'acascrape - A python package used by Oxford University to scrape details of academics for our ChemBioHub project',
    'From': 'andrew.stretton@sgc.ox.ac.uk'  # This is another valid field
}



class AcaScraper():
    def get_soup(self, url):
        "Take a URL and crawl it using our user agent"
        resp = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.text)
        return soup


    def get_simple_profile(self, profile_url):
        return NotImplementedError


    def get_js_soup(self, profile_url):
        scraper = seleniumscraper.Selenium()
        scraper.get(profile_url)
        soup = BeautifulSoup(scraper.data)
        return soup



def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s.strip()



class ResearchGateScraper(AcaScraper):
    def get_simple_profile(self, profile_url):
        #Some simple stats and info about the user
        soup = self.get_soup(profile_url)
        parsed = {}
        labels = soup.findAll("div",class_="stats-label")
        stats = lis=soup.findAll("div",class_="stats-count")
        for index, label in enumerate(labels):
            if label.string:
                parsed[label.string.lower().strip()] = num(stats[index].string.strip())
        parsed["name"] = soup.find("title").string.strip()
        links = soup.findAll("a")
        for link in links:
            href =  link.get('href',"")

            if "institution" in href and "department" not in href:
                parsed["institution"] = link.string.strip()
            elif "department" in link.get("href", ""):
                parsed["department"] = link.string.strip()
                break

        topics = soup.findAll("a",class_="keyword-list-token-text")
        parsed["topics"] = [topic.string.strip() for topic in topics]
        profile_image = soup.find("img" ,{"title" :parsed["name"]}).get("src")
        if "profile_default" not in profile_image:
            parsed["profile_image"] = profile_image
        return parsed



class AcademiaEduScraper(AcaScraper):
    def get_simple_profile(self, profile_url):
        soup = self.get_js_soup(profile_url)
        parsed = {}
        parsed["name"] = soup.find("h1").string.strip()
        stats = soup.findAll("div",class_="count")
        print stats
        labels = soup.findAll("div",class_="label")[0:len(stats)]

        for index, label in enumerate(labels):
            if label.string:
                parsed[label.string.lower().strip()] = num(stats[index].string.strip())
        topics = soup.findAll("a", class_="research_interest_link")
        parsed["topics"] = [topic.string.strip() for topic in topics]

        links = soup.findAll("a")
        for link in links:
            href =  link.get('href',"")

            if 'academia.edu"' in href and "Department" not in href:
                parsed["institution"] = link.string.strip()
            elif "Department" in link.get("href", ""):
                parsed["department"] = link.string.strip()
                break
        profile_image = soup.find("img" ,{"id" :"profile_photo"}).get("src")
        if "no pattern was found"  not in profile_image:
            parsed["profile_image"] = profile_image

        return parsed



class MendeleyScraper(AcaScraper):
    def get_simple_profile(self,profile_url):
        soup = self.get_soup(profile_url)
        parsed = {}
        parsed["name"] = soup.find("h1").string.strip()
        total_journals = 0
        journals_total = soup.find("a",{"title" :"Show Publication"})
        if journals_total:
            total_journals= journals_total.string
            print total_journals
            total_journals =total_journals.split("(")[1].split(")")[0]
            total_journals = num(total_journals)

        topic_div = soup.find("a", {"name" :"research_interests"}).next_element.next_element
        topics = str(topic_div.string)
        if topics != "No research interests added yet.":
            parsed["topics"] = topics.split(",")
        else:
            parsed["topics"] = []
        parsed["stats"] = {"publications" : total_journals}

        profile_image = soup.find("img" ,{"class" :"photo-full"}).get("src")
        if "awaiting"  not in profile_image:
            parsed["profile_image"] = profile_image
        return parsed
