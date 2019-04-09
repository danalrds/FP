'''
Created on Nov 19, 2016

@author: Imi
'''
class IdObject():
    ''' 
    this is a parent class which will be used for another classes
    instaances of this classes will surely have an id, that's why this class has a setter and a getter
    method for the id field
    '''
    
    def __init__(self,objectId):
        self._objectId=objectId
    def getId(self):
        return self._objectId
    def setId(self,id):
        self._objectId=id    