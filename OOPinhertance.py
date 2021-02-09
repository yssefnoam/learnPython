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
def main():
    # OP = Operation()
    # OP.Sub(5, 6)
    # OP.Sum(5, 6)
    OP = OperationWithMul()
    OP.Mul(5, 0)

main()