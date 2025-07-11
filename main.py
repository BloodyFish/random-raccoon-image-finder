from icrawler.builtin import GoogleImageCrawler
import random 
import os


num_of_raccoons = int(input("How many raccoons would you like: "))
download_location = input("Download location (use \"/\" ): ")

script_dir = os.path.dirname(__file__)  # directory of the running script
file_path = os.path.join(script_dir, "english-adjectives.txt")

keywords = []
with open(file_path, 'r') as file:
    for line in file:
        keywords.append(line.strip())

chosen_word = keywords[random.randint(0, len(keywords) - 1)]

search_term = f"{chosen_word} raccoon"

google_crawler = GoogleImageCrawler(storage={'root_dir': download_location})
google_crawler.crawl(filters= {'type': "photo"}, keyword= search_term, max_num= num_of_raccoons)