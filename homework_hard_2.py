def generate_password(n):
    if n < 3 or n > 20:
        return "Число n должно быть в диапазоне от 3 до 20"

    password = ""
    for i in range(1, n):
        for j in range(i, n):
            if (i + j) % n == 0:
                password += str(i) + str(j)
    return password


n = 5
result = generate_password(n)
print(f"Для числа {n} нужный пароль: {result}")