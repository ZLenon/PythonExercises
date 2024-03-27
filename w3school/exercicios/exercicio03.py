class ClassVariables:
    def carName(self):
        carName = "Volvo"
        return carName

    def numberRandom(self):
        number = 10
        return number

    def createVariables(self):
        x = 2
        y = 5
        return x, y

    def sumPrintSum(self):
        x = 2
        y = 5
        z = x * y
        return z, x, y

    def printStrings(self):
        x, y, z = "Orange", "Banana", "Cherry"
        return x, y, z

    def atribuindoMesmoValor(self):
        x = y = z = "Orange"
        return x, y, z

    def showVariableGlobal(self):
        global varGlobal
        varGlobal = "Lenon"
        return varGlobal
