class idobject():
    def init(self,objectid):
        self._objectid=objectid
    def getId(self):
        return self._objectid
    def setId(self,id):
        self._objectid=id