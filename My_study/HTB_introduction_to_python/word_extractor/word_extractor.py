import requests
import re
import click
from bs4 import BeautifulSoup


# getting the html code of the page
def get_html_of(url, length):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(
            f"HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting..."
        )
        exit(1)
    soup = BeautifulSoup(resp.content.decode(), "html.parser")
    raw_text = soup.get_text()
    return re.findall(r"\b\w{%d,}\b" % length, raw_text)


def word_counter(words_list, Sorted=False):
    words_count = {}
    for i in words_list:
        if i not in words_count:
            words_count[i] = 1
        else:
            words_count[i] += 1
    if Sorted:
        return [
            x[0]
            for x in sorted(words_count.items(), key=lambda item: item[1], reverse=True)
        ]
    return words_count


@click.command()
@click.option(
    "--url", "-u", prompt="Web_URL", help="The url to fetch and extract words from."
)
@click.option(
    "--length", "-l", default=0, help="Set the min length for the words default is 0."
)
@click.option("--count", "-c", default=1, help="specify the amount of the urls")
def main(url, length, count):
    all_words = get_html_of(url, length)
    top_words = word_counter(all_words, Sorted=True)
    top_words = top_words[1:]
    print(top_words)


if __name__ == "__main__":
    main()
