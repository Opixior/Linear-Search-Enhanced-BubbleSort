class IdentificationCard():
    def __init__(self,fn,ln,idnum):
        self.__firstName = fn
        self.__lastName = ln
        self.__IDnumber = idnum

    def getfirstName(self):
        return self.__firstName

    def getlastName(self):
        return self.__lastName

    def getIDNumber(self):
        return self.__IDnumber



