import requests

endpoint= "https://api.datamuse.com/words?rel_jjb=ocean"

response= requests.get(endpoint)

data= response.json()

if response.status_code == 200:
    for item in data:
        getting_score= item.get("score")
        if getting_score > 950:
            print(item.get("word"))

#OUTPUT:
# open
# great
# vast
# deep
# western
# atlantic
# wide
# indian
# blue
# southern
# eastern
# whole
# mighty
# boundless
# tropical
# northern
# broad
# dark
# stormy
# infinite
# entire
# central
# upper
# equatorial
# inter
# north
# coastal
# distant
# unknown
# mid
# immense
# lndian
# global
# big
# primeval
# warm
# wild
# frozen
# endless
# green
# german
# shoreless
# cold
# calm
# empty
# limitless
# restless
# south
# trackless
# tempestuous
# troubled