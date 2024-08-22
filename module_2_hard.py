def generate_password(n):
    password = ""
    pairs = []
    for i in range(1, 21):
        for j in range(i, 21):
            if i != n and j != n:
                pair_sum = i + j
                if n % pair_sum == 0:
                    pairs.append(f"{i}{j}")
    password = ''.join(pairs)
    return password
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print("Нужный пароль:", result)
else:
    print("Число должно быть от 3 до 20.")