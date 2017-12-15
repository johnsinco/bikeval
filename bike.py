#!/usr/bin/python
from lxml import html
from lxml.cssselect import CSSSelector
import requests

class Bike:

    def __init__(self, biketree):
        self.parse_bike(biketree)

    # read the bike listing and parse it
    # should return a dictionary of the bike data
    def parse_bike(self, biketree):
        titleselector = CSSSelector("meta[property='og:title']")
        self.title = titleselector(biketree)

    def get_bike(bikeurl):
      # read the individual bike page, add it's data
      bikepage = requests.get(bikeurl)
      biketree = html.fromstring(bikepage.content)
      parse_bike(biketree)
