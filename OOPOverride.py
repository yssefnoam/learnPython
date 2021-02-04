class Operation:
    def Sum(self, n1, n2):
        sumResult = n1 +n2
        print("sum = ", sumResult)
    def Sub(self, n1, n2):
        subResult = n1 - n2
        print("sub = ", subResult)


class OperationWithMul(Operation):
    def Mul(self, n1, n2):
        mulResult = n1 * n2
        print("mul = ", mulResult)
    def Sub(self, n1, n2):
        super().Sub(n1, n2)
        #subResult = n1 - n2 + 5
        #print("sub = ", subResult)


def main():
    OP = OperationWithMul()
    OP.Sub(5, 5)

main()