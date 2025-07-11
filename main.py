from icrawler.builtin import GoogleImageCrawler
import random 


num_of_raccoons = int(input("How many raccoons would you like: "))
download_location = input("Download location (use \"/\" ): ")

keywords = []
with open("RaccoonFinder/english-adjectives.txt", 'r') as file:
    for line in file:
        keywords.append(line.strip())

chosen_word = keywords[random.randint(0, len(keywords) - 1)]

search_term = f"{chosen_word} raccoon"

google_crawler = GoogleImageCrawler(storage={'root_dir': download_location})
google_crawler.crawl(filters= {'type': "photo"}, keyword= search_term, max_num= num_of_raccoons)