import re
from bs4 import BeautifulSoup
import whois
import requests
import json



class ProductsScraper():

    #def __init__(self):

    def constructLinkAmazon(self, searchterm):
        searchitem_parsed = ("+").join(searchterm.split("."))
        return f"https://www.amazon.es/s?k={searchitem_parsed}"

    def constructLinkECI(self, searchterm):
        searchitem_parsed = ("%20").join(searchterm.split("."))
        return f"https://www.elcorteingles.es/search/?s={searchitem_parsed}"
        
    def scrapping(self, searchterm):
        link_amazon = self.constructLinkAmazon(searchterm)
        link_eci = self.constructLinkECI(searchterm)

        # Get Amazon products as a dataset

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
            */*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8",
            "Cache-Control": "no-cache",
            "dnt": "1",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
            37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        #r = requests.get("http://www.example.com", headers=headers)

        my_cookie = {
            "version":0,
            "name":'COOKIE_NAME',
            "value":'true',
            "port":None,
            # "port_specified":False,
            "domain":'www.mydomain.com',
            # "domain_specified":False,
            # "domain_initial_dot":False,
            "path":'/',
            # "path_specified":True,
            "secure":False,
            "expires":None,
            "discard":True,
            "comment":None,
            "comment_url":None,
            "rest":{},
            "rfc2109":False
            }

        session = requests.Session()
        session.cookies.set(**my_cookie)

       
        #session.cookies.set("COOKIE_NAME", "the cookie works", domain="www.amazon.es")
        #session.post(link_amazon, data=dict(
        #    email="meaow@gmail.com",
        #    password="secret_value_pw"
        #))

        #try:
        page = session.get(link_amazon, headers=headers)
        #if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="html.parser")

        #data = soup.find("span", attrs={"class": 'a-size-base-plus'})
 
        products = soup.find_all('span', attrs={"class": 'a-size-base-plus'})

        prices = soup.find_all('span', attrs={"class": 'a-price-whole'})

        prod_data = soup.find_all('div', attrs={"class": 's-card-container'})
        # s-overflow-hidden aok-relative s-expand-height s-include-content-margin s-latency-cf-section s-card-border"
        

        json_l = []
        json_p = []

        f = open("amazon_test.html", "w", encoding='utf8')
        for pd in prod_data:
            f.write("-----CHILDREN BATCH")
            for ch in pd.children:
                f.write(str(ch))
        #for s in products:
        #    json_l.append({
        #        "product": s.string
        #    })
        #for p in prices:
        #    json_p.append({
        #        "price": p.string
        #    })
        #    f.write(json.dumps(json_l, ensure_ascii=False))
        #    f.write(json.dumps(json_p, ensure_ascii=False))
        f.close()
