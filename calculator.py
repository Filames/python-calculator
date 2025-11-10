class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        bcount = b
        if b < 0:
            bcount *= -1
        for i in range(bcount):
            result = self.add(result, a)
        if b < 0:
            result = result * -1
        return result

    def divide(self, a, b):
        result = 0
        diva = a
        divb = b
        if(a < 0):
            diva = a - (a+a)
        if(b < 0):
            divb = b - (b+b)
        while diva > divb - 1:
            diva = self.subtract(diva, divb)
            result += 1
        if b < 0 or a < 0:
            result = result - (result+result)
        return result

    def modulo(self, a, b):
        a_div_b = self.divide(a, b)
        if b < 0 and a < 0:
            a_div_b = a_div_b
        elif b < 0 or a < 0:
            a_div_b -= 1
        result = self.multiply(a_div_b, b)
        return self.subtract(a, result)



# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
