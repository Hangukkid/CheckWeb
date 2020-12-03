
import requests 
from bs4 import BeautifulSoup 

URLs = ["https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H/ref=as_li_ss_tl?dchild=1&keywords=ps5&qid=1605140418&sr=8-2&linkCode=sl1&tag=ps5sa01-20&linkId=8375cd77f565aba3e48e536be4790ec5&language=en_CA",
"https://www.ebgames.ca/PS5/Games/877522/playstation-5", 
"https://www.walmart.ca/en/ip/playstation-5-console-plus-extra-dualsense-wireless-controller/6000201790922",
"https://www.walmart.ca/en/ip/playstation5-digital-edition/6000202198823",
"https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185"
]

for url in URLs:
    r = None
    try: 
        r = requests.get(url, timeout=10)
    except requests.exceptions.Timeout as err:
        print(err)

    if (not r):
        continue
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    # print(soup.prettify()) 
    available = soup.find('div', attrs={'id': 'qualifiedBuybox'})
    if (available):
        print(url)
