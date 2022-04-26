import urllib.request as url
import re
import bs4 as bs
import random


def get_html(genre, location, start = 0, main = None):
    """
    Request the yelp webpage with specified parameters
    Filters all html to find just the resturant info containers
       
    Returns Bs4 Set (list) of the html of found resutuarant div tags 
    """

    #Generate yelp link based of user inputs
    if main == None:
        source = 'https://www.yelp.com/search?find_desc={}&find_loc={}&sortby=rating&start={}'.format(genre, location, start)

    if main == 'backup':
        #Used when yelp returns no resturants for the above link
        source = 'https://www.yelp.com/search?find_desc={}&find_loc={}&sortby=recommended&start={}'.format(genre, location, start)

    #Connect to yelp page
    source = url.urlopen(source)

    #Save the webpage html
    soup = bs.BeautifulSoup(source, 'html.parser')
    
    #Filter webpage html for resturant div tags with specific class value (class value identifies only resturants)
    resturant_divs = soup.find_all("div", {"class": 'container__09f24__mpR8_ hoverable__09f24__wQ_on margin-t3__09f24__riq4X margin-b3__09f24__l9v5d padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border--top__09f24__exYYb border--right__09f24__X7Tln border--bottom__09f24___mg5X border--left__09f24__DMOkM border-color--default__09f24__NPAKY'})

    return resturant_divs


def extract_restaurant_name(a_tags):
    """
    Given a list of a tags from a resturant div,
    function finds the a tag with resturant name 
    
    Returns a string of the name
    """

    #Loop over all a_tags in the resturant div
    for a_tag in a_tags:
        attributes = a_tag.attrs #attrs returns dictionary of all attributes in the a_tag

        #If name is one of the key-value pairs it means the a tag has the resturant name
        if 'name' in attributes:
            return attributes['name'] #Returns name of resturant as string


def get_restaurants(html):
    """
    Given a list of resturant divs the function
    will find all a tags and send to extract_restaurant_name
    which will find the specific resturant div name then 
    saves name to list

    Returns list of all resturant names on the yelp page
    """

    restaurants = []

    #Loop over resturant divs in html
    for restaurant_html in html:
        a_tags = restaurant_html.findAll("a")

        #Find resturant name in the a tag list
        restaurants_name = extract_restaurant_name(a_tags)

        restaurants.append(restaurants_name)

    return restaurants


def restaurants_finder(genre, location, main = None):
    #Get yelp webpage html with user inputs on page 1
    html = get_html(genre, location, 0, main = main)

    #Find resturants from the html
    restaurants1 = get_restaurants(html)

    #If no resturants found return function to activate backup source
    if len(restaurants1) < 1:
        return 0

    #Same process as above but using the page 2 results
    html = get_html(genre, location, 10, main = main)
    restaurants2 = get_restaurants(html)

    #Combine page one and two results and drop duplicates
    return list(set(restaurants1 + restaurants2))


def choose_restaurant(list_of_restaurant):
    """
    Given list of restaurant names function
    generates random number and uses that
    number as an index to choose restaurant
    """

    length = len(list_of_restaurant) - 1
    num = random.randint(0, length) #randint includes 0 and length as possible choices

    return list_of_restaurant[num]


def where_to_eat(genre, location):
    """
    Main function used in tkinter application

    Given a user input of food genre and restuarant
    location, function will return a resturant that
    meets the user criteria

    Returns a single restuarant
    """

    #Generate list of all resturants that meet criteria
    lst = restaurants_finder(genre, location, main = None)

    #Run backup source if no resturants are found
    if lst == 0:
        lst = restaurants_finder(genre, location, main = 'backup')

    return choose_restaurant(lst)