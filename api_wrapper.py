import requests


class MailStatus:
    # api url
    def __init__(self, url=None):
        self.url = url if url is not None else "default url"
    
    # returns a hash value
    def getHash(self):
        endpoint = "/get_image_hash/"
        res = requests.get(self.url + endpoint)
        if res.ok :
            js = res.json()
            if "i_hash" in js.keys():
                return js["i_hash"]
            return False
        return False
        
    # checks status
    def hashStatus(self,i_hash):
        endpoint = "/get_hash_status/"+i_hash
        res = requests.get(self.url + endpoint)
        if res.ok :
            js = res.json()
            if "status" in js.keys():
                return js["status"]
            return False
        return False
    


# status = MailStatus(url="https://8f18d1285c80.ngrok.io")


# h = status.getHash()

# status.hashStatus(h)

