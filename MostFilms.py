# importing json and urllib library
import json
from urllib.request import urlopen
def main():
    try:
        # Storing URL in url
        url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
        # storing the url response
        response = urlopen(url)
        # storing JSON response from url in data
        data = json.loads(response.read())
    except:
        print("Some Error Occured ! ")
        # creating empty dictonary

    d ={}
    #iterating through thr each set in the data
    for i in data:
        year = i["year"]
        if year >= 2010:
            #creating dictonary with key as year if it doesnot exist
            if year not in d:
                d[year] = {}
                #counting the genres in each year
            for k in i["genres"]:
                d[year][k] = d[year].get(k,0)+1
    for y in d:
        print("In year ",y,"Most of the films released in genre",max(d[y],key=d[y].get))
    
if __name__ =="__main__":
    main()
