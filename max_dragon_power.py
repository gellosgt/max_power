def max_dragon_power(N: int) -> int:
    # Малые случаи
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 3
    if N == 4:
        return 4  # 2*2 = 4

    # Общий случай N >= 5
    r = N % 3
    if r == 0:
        return 3 ** (N // 3)
    elif r == 1:
        return 3 ** ((N - 4) // 3) * 4
    else:  # r == 2
        return 3 ** (N // 3) * 2

# Основная программа
if __name__ == "__main__":
    N = int(input().strip())
    print(max_dragon_power(N))