from Read import readexcel

from Search import searchName

names = readexcel()

for name in names:
    print( "name[0] " + name[0] , " name[1] " + name[1] )
    searchName( name[0] , name[1] )

import webbrowser
#import urllib.
import requests

    
tabUrl="https://www.linkedin.com/uas/login?trk=people-guest_nav-header-signin?#q=";
r=requests.get(tabUrl)
print(tabUrl)        
var = webbrowser.open(tabUrl);
