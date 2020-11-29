class Stack:
    def _data_validate(self):
        self._stack['size']=len(self._stack['data'])

    def __init__(self,elements=[], filename="nil" ):
        self._stack={}
        self._stack['size']=[]
        self._stack['data']=elements
        self._stack['size']=len(elements)
    
    def pop(self):
        if not self._stack['size']:
            raise Exception("stack Exausted")
        temp=self._stack['data'][self._stack['size']-1]
        del self._stack['data'][self._stack['size']-1]
        self._stack['size']=len(self._stack['data'])
        
        return temp

    def empty_stack(self):
        self._stack["data"]=[]
        self._data_validate()

    def push(self,newElement=""):
        self._stack['data'].append(newElement)
        self._stack['size']=len(self._stack['data'])
        return newElement

    def is_empty(self):
        if self._stack['size']:
            return 0
        else:
            return 1 
    
    def size(self):
            temp=self._stack['size']
            return temp
    
    def top(self):
        if not self._stack['size']:
            raise Exception("stack empty")
        return self._stack['data'][self._stack['size']-1]

    def stack(self):
        temp=self._stack['data']
        return temp 

    def raw_stack(self):
        temp=self._stack
        return temp