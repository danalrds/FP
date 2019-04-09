'''
Created on Nov 26, 2016

@author: Imi
'''
class ValidatorException(Exception):
    def __init__(self,Emess):
        self._mess=Emess
    def getMessage(self):
        return self._mess
    def __str__(self):
        messList=''
        for mess in self.getMessage():
            messList+=str(mess)
        return messList