import json
import ssl
from urllib.request import urlopen

def main():
    article = input("Enter an article title: ")
    print(buildURL(article))

def buildURL(article):
    article = article.replace(' ', '%20')
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles="+article+"&rvprop=timestamp|user&rvlimit=30&redirects"

main()

