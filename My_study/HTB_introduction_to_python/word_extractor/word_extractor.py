import requests
import re
from bs4 import BeautifulSoup


# getting the html code of the page
def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(
            f"HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting..."
        )
        exit(1)
    return resp.content.decode()


def word_slicer(resp):
    soup = BeautifulSoup(resp, "html.parser")
    raw_text = soup.get_text()
    return re.findall(r"\w+", raw_text)


def word_counter(words_list):
    words_count = {}
    for i in words_list:
        if i not in words_count:
            words_count[i] = 1
        else:
            words_count[i] += 1
    return words_count


url = "http://www.example.com"
url_HTB_exercise = "http://94.237.122.36:33847"
word_count = word_counter(word_slicer(get_html_of(url_HTB_exercise)))
# print(word_count)
top_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print([top_words[x] for x in range(5)])
top_words = [i[0] for i in top_words]
print(top_words[0])
