class Category:
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name

    def setDescription(self, description):
        self._description = description

    def getDescription(self):
        return self._description