import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Israel"


# print(len(citations))


def get_citations_needed_count(cite):
    req = requests.get(url)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')
    citations = soup.find_all("sup", {"class": "noprint Inline-Template"})
    print(len(citations))




def get_citations_needed_report(new_url):
    req = requests.get(new_url)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')
    citations = soup.find_all("sup", {"class": "noprint Inline-Template"})
    citation_need = '\n\n'.join([citation.parent.text.strip() for citation in citations])
    print(citation_need)







get_citations_needed_count(url)
get_citations_needed_report(url)
