import urllib.request as url
import re
import bs4 as bs
import random


def get_html(genre, location, start = 0, main = None):
    if main == None:
        source = 'https://www.yelp.com/search?cflt={}&find_loc={}&sortby=rating&start={}'.format(genre, location, start)

    if main == 'backup':
        source = 'https://www.yelp.com/search?cflt={}&find_loc={}&sortby=recommended&start={}'.format(genre, location, start)

    source = url.urlopen(source)
    soup = bs.BeautifulSoup(source, 'html.parser')

    mains = soup.find_all("div", {"class": 'businessName__09f24__3Ml2X display--inline-block__09f24__3SvIn border-color--default__09f24__3Epto'})

    return mains


def get_restaurants(html):
    restaurants = []
    for restaurant_html in html:
        restaurants.append(restaurant_html.find('a').text)

    return restaurants


def restaurants_finder(genre, location, main = None):
    html = get_html(genre, location, 0, main = main)
    restaurants1 = get_restaurants(html)

    if len(restaurants1) < 1:
        return 0

    html = get_html(genre, location, 10, main = main)
    restaurants2 = get_restaurants(html)

    return list(set(restaurants1 + restaurants2))


def choose_restaurant(list_of_restaurant):
    length = len(list_of_restaurant) - 1
    num = random.randint(0, length)

    return list_of_restaurant[num]


def back_up_function():
    pass



def where_to_eat(genre, location):
    lst = restaurants_finder(genre, location, main = None)

    if lst == 0:
        lst = restaurants_finder(genre, location, main = 'backup')

    return choose_restaurant(lst)
