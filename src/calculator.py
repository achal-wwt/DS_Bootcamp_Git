class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide_achal(self):
        return self.a / self.b

    def divide_anonymous(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("[Error] Denominator can't be Zero in division!")

