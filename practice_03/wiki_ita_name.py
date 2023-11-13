from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import json


# First, the most straightforward way to get data from wikipedia is using wikipedia lib
# However, I don't know why it didn't work on my computer. It always returns wrong pages.
# page = wikipedia.page('https://en.wikipedia.org/wiki/Paolo') # it returns the page Paulo, not Paolo
# page = wikipedia.page(pageid=2010558)
# Therefore, I use BeautifulSoup to scrap it.

def get_page_data(wiki_url):
    """
    Retrieves and parses the HTML content of a Wikipedia page given its URL.
    :param wiki_url: (str): The URL of the Wikipedia page to be fetched and parsed.
    :return: BeautifulSoup: A BeautifulSoup object representing the parsed HTML content of the page.
    """

    req = Request(url=wiki_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                                 '(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36')
    with urlopen(req, timeout=5) as w:
        text = w.read()
    soup = BeautifulSoup(text, 'html.parser')
    return soup


def extract_info(soup, save_path):
    """
    The function finds all <li> tags in the provided BeautifulSoup object, filters out unwanted
    elements, and extracts relevant information such as wiki URL, name, year of birth, year of death,
    nationality, and profession. The extracted information is then saved in a JSON file.

    :param soup: (BeautifulSoup): The BeautifulSoup object containing the HTML content.
    :param save_path: (str): The file path to save the extracted information in JSON format.
    :return: None, just save the file
    """

    # Find the <li> tag
    li_tags = soup.find_all('li')

    # Initialize an empty list to store all extracted info
    all_records = []

    # Loop through each <li> tag and find all target elements within it
    for li_tag in li_tags:
        if str(li_tag).startswith('<li><a href="/wiki/') and '/wiki/Category:' not in str(li_tag):
            record = dict()
            record['wiki_url'] = li_tag.find('a').get('href')
            record['name'] = li_tag.find('a').get('title')
            # record['text'] = li_tag.text

            # (2001- | (born 987 | (born late 1700 | (c. 1234
            birth_pattern = r'\(\d{1,4}–|\(born \d{1,4}|\(born late \d{1,4}|\(c\..\d{1,4}'
            birth_found = re.findall(birth_pattern, li_tag.text)
            if birth_found:
                yob = int(re.findall(r'\d+',birth_found[0])[0])
            else:
                yob = None
            # - 1982) | (died 1932 | (died c. 400
            death_pattern = r'–.*\d{1,4}\)|\(died \d{1,4}|\(died c.+\d{1,4}'
            death_found = re.findall(death_pattern, li_tag.text)
            if death_found:
                yod = int(re.findall(r'\d+', death_found[0])[0])
            else:
                yod = None
            record['year_birth'] = yob
            record['year_death'] = yod

            # just accept the simple pattern that the first word after comma is the nationality
            # and all the text after that is the profession
            description = li_tag.text.split(',')[1].strip()
            record['nationality'] = description.split(' ')[0]
            record['profession'] = ' '.join(description.split(' ')[1:])

            all_records.append(record)

    # save file in JSON format
    with open(save_path, "w", encoding='utf-8') as f:
        json.dump(all_records, f, ensure_ascii=False, indent=4)


def download_images(wiki_url):
    # read the json file, select wiki url only, put them in a list
    # iterate over the wiki url list, request the page
    # look for the image url pattern in the infobox, put the image url in a list
    # download the image, save it in a directory
    # if the image is not found, assign a none value in the image list
    # write the pair (wiki_url, image_url) in another json file
    pass


if __name__ == '__main__':
    soup = get_page_data(wiki_url='https://en.wikipedia.org/wiki/Paolo')
    extract_info(soup=soup, save_path='./results/data_Paolo.json')
