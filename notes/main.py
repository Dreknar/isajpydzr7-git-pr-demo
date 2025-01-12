def even_and_odd_counter(numbers: list[int]) -> dict:
    counter = {
        "even": 0,
        "odd": 0
    }

    for number in numbers:
        try:
            if int(number) % 2 == 0:
                counter["even"] += 1
            else:
                counter["odd"] += 1
        except ValueError:
            continue

    return counter

if __name__ == '__main__':
    print(even_and_odd_counter([1, 2, 3, 4, 5]))
    print(even_and_odd_counter(["10", 2, "12", 23.0]))
    print(even_and_odd_counter([10, 12, "A", "TEST", 3]))