def main():
    dirs = [
    "blog/travel/myblog.pdf",
    "blog/travel/yourblog.pdf",    
    "whitepaper/travel/mywhitepaper.pdf",
    "whitepaper/travel/yourwhitepaper.pdf"]
    lst = []
    for dr in dirs:
        p = dr.split('/')
        for i in p:
            d ={}
            if '.' in i:
                d["type"] = "file"
                d["name"] = i
                d["path"] = path(i,p)
            else:
                d["type"] = "folder"
                d["name"] = i
                d["path"] = path(i,p)
                d["children"] = []
            if not lst:
                lst.append(d)
            else:
                for k in lst:
                    app(dict(k))
    print(lst)
                                            
def app(k):
    for key,value in k.items():
        if key == "children":
            if not "children":
                value = d
            else: 
                for i in value:
                    app(dict(i))
        else:
            continue

def path(i,p):
    s =""
    for k in p:
        if(i==k):
            s+=("/"+k)
            break
        s+=("/"+k)
    return s
if __name__ == "__main__":
    
    main()