def generate_password(n):
    password = ""
    pairs = []

    for i in range(1, 21):
        for j in range(i+1, 21):
               if i != n and j != n:
                pair_sum = i + j
                if n % pair_sum == 0:
                    pairs.append(f"{i}{j}")
    password = ''.join(pairs)
    return password
for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")