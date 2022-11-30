import aiohttpclient

url = 'http://localhost:8080/people'

def getPersons():
    return aiohttpclient.get(url)