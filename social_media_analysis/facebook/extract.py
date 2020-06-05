
import browser_cookie3
import requests

def get_first_tag(tag,unique,inputt):
    unique_start_index=int(inputt.find(unique))
    i=1
    #find start index
    while (True):
        if (inputt[unique_start_index-i]=='<'):
            # print('found 1')
            start_index=unique_start_index-i
            break
        else:
            i+=1
    #find end index
    i=1
    while (True):
        if (inputt[unique_start_index+i]=='>'):
            end_index=unique_start_index+i
            break
        else:
            i+=1
    return (inputt[start_index:end_index+1])
def get_parent_level_elements(tag,parent_tag,inputt):
    elements=[]
    start_index=len('<'+parent_tag)
    full_length=len(inputt)
    while(True):
        if(start_index<full_length):
            tag_start_index=inputt[start_index:].find('<'+tag)+start_index
            result=get_full_element(tag,tag_start_index,inputt)
            elements.append(result[0])
            tag_end_index=result[1]
            start_index=tag_end_index
        else:
            break
    return elements

def get_series_of_same_elememts(tag,unique_values,inputt,num_of_elements):
    elements=[]
    for i in range(num_of_elements):
        try:
            unique=unique_values[0]    
            unique_start_index=int(inputt.find(unique))
            if(unique_start_index==-1):
                break
            passed=1
            if (passed==len(unique_values)):
                i=1
                #find start index
                while (True):
                    if (inputt[unique_start_index-i]=='<'):
                        # print('found 1')
                        start_index=unique_start_index-i
                        break
                    else:
                        i+=1
                #find end element
                result=get_full_element(tag,start_index,inputt)
                elements.append(result[0])
                # print(result[0])
                inputt=inputt[result[1]:]
            else:
                print('cannot get the exact element')
        except:
            break
    return elements
def get_full_element(tag,start_index,inputt): #this fuction return the entire element starting from given index
    temp_start=start_index+len('<'+tag)
    found=1
    while (True):
        if (found!=0):
            open_index=inputt[temp_start:].find('<'+tag)+temp_start
            close_index=inputt[temp_start:].find('</'+tag+'>')+temp_start
            if(open_index<close_index):  #found another open tag
                found+=1
                temp_start=open_index+len('<'+tag)
            else:  #found a closed tag
                found-=1
                temp_start=close_index+len('</'+tag+'>')
        else:
            break
    end_index=temp_start
    return ([inputt[start_index:end_index],end_index])

def get_element(tag,unique_values,inputt): #this function can get entire element with the unique values(list)

    unique=unique_values[0]
    unique_start_index=int(inputt.find(unique))
    passed=1
    # for u in unique_values:
    #     if ():
    #         passed+=1
    if (passed==len(unique_values)):
        i=1
        try:        
            #find start index
            while (True):
                if (inputt[unique_start_index-i]=='<'):
                    # print('found 1')
                    start_index=unique_start_index-i
                    break
                else:
                    i+=1
            #find end index
            temp_start=start_index+len('<'+tag)
            found=1
            while (True):
                if (found!=0):
                    close_index=inputt[temp_start:].find('</'+tag+'>')+temp_start
                    if(inputt[temp_start:].find('<'+tag)!=-1):
                        open_index=inputt[temp_start:].find('<'+tag)+temp_start
                    else:
                        open_index=close_index+10
                    if(open_index<close_index):  #found another open tag
                        found+=1
                        temp_start=open_index+len('<'+tag)
                    else:  #found a closed tag
                        found-=1
                        temp_start=close_index+len('</'+tag+'>')
                else:
                    break
            end_index=temp_start
            return (inputt[start_index:end_index])
        except:
            return None
    else:
        print('cannot get the exact element')

def get_a_value_within_a_tag(tag,inputt): #this function get tag value within a given input (not need to get exact tag)
    tag_start_index=int(inputt.find('<'+tag))
    # value start index
    i=1 
    try:    
        while(True):
            if(inputt[tag_start_index+i]=='>'):
                value_start_index=tag_start_index+i+1
                break
            else:
                i+=1
        # value end index
        while(True):
            if(inputt[tag_start_index+i+1]=='<'):
                value_end_index=tag_start_index+i+1
                break
            else:
                i+=1
        return (inputt[value_start_index:value_end_index])
    except:
        return
      




# r = requests.get(url, cookies=cj)


