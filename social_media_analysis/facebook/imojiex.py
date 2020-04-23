from bs4 import BeautifulSoup

urls=[]
with open("C:/Users/Dane/Desktop/imojiii.html", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'html.parser')
    urls=[]
    main_blocks = soup.findAll('div', {'class': '_3vgi'})
    # main_blocks = soup.findAll('div')
    
    for main_block in main_blocks:
        # print ('block found!')
        block=[]
        clearfixes = main_block.findAll('div', {'class': 'clearfix'}) 
        for clearfix in clearfixes:
            row=[]
            imoji_containers=clearfix.findAll('span')
            for imoji_div in imoji_containers:
                div=imoji_div.find('div')
                img_part=div.find('img')
                link=img_part.get('src')
                row.append((link.split('/')[-1]).split('.')[0])
            block.append(row)
        urls.append(block)
        # break
# print (len(urls))
smile_urls=urls[1][:17]
symbol_urls=urls[7][:3]
urls_set=[smile_urls,symbol_urls]
print (urls[0][0])
print ('finding')
for i in range(len(urls)):
    for j in range(len(urls[i])):
        if ('2764' in urls[i][j]):
            print ('found the imoji !!')
            print(urls[i][j])
            print (len(urls[i]))
            print(i+1)
            print (j+1)


symbol=[
    [3.3,3.3,3.3,3.3,3.3,3.3,3.3,1.3],
    [3.3 for i in range(8)],
    [3.3 for i in range(8)],
]
smile=[
    [3.2 for i in range(8)],
    [3.1,3.1,3.1,3.2,3.1,3.1,2.3,3.3],
    [3.3 for i in range(8)],
    [3.3,3.3,1.3,2.2,2.2,3.1,3.3,3.3],
    [1.3 for i in range(8)],
    [1.3 for i in range(8)],
    [1.3 for i in range(8)],
    [1.3,1.3,1.3,1.2,3.2,2.2,3.1,2.2],
    [2.2,3.3,2.2,2.2,3.3,1.3,1.3,2.2],
    [1.3 for i in range(8)],
    [1.3,1.3,1.3,1.3,1.3,3.2,1.3,3.2],
    [1.3,1.3,1.3,2.1,2.1,3.1,3.3,3.3],
    [3.3,3.3,2.3,3.3,2.3,1.1,1.3,2.3],
    [3.2 for i in range(8)],
    [3.2 for i in range(8)],
    [3.2 for i in range(8)],
    [3.2 for i in range(8)]
]
values_set=[smile,symbol]
def  create_weights(urls_set,values_set):
    neg={}
    neu={}
    pos={}
    for k in range(len(urls_set)):
        values=values_set[k]
        urls=urls_set[k]
        for i in range(len(urls)):
            for j in range(8):
                if(1<values[i][j] and values[i][j]<1.4):
                    neg[urls[i][j]]=float("%.1f" % float(values[i][j]-1.0))
                elif(2<values[i][j] and values[i][j]<2.4):
                    neu[urls[i][j]]=float("%.1f" % float(values[i][j]-2.0))
                elif(3<values[i][j] and values[i][j]<3.4):
                    pos[urls[i][j]]=float("%.1f" % float(values[i][j]-3.0))             
    print ('pos')
    print (pos)
    print ('neu')
    print (neu)
    print ('neg')
    print (neg)

create_weights(urls_set,values_set)