# 1st program

print(9**0.5*4)


# 2nd program

print(9.99 > 9.98 and 100 != 100.1)


# 3rd program

result_1 = 2*2+2

# print(result_1)

result_2 = 2*(2+2)

# print(result_2)

print(result_1 == result_2)


# 4th program вариант 1

simbol = float("123.456")*10  # преобразовали текст в число с точкой и увеличили в 10 раз

last_figure = int(simbol) % 10  # преобразовали десятичное число в целое и взяли остаток от деления на 10

print(f"первая цифра после запятой - {last_figure}")


# 4th program вариант 2

print(int(float("123.456")*10) % 10)
