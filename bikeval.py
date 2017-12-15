#!/usr/bin/python

from lxml import html
from lxml.cssselect import CSSSelector
import requests

def main():

  page =  requests.get('https://denver.craigslist.org/search/bia?max_price=4000&min_price=800&query=%28trailfox%20%7C%20scale%20%7C%20spark%20%7C%20fuel%20%7C%20slash%20%7C%20remedy%20%7C%20works%20%7C%20enduro%20%7C%20epic%20%7C%20rhyme%20%7C%20kona%20%7C%20evil%20%7C%20ibis%20%7C%20juliana%20%7C%20pivot%20%7C%20niner%20%7C%20cruz%20%7C%20yeti%20%7C%20stumpjumper%20%7C%20camber%20%7C%20yt%29&sort=date&srchType=T')

  tree = html.fromstring(page.content)

  sel = CSSSelector('a.result-title.hdrlnk')

  results = sel(tree)
  bikes = {}
  for bike in results:
   print '-------------------------------------'
   print

   bikeurl =  bike.get('href')

   #add the byke to the list
   bikes[bikeurl] = parseByke(bikeurl)

def parseByke(bikeurl):
  # read the individual bike page, add it's data
  bikepage = requests.get(bikeurl)
  biketree = html.fromstring(bikepage.content)

main()
