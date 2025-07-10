from icrawler.builtin import GoogleImageCrawler
import random

num_of_raccoons = int(input("How many raccoons would you like: "))
download_location = input("Download location (use \"/\" ): ")

keyWords = ["funny", "weird", "dumb", "goofy", "silly", "cute", "adorable"]
chosen_word = keyWords[random.randint(0, len(keyWords) - 1)]
randomizer = random.randint(0, 1000)
search_term = f"{chosen_word} raccoon 5{randomizer}"

google_crawler = GoogleImageCrawler(storage={'root_dir': download_location})
google_crawler.crawl(filters= {'type': "photo"}, keyword= search_term, max_num= num_of_raccoons)