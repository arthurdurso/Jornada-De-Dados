class Calculadora:
    def soma(self, *args):
        total = 0
        for numero in args:
            total += numero
        return total
    
calculadora = Calculadora()
print(calculadora.soma(381,237))
print(calculadora.soma(28,294,1,0))
print(calculadora.soma(3,7,10,21,-1))
