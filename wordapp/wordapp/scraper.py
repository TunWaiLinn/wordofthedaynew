import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import wordnet


# URL of the Merriam-Webster "Word of the Day" page
url = "https://www.merriam-webster.com/word-of-the-day"


# Send an HTTP GET request to the website
def scrape_word_of_the_day():
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the element that contains the "Word of the Day"
        word_of_the_day = soup.find("h2", class_="word-header-txt")

        if word_of_the_day:
            # Extract and print the "Word of the Day"
            word = word_of_the_day.text.strip()
            print("Word of the Day:", word)
            return word
        else:
            return "Word of the Day not found on the page."

    return print("Failed to retrieve the webpage. Status code:", response.status_code)


def get_word_details():
    word = scrape_word_of_the_day()

    synsets = wordnet.synsets(word)

    if not synsets:
        return 'Word not found in WordNet', ''

    # Get the first synset (sense) of the word
    first_synset = synsets[0]
    definition = first_synset.definition()
    usage_sentences = first_synset.examples()

    return word, definition, '\n'.join(usage_sentences)
