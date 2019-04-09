'''
Created on Dec 9, 2016

@author: Imi
'''
class UndoController:
    def __init__(self):
        self._operations=[]
        self._counter=-1
        self._recorded=True
    def checkRecord(self):
        return self._recorded
    def saveOperation(self, operation):
        if self.checkRecord()==True:
            self._operations[-1].append(operation)
    def newOperation(self):
        if self.checkRecord()==False:
            return
        self._operations=self._operations[0:self._counter+1]
        self._operations.append([])
        self._counter=self._counter+1
    def undoOperation(self):
        if self._counter<0:
            return False
        self._recorded=False
        for operation in self._operations[self._counter]:
            operation.undo()
        self._recorded=True
        self._counter=self._counter-1
        return True
    def redoOperation(self):
        if self._counter>len(self._operations):
            return False
        self._recorded=False
        for operation in self._operations[self._counter+1]:
            operation.redo()
        self._recorded=True
        self._counter=self._counter+1
        return True
class Function:
    def __init__(self,funcName, *parameters):
        self._funcName=funcName
        self._parameters=parameters
    def callFunction(self):
        self._funcName(*self._parameters)
class Operation:
    def __init__(self, do, undo):
        self._do=do
        self._undo=undo
    def undo(self):
        self._undo.callFunction()
    def redo(self):
        self._do.callFunction()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    