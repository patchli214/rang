from xpinyin import Pinyin

def removeComment():
    file = open("/Users/patch/Documents/project/rang/stations.txt",'r')
    file2 = open("/Users/patch/Documents/project/rang/stations-pure.",'a')
    lines = file.readlines()
    for line in lines:
        if line.find('/*') == -1:
            file2.writelines([line])
    print('DONE')
    return

def pinyin():
    file = open("/Users/patch/Documents/project/rang/station-nolatin.json",'r')
    file2 = open("/Users/patch/Documents/project/rang/station.json",'a')
    lines = file.readlines()

    indb = []
    p = Pinyin()
    name = ''
    latin = ''
    i = 0
    for line in lines:
        if line.find('name') > -1:
            latin = ''
            name = line[line.find('name')+9:len(line)-3]
            py = p.get_pinyin(name).split("-")
            for s in py:
                latin = latin + s

        elif line.find('\"latin\" : \"\"') > -1:
            i = i + 1
            print(latin)
            line = line.replace('\"latin\" : \"\"','\"latin\" : \"'+latin+'\"')
            print(line)
            #file2.writelines([line])
        file2.writelines([line])
        #latin = ''
    file.close()
    file2.close()
    return

if __name__ == "__main__":
    removeComment()
    #pinyin()
