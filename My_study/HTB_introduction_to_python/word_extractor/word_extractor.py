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
    soup = BeautifulSoup(resp.content.decode(), "html.parser")
    raw_text = soup.get_text()
    print(re.findall(r"\$.", raw_text))
    return re.findall(r"\w+", raw_text)


def word_counter(words_list, Top_ten=False, Sorted=False):
    words_count = {}
    for i in words_list:
        if i not in words_count:
            words_count[i] = 1
        else:
            words_count[i] += 1
    if Top_ten:
        return sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:10]
    if Sorted:
        return [
            x[0]
            for x in sorted(words_count.items(), key=lambda item: item[1], reverse=True)
        ]
    return words_count


def main():
    url = "http://www.example.com"
    url = "http://83.136.249.223:39502"
    all_words = get_html_of(url)
    top_words = word_counter(all_words, Sorted=True)


if __name__ == "__main__":
    main()
