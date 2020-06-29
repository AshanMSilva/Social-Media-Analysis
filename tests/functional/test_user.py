def test_home_page(test_client):
    
    response = test_client.get('/')
    assert response.status_code == 200

def test_Twitter_page(test_client):
    
    response = test_client.get('/twitter')
    assert response.status_code == 200

def test_Forum_page(test_client):
    
    response = test_client.get('/forum')
    assert response.status_code == 200

def test_Facebook_page(test_client):
    
    response = test_client.get('/facebook')
    assert response.status_code == 200

def test_Youtube_page(test_client):
    
    response = test_client.get('/youtube')
    assert response.status_code == 200

def test_StackOverflow_page(test_client):
    
    response = test_client.get('/stack_overflow')
    assert response.status_code == 200

def test_twitter_search(test_client):
    
    response = test_client.post('/twitter',
                                data=dict(search='submit', name='AshanMSilva'),
                                follow_redirects=True)
    assert response.status_code == 200

def test_twittersearch(test_client):
    
    response = test_client.get('/twitter/mahelajay',follow_redirects=True)
    post_response = test_client.post('/twitter/mahelajay')
    delete_response = test_client.delete('/twitter/mahelajay')
    put_response = test_client.put('/twitter/mahelajay')
                                
    assert response.status_code == 200
    assert post_response.status_code == 405
    assert delete_response.status_code == 405
    assert put_response.status_code == 405
def test_wrongroute(test_client):
    
    response = test_client.get('/twit')
                                
    assert response.status_code == 404

def test_twitterhashtag(test_client):

    response = test_client.get('twitter/hashtag/covid',follow_redirects=True)
    post_response = test_client.post('twitter/hashtag/covid')
    delete_response = test_client.delete('twitter/hashtag/covid')
    put_response = test_client.put('twitter/hashtag/covid')
                                
    assert response.status_code == 200
    assert post_response.status_code == 405
    assert delete_response.status_code == 405
    assert put_response.status_code == 405

def test_twitterbotaccount(test_client):
   
    response = test_client.get('/twitter/botaccount/mahelajay',follow_redirects=True)
    post_response = test_client.post('/twitter/botaccount/mahelajay')
    delete_response = test_client.delete('/twitter/botaccount/mahelajay')
    put_response = test_client.put('/twitter/botaccount/mahelajay')
                                
    assert response.status_code == 200
    assert post_response.status_code == 405
    assert delete_response.status_code == 405
    assert put_response.status_code == 405

def test_twitterlikes(test_client):
   
    response = test_client.get('/twitter/likesprediction/mahelajay', data=dict(time='22:10', tweet='AshanMSilva as shhd dhd') ,follow_redirects=True)
    post_response = test_client.post('/twitter/likesprediction/mahelajay')
    delete_response = test_client.delete('/twitter/likesprediction/mahelajay')
    put_response = test_client.put('/twitter/likesprediction/mahelajay')
                                
    assert response.status_code == 200

    assert post_response.status_code == 405
    assert delete_response.status_code == 405
    assert put_response.status_code == 405

def test_twitter_bot(test_client):
    
    response = test_client.post('/twitter',
                                data=dict(submit='submit', name='AshanMSilva'),
                                follow_redirects=True)
    assert response.status_code == 200

def test_twitter_hashtag(test_client):
    
    response = test_client.post('/twitter',
                                data=dict(hashtagsubmit='submit', hashtag='covid'),
                                follow_redirects=True)
    assert response.status_code == 200

def test_facebook_bot(test_client):

    response=test_client.post('/facebook/bot', data=dict(submit='submit',link='https://www.facebook.com/sisara.kahatapitiya.9'),follow_redirects=True)

    assert response.status_code == 200

def test_facebook_ad(test_client):
    response=test_client.post('/facebook/fbAdClicksPredict',data=dict(gender='M',adText='New employees',weekday='sun',minAge=18,maxAge=65,adSpends=12),follow_redirects=True)

    assert response.status_code == 200