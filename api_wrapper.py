import requests


class MailStatus:
    # api url
    def __init__(self, url=None):
        self.url = url if url is not None else " default heroku url " #if this is blank, i probably didnt get a chance to host it on heroku ;)
    
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
    
    # make URL out of a given hash
    def getImgURL(self,i_hash=None):
        if i_hash==None:
            endpoint = "/get_image_hash/"
            res = requests.get(self.url + endpoint)
            if res.ok :
                js = res.json()
                if "i_hash" in js.keys():
                    return self.url+"/load_image/"+js["i_hash"]
                return False
            return False
        return self.url+"/load_image/"+i_hash
        
    # checks status of given hash
    def hashStatus(self,i_hash):
        endpoint = "/get_hash_status/"+i_hash
        res = requests.get(self.url + endpoint)
        if res.ok :
            js = res.json()
            if "status" in js.keys():
                return js["status"]
            return False
        return False
    