# find education
def find_education_details(url):
    details={}
    edu_url=url+'/about?section=education'
    req = requests.get(edu_url, cookies=cj)
    w=req.text # pagelet_eduwork
    category_containers=get_series_of_same_elememts('div',['class="_4qm1"'],w,4)
    for category_container in category_containers:
        category_container_small=get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
        # print ("category")
        # print(category_container_small)
        key_container=get_element('div',['class="clearfix _h71"'],category_container)
        key=get_a_value_within_a_tag('span',key_container)
        # print(key_container)
        details[key]=[]
        # print(category_container)
        value_containers=get_parent_level_elements('li','ul',category_container_small)    
        for value_container_large in value_containers:

            value_container=get_element('div',['class="_2lzr _50f5 _50f7"'],value_container_large)
            
            value=get_a_value_within_a_tag('a',value_container)
            
            details[key].append(value)
    return details
def find_basic_info(url):
        details={}
        edu_url=url+'/about?section=contact-info'
        req = requests.get(edu_url, cookies=cj)
        w=req.text
        category_containers=get_series_of_same_elememts('div',['class="_4qm1"'],w,4)
        for category_container in category_containers:
            category_container_small=get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
            # print ("category")
            # print(category_container)
            key_value_containers=get_parent_level_elements('li','ul',category_container_small)    
            for key_value_container in key_value_containers:
                key_container=get_element('div',['class="_4bl7 _3xdi _52ju"'],key_value_container)
                key=get_a_value_within_a_tag('span',key_container)
                details[key]=''
                value_container=get_element('ul',['class="uiList _4kg"'],key_value_container)
                if(value_container==''):
                    value_container=get_element('div',['class="_4bl7 _pt5"'],key_value_container)
                
                value=get_a_value_within_a_tag('span',value_container)
                if(value==''):
                    value=get_a_value_within_a_tag('li',value_container)
                    if(value==''):
                        value=get_a_value_within_a_tag('a',value_container)
                details[key]=value

                        # print('NO VALUE')
        return details
        

def find_relationship_details(url):
    edu_url=url+'/about?section=relationship'
    req = requests.get(edu_url, cookies=cj)
    w=req.text
    details={}
    category_containers=get_series_of_same_elememts('div',['class="_4qm1"'],w,4)
    for category_container in category_containers:
        category_container_small=get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
        # print ("category")
        # print(category_container_small)
        key_container=get_element('div',['class="clearfix _h71"'],category_container)
        key=get_a_value_within_a_tag('span',key_container)
        # print(key_container)
        details[key]=[[],[]]
        # print(category_container)
        value_containers=get_parent_level_elements('li','ul',category_container_small)    
        check=get_element('span',['class="_50f8 _2iem"'],value_containers[0])
        if(check!=''):
            details[key][0]=0
        else:
            details[key][0]=len(value_containers)
            for value_container_large in value_containers:

                value_container=get_element('div',['class="fsm fwn fcg"'],value_container_large)
                # print(value_container)
                value=get_a_value_within_a_tag('span',value_container)
                if(value==''):
                    value=get_a_value_within_a_tag('a',value_container)
                    
                details[key][1].append(value)  
    return details

def get_friend_count(url):
    edu_url=url+'/friends'
    req = requests.get(edu_url, cookies=cj)
    w=req.text
    print(get_element('span',['class="_3d0"'],w))

    friend_count_container=get_element('a',['class="_3c_ _3s-"'],w)
    # print(friend_count_container)
    count=get_a_value_within_a_tag('span',friend_count_container)
    print(count)

def find_tag_photo_count(url):
    edu_url=url+'/photos_of'
    req = requests.get(edu_url, cookies=cj)
    w=req.text
    details={}
    photo_container=get_element('ul',['id="u_0_3o"'],w)
    # print(photo_container)
    photos=get_parent_level_elements('li','ul',photo_container)
    details['tagged_photo_count']=len(photos)
    return details
# https://www.facebook.com/dilshan.lakshaka/friends

url='https://www.facebook.com/sanduniayeshika.silva'
# url = 'https://www.facebook.com/chinthakau'
# url = 'https://www.facebook.com/dilshan.lakshaka'
# url='https://www.facebook.com/thanuja.malshan'
# url='https://www.facebook.com/harshani.cathurani'
# url='https://www.facebook.com/ruwanthi.paranagama'
# basic_info(url)
# find_education_details(url)
# find_relationship_details(url)
# find_tag_photo_count(url)
# # find_relationship_details(url)
# get_friend_count(url)

# cj = browser_cookie3.chrome()
# def get_info(url):
#     basic_info=find_basic_info(url)
#     education_details=find_education_details(url)
#     relationship_details=find_relationship_details(url)
#     photo_count=find_tag_photo_count(url)
#     info={**basic_info,**education_details,**relationship_details,**photo_count}
#     return info
#     # return basic_info



# print (get_info(url))
# get_a_value_within_a_tag('a',el)   