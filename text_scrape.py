import requests
from bs4 import BeautifulSoup

def get_scraped_text(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    whitelist = [
        'p',
        'blockquote'
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name :
            if t.parent.name in whitelist :
                output += '{} '.format(t)

    return(output)