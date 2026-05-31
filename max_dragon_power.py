def max_dragon_power(n: int) -> int:
    # Малые случаи
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4  # 2*2 = 4

    # Общий случай N >= 5
    r = n % 3
    if r == 0:
        return 3 ** (n // 3)
    elif r == 1:
        return 3 ** ((n - 4) // 3) * 4
    else:  # r == 2
        return 3 ** (n // 3) * 2

# Основная программа
if __name__ == "__main__":
    n = int(input().strip())
    print(max_dragon_power(n))
