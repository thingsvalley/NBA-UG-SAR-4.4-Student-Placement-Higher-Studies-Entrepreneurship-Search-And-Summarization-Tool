import webbrowser
#import urllib.
import requests


def searchName( firstName , lastName )
    
    tabUrl="https://www.linkedin.com/people/search?firstName="+firstName+"&lastName="+lastName+"&trk=homepage-basic_people-search-bar_search-submit?#q=";
    r=requests.get(tabUrl)
    print(tabUrl)    
    term ="gogte institute of technology"
    var = webbrowser.open(tabUrl+term);
