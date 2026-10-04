def divide(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    negative = (dividend < 0) != (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    quotient = 0
    while a >= b:
        shift = 0

        while a >= (b << (shift + 1)):
            shift += 1

        quotient += 1 << shift
        a -= b << shift

    if negative:
        quotient = -quotient

    if quotient > INT_MAX:
        return INT_MAX
    if quotient < INT_MIN:
        return INT_MIN
    return quotient
dividend, divisor = map(int, input().split())
print(divide(dividend, divisor))
