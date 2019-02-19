import requests

def random_quote():
   url='http://quotes.stormconsultancy.co.uk/random.json'
   blockquote= requests.get(url)
   quote= blockquote.json()
   return quote