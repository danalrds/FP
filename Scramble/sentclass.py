class Sentence():
    def __init__(self,sent):
        self._sent=sent  
    def getSent(self):
        return str(self._sent)
    def __str__(self):
        return str(self._sent)
