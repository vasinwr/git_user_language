#!/usr/bin/python
import urllib2
import json
import sys

def myplus(x):
    return x + 1

def language_count (data):
    lcount = {}
    for repo in data:
        if repo['language'] is not None:
            if repo['language'] in lcount:
                lcount[repo['language']] += 1
            else:
                lcount[repo['language']] = 1
    return lcount

def get_data(url):
    response = urllib2.urlopen(url)
    return json.load(response)


def main():
    try:
        while True:
            
            while True:
                query = raw_input("Please enter a Github username >> ")
                url = "https://api.github.com/users/"+query+"/repos"
                
                try:
                    data = get_data(url)
                except urllib2.HTTPError:
                    print "invalid user - please try again" 
                else:
                    break
            
            lcount = language_count(data) 
            
            if lcount:
                max_lang =  max(lcount, key=lcount.get)
                result = ""
                for lang in lcount:
                    if lcount[lang] == lcount[max_lang]:
                        result += " "+lang 
                print "most used language is(are): ", result
            else:
                print "The user have no repositry with a language registered"
            
    except KeyboardInterrupt:
        print "\nApplication exiting ..."
        sys.exit(0)

if __name__ == "__main__":
    main()
