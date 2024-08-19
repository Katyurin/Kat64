def generate_password(divisor):
    result = ''
    for i in range(1, 11):
        for j in range(1, 11):
            if i != j:
                pair_sum = i + j
                if divisor % pair_sum == 0:
                    result += f"{i}{j}"
    return result
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Сгенерированный пароль: {password}")
else:
    print("Ошибка: число должно быть в диапазоне от 3 до 20.")