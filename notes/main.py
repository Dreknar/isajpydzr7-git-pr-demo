def even_and_odd_counter(numbers: list[int]) -> dict:
    counter = {
        "even": 0
        "odd": 0
    }

    for number in numbers
        if number % 2 == 0
            counter["even"] += 1
        else:
            counter["odd"] += 1

        return counter