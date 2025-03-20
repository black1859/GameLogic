import json

class JsonReader():
    scriptFilesPaths = {
    'tutorial' : r'C:\Codes\pythons\GameLogic\jsons\scripts\ tutorial.json',
    'startadvanture' : r"C:\Codes\pythons\GameLogic\jsons\scripts\startadvanture.json",
    'events' : r'C:\Codes\pythons\GameLogic\jsons\Events\gethealpack.json',
}
    
    def __init__(self,pathKey:str = None):
        self.currentPath = None
        self.data = None
        self.loadData(path = pathKey)
    
    #when calling setPath Method, data should be changed
    def loadData(self, path:str):
        if path in JsonReader.scriptFilesPaths.keys():
            self.currentPath = path
            self.__setData()
            return self.data
        else:
            print(KeyError)
            return KeyError
    #it will be called only when setPath is called
    def __setData(self):
        with open(JsonReader.scriptFilesPaths[self.currentPath], 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def printall(self):
        print(self.data)

def getBasicReader(path = None):
    return JsonReader(path)

if __name__ == '__main__':
    t = JsonReader('tutorial')
    t.printall()
    t.loadData('afdasf')

    t.loadData('startadvanture')
    t.printall()