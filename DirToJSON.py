def main():
    dirs = ["blog/travel/myblog.pdf","blog/travel/yourblog.pdf","whitepaper/travel/mywhitepaper.pdf","whitepaper/travel/yourwhitepaper.pdf"]
    lst = []
    for dr in dirs:
        d= {}
        p = dr.split('/')
        for i in p:
            if '.' in i:
                d["type"] = "file"
                d["name"] = i
                d["path"] = path(i,p)
            else:
                d["type"] = "folder"
                d["name"] = i
                d["path"] = path(i,p)
                d["children"] = []


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