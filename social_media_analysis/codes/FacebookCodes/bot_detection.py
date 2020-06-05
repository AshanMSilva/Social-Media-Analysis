import browser_cookie3
import requests
import time
class BotAccountDetection():
    def get_first_tag(self,tag,unique,inputt):
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
    def get_parent_level_elements(self,tag,parent_tag,inputt):
        elements=[]
        if(inputt==None):
            return []
        start_index=len('<'+parent_tag)
        full_length=len(inputt)
        while(True):
            if(start_index<full_length):
                tag_start_index=inputt[start_index:].find('<'+tag)+start_index
                result=self.get_full_element(tag,tag_start_index,inputt)
                elements.append(result[0])
                tag_end_index=result[1]
                start_index=tag_end_index
            else:
                break
        return elements

    def get_series_of_same_elememts(self,tag,unique_values,inputt,num_of_elements):
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
                    result=self.get_full_element(tag,start_index,inputt)
                    elements.append(result[0])
                    # print(result[0])
                    inputt=inputt[result[1]:]
                else:
                    print('cannot get the exact element')
            except:
                break
        return elements
    def get_full_element(self,tag,start_index,inputt): #this fuction return the entire element starting from given index
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

    def get_element(self,tag,unique_values,inputt): #this function can get entire element with the unique values(list)

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

                #check if found the correct tag
                if(inputt[start_index:start_index+len('<'+tag)]!='<'+tag):
                    return None
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

    def get_a_value_within_a_tag(self,tag,inputt): #this function get tag value within a given input (not need to get exact tag)
        if(inputt==None):
            return None
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
            return None
        


    # find education
    def find_education_details(self,url,cj):
        details={}
        edu_url=url+'/about?section=education'
        req = requests.get(edu_url, cookies=cj)
        w=req.text # pagelet_eduwork
        category_containers=self.get_series_of_same_elememts('div',['class="_4qm1"'],w,4)
        for category_container in category_containers:
            category_container_small=self.get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
            # print ("category")
            # print(category_container_small)
            key_container=self.get_element('div',['class="clearfix _h71"'],category_container)
            key=self.get_a_value_within_a_tag('span',key_container)
            # print(key_container)
            details[key]=[]
            # print(category_container)
            value_containers=self.get_parent_level_elements('li','ul',category_container_small)    
            for value_container_large in value_containers:

                value_container=self.get_element('div',['class="_2lzr _50f5 _50f7"'],value_container_large)
                
                value=self.get_a_value_within_a_tag('a',value_container)
                
                details[key].append(value)
        return details
    def find_basic_info(self,url,cj):
            details={}
            edu_url=url+'/about?section=contact-info'
            req = requests.get(edu_url, cookies=cj)
            w=req.text
            category_containers=self.get_series_of_same_elememts('div',['class="_4qm1"'],w,4)

            for category_container in category_containers:
                category_container_small=self.get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
                # print ("category")
                key_value_containers=self.get_parent_level_elements('li','ul',category_container_small)    
                for key_value_container in key_value_containers:
                    # break
                    key_container=self.get_element('div',['class="_4bl7 _3xdi _52ju"'],key_value_container)
                    key=self.get_a_value_within_a_tag('span',key_container)
                    details[key]=''
                    value_container=self.get_element('ul',['class="uiList _4kg"'],key_value_container)
                    if(value_container==None):
                        value_container=self.get_element('div',['class="_4bl7 _pt5"'],key_value_container)
                    
                    value=self.get_a_value_within_a_tag('span',value_container)
                    if(value==None):
                        value=self.get_a_value_within_a_tag('li',value_container)
                        if(value==None):
                            value=self.get_a_value_within_a_tag('a',value_container)
                    details[key]=value
            return details
            

    def find_relationship_details(self,url,cj):
        edu_url=url+'/about?section=relationship'
        req = requests.get(edu_url, cookies=cj)
        w=req.text
        details={}
        category_containers=self.get_series_of_same_elememts('div',['class="_4qm1"'],w,4)
        for category_container in category_containers:
            category_container_small=self.get_element('ul',['class="uiList fbProfileEditExperiences _4kg _4ks"'],category_container)    
            # print ("category")
            # print(category_container_small)
            key_container=self.get_element('div',['class="clearfix _h71"'],category_container)
            key=self.get_a_value_within_a_tag('span',key_container)
            # print(key_container)
            details[key]=[[],[]]
            # print(category_container)
            value_containers=self.get_parent_level_elements('li','ul',category_container_small)  
            if(value_containers==[]):
                return details
            check=self.get_element('span',['class="_50f8 _2iem"'],value_containers[0])
            if(check!=None):
                details[key][0]=0
            else:
                details[key][0]=len(value_containers)
                for value_container_large in value_containers:

                    value_container=self.get_element('div',['class="fsm fwn fcg"'],value_container_large)
                    # print(value_container)
                    value=self.get_a_value_within_a_tag('span',value_container)
                    if(value==None):
                        value=self.get_a_value_within_a_tag('a',value_container)
                        
                    details[key][1].append(value)  
        return details

    def get_friend_count(self,url,cj):
        edu_url=url+'/friends'
        req = requests.get(edu_url, cookies=cj)
        w=req.text
        print(get_element('span',['class="_3d0"'],w))

        friend_count_container=self.get_element('a',['class="_3c_ _3s-"'],w)
        # print(friend_count_container)
        count=self.get_a_value_within_a_tag('span',friend_count_container)
        print(count)

    def find_tag_photo_count(self,url,cj):
        edu_url=url+'/photos_of'
        req = requests.get(edu_url, cookies=cj)

        # time.sleep(5)
        w=req.text
        # print (w)
        details={}
        photo_container=self.get_element('ul',['class="fbStarGrid'],w)
        # print(photo_container)
        photos=self.get_parent_level_elements('li','ul',photo_container)
        details['tagged_photo_count']=len(photos)
        return details

    def get_info(self,url):
        cj = browser_cookie3.chrome()
        basic_info=self.find_basic_info(url,cj)
        education_details=self.find_education_details(url,cj)
        relationship_details=self.find_relationship_details(url,cj)
        photo_count=self.find_tag_photo_count(url,cj)
        info={**basic_info,**education_details,**relationship_details,**photo_count}
        return info

    def calculate(self,info_dict):
        neg=0
        pos=0
        check=[]
        #address
        if('Address' in info_dict):
            pos+=20
            check.append('add ok')
        else:
            neg+=20

        #education/work
        edu=0
        edu_found=False
        work_found=False
        if('Education' in info_dict):
            if(info_dict['Education'][0]!=None):
                edu+=len(info_dict['Education'])*10
                check.append('edu ok')
                edu_found=True
        if('Work' in info_dict):
            if(info_dict['Work'][0]!=None):
                edu+=len(info_dict['Work'])*10
                check.append('work ok')
                work_found=True
        if(edu_found==False and work_found==False):
            neg+=20
        else:
            if(edu<=20):
                pos+=edu
            else:
                pos+=20

        #family
        if('Family Members' in info_dict):
            num=info_dict['Family Members'][0]*10
            if(num>0):
                if(num<=20):
                    check.append('fam'+str(num))
                    pos+=num
                else:
                    pos+=20
            else:
                neg+=20
        # tagged
        if('tagged_photo_count' in info_dict):
            num=info_dict['tagged_photo_count']
            if(num>0):
                # if(num<=20):
                #     check.append('tag'+str(num))
                #     pos+=num
                # else:
                pos+=20
            else:
                neg+=20

        #others
        other=0
        if('Birthday' in info_dict):
            other+=5
        
        if('Gender' in info_dict):
            other+=5
        if('Religious Views' in info_dict):
            other+=5
        if('Interested In' in info_dict):
            other+=5

        if('Mobile Phones' in info_dict):
            other+=5
        if(other>0):
            if(other<20):
                pos+=other
                neg+=(20-other)/2
            else:
                pos+=20
        else:
            neg+=20
        check.append('other'+str(other))
        

        neg_p=neg*100/(pos+neg)
        pos_p=pos*100/(pos+neg)
        res={'pos':pos_p,'neg':neg_p,'check':check}
        return res
