def transform(base, number):
    result = ""

    while number != 0:
        number, mod = divmod(number, base)

        if base > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod%10]
        else:
            result += str(mod)
    return result[::-1]


def solution(n, t, m, p):

    result = "0"

    for num in range(1, t*m):
        result += transform(n, num)

    return "".join(result[i] for i in range(p-1, t*m, m))