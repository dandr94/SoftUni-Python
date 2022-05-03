class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        sum_of_args = 1
        for num in args:
            sum_of_args *= num

        return sum_of_args

    @staticmethod
    def divide(*args):
        my_num = args[0]
        subtract_sum = sum(args[1:])
        if subtract_sum != 0:
            return my_num / subtract_sum

    @staticmethod
    def subtract(*args):
        my_num = args[0]
        subtract_sum = sum(args[1:])

        return my_num - subtract_sum


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
