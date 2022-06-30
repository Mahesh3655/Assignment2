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
        # creating empty dictonary
    except:
        print("Invalid url")
    d ={}
    #iterating through thr each set in the data
    for i in data:
        if i["year"] == 2018:
            #counting the films in each genre in year 2018
            for k in i["genres"]:
                d[k] = d.get(k,0)+1
    #converting dictonary to list of tuples
    lst = list(d.items())
    #Bubble sort
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(lst[j][1] < lst[j+1][1]):
                t = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = t
    d = dict(lst)
    for key in d:
        print(key, d[key])
if __name__ == "__main__":
    main()