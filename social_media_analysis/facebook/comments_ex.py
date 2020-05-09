pos_imojies= {'1f600': 0.2, '1f603': 0.2, '1f604': 0.2, '1f601': 0.2, '1f606': 0.2, '1f605': 0.2, '1f602': 0.2, '1f923': 0.2, '263a': 0.1, '1f60a': 0.1, '1f607': 0.1, '1f642': 0.2, '1f643': 0.1, '1f609': 0.1, '1f60d': 0.3, '1f970': 0.3, '1f618': 0.3, '1f617': 0.3, '1f619': 0.3, '1f61a': 0.3, '1f60b': 0.3, '1f61b': 0.3, '1f61d': 0.3, '1f61c': 0.3, '1f92a': 0.3, '1f60e': 0.1, '1f929': 0.3, '1f973': 0.3, '1f917': 0.2, '1f92d': 0.1, '1f636': 0.3, '1f62c': 0.3, '1f912': 0.2, '1f911': 0.2, '1f921': 0.1, '1f4a9': 0.3, '1f47b': 0.3, '1f480': 0.3, '2620': 0.3, '1f47e': 0.3, '1f639': 0.2, '1f63b': 0.2, '1f63c': 0.2, '1f63d': 0.2, '1f640': 0.2, '1f63f': 0.2, '1f63e': 0.2, '1f932': 0.2, '1f450': 0.2, '1f64c': 0.2, '1f44f': 0.2, '1f91d': 0.2, '1f44d': 0.2, '1f44e': 0.2, '1f44a': 0.2, '270a': 0.2, '1f91b': 0.2, '1f91c': 0.2, '1f91e': 0.2, '270c': 0.2, '1f91f': 0.2, '1f918': 0.2, '1f44c': 0.2, '1f448': 0.2, '1f449': 0.2, '1f446': 0.2, '1f447': 0.2, '261d': 0.2, '270b': 0.2, '1f91a': 0.2, '1f590': 0.2, '1f596': 0.2}

neu_imojies={'1f60c': 0.3, '1f9d0': 0.2, '1f913': 0.2, '1f914': 0.2, '1f92b': 0.2, '1f925': 0.2, '1f610': 0.2, '1f611': 0.2, '1f626': 0.2, '1f479': 0.1, '1f47a': 0.1, '1f47d': 0.3, '1f916': 0.3, '1f638': 0.3}

neg_imojies={'1f928': 0.3, '1f60f': 0.3, '1f612': 0.3, '1f61e': 0.3, '1f614': 0.3, '1f61f': 0.3, '1f615': 0.3, '1f641': 0.3, '2639': 0.3, '1f623': 0.3, '1f616': 0.3, '1f62b': 0.3, '1f629': 0.3, '1f97a': 0.3, '1f622': 0.3, '1f62d': 0.3, '1f624': 0.3, '1f620': 0.3, '1f621': 0.3, '1f92c': 0.3, '1f92f': 0.3, '1f633': 0.3, '1f975': 0.3, '1f976': 0.3, '1f631': 0.3, '1f628': 0.3, '1f630': 0.3, '1f625': 0.3, '1f613': 0.2, '1f644': 0.3, '1f62f': 0.3, '1f627': 0.3, '1f62e': 0.3, '1f632': 0.3, '1f634': 0.3, '1f924': 0.3, '1f62a': 0.3, '1f635': 0.3, '1f910': 0.3, '1f974': 0.3, '1f922': 0.3, '1f92e': 0.3, '1f927': 0.3, '1f637': 0.3, '1f915': 0.3, '1f920': 0.3, '1f608': 0.3, '1f47f': 0.3, '1f383': 0.1, '1f63a': 0.3}
from bs4 import BeautifulSoup
import cssutils
with open("C:/Users/Dane/Desktop/(9) Campus Set Eka_කැම්පස් අපේ පිටුව - Posts.html", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'html.parser')
    comments=[]
    main_content = soup.find('ul', {'class': '_7a9a'})
    try:
        list_of_comments = main_content.findAll('li')
    except:
        main_content= soup.find('ul', {'class': '_7791'})
        list_of_comments = main_content.findAll('li')
    for container_large in list_of_comments:
        try:
            img_link= container_large.img.get('src')
            comment_container=container_large.find('div', {'class': '_72vr'})
            
            profile_link=comment_container.a.get('href')
            container_small = container_large.find('span', {'class': '_3l3x'}) #imoji spnas & text in here
            imoji_spans=container_small.findAll('span', {'class': '_5mfr'})
            imojies=[]
            for imoji_span in imoji_spans:
                span_style=imoji_span.find('span')['style']
                style=cssutils.parseStyle(span_style)
                imoji_url=style['background-image']
                imojies.append((imoji_url.split('/'))[-1].split('.')[0])
            profile_name_container=comment_container.find('a', {'class': '_6qw4'})
            profile_name=profile_name_container.text
            lnk="C:/Users/Dane/Desktop"+img_link[1:]
            comments.append([container_small.text,profile_name,profile_link,lnk,imojies])
        except:
            x='s'
    # print (comments[6])
# print (pos_imojies['1f4aa'])