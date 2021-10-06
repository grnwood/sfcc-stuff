#!/usr/bin/env python
import requests, sys
from bs4 import BeautifulSoup
import tempfile
import pdb

"""
Scrape the entire dumb SFCC marketplace site (which has no search?!?)
and find out if a vendor is listed or not (or search by topic).

Usage:
$ ./sfcc-partners.py {vendor name case insensitive}

    Example:
    $ ./sfcc-partners.py yotpo

    * Scraping page 9 pages.
    [*********]
    Yotpo empowers brands to grow direct-to-consumer business through experiences that sustain customer loyalty.

If the tagline in the horrible site exists it will show otherwise nothing
returns.  NOTE:  The data is bad so a tagline may not include the company
but in that case a topic could be used.

    $./sfcc-partners.py loyalty
    * Scraping page 9 pages.
    [*********]
    Annex Cloud delivers fully integrated Customer Loyalty, Referral Marketing, and User Generated Content solutions.
    Antavo is the leading customer loyalty tech for retail and fashion, creating experiences through Recognition Loyalty .
    Clutch is an innovative provider of Loyalty, Gift, Customer Intelligence, CRM, and Promotional Solutions.
    Clutch is the integrated platform powering the Next Generation of loyalty and gift solutions for Salesforce.
    Clyde is an end-to-end product protection platform that empowers retailers to drive revenue and increase loyalty.
    Data-driven ecommerce marketing right at your fingertips. For omnichannel campaigns that boost sales and drive loyalty.
    Yotpo empowers brands to grow direct-to-consumer business through experiences that sustain customer loyalty.
    Zinrelo is an enterprise-grade loyalty rewards platform designed for the needs of mid to large businesses.

At least you know there is a 'nameless' vendor out there and you can find it.
    or, fork this and fix it :).
"""
nextURL = 'https://www.salesforce.com/products/commerce-cloud/partner-marketplace._filter.x/'

def stripchars(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def extract_vendors(soupdata):
    buffer = []
    for x in soupdata.select('.event-pages-data'):
        for y in x.select('h2'):
            #breakpoint()
            buffer.append(y.select('.header-text')[0].text.strip())
    return buffer


# get # of pages
firstpage = requests.get(nextURL.replace('x','1'))
htmldata = firstpage.text
soup = BeautifulSoup(htmldata, 'html.parser')
pages = int(soup.select('#pageButtons')[0].attrs['data-total-pages'])

# get page data
pagedata = []
print('* Scraping page {end} pages.'.format(end=pages))
print ('[',end='')
for page in range(1,pages+1):
    nurl = nextURL.replace('x',str(page))
    page = requests.get(nurl)
    htmldata = page.text
    soup = BeautifulSoup(htmldata, 'html.parser')
    vendorinfo = extract_vendors(soup)
    for vend in vendorinfo:
        pagedata.append(vend)
    print('*',end='')
print (']')

tofind = 'Adyen'
if len(sys.argv) > 1:
    tofind = sys.argv[1]

for eachone in pagedata:
    if eachone.lower().find(tofind.lower()) >= 0:
        print(stripchars(eachone))







