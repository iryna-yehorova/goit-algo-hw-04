import random
import timeit


def insertion_sort(numbers):
    result = numbers.copy()
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def make_data(size):
    rng = random.Random(42)
    random_data = [rng.randint(0, size) for _ in range(size)]
    sorted_data = sorted(random_data)
    nearly_sorted = sorted_data.copy()
    for _ in range(max(1, size // 100)):
        a = rng.randrange(size)
        b = rng.randrange(size)
        nearly_sorted[a], nearly_sorted[b] = nearly_sorted[b], nearly_sorted[a]

    return {
        "random": random_data,
        "sorted": sorted_data,
        "reversed": sorted_data[::-1],
        "nearly sorted": nearly_sorted,
    }


if __name__ == "__main__":
    algorithms = {
        "insertion": insertion_sort,
        "merge": merge_sort,
        "Timsort (sorted)": sorted,
    }

    print("| Data | Size | Insertion (ms) | Merge (ms) | Timsort (ms) |")
    print("|---|---:|---:|---:|---:|")

    for size in (1000, 3000, 10000):
        for data_name, data in make_data(size).items():
            expected = sorted(data)
            times = []
            for algorithm in algorithms.values():
                assert algorithm(data) == expected
                measurements = timeit.repeat(
                    lambda: algorithm(data), repeat=3, number=1
                )
                times.append(min(measurements) * 1000)

            print(
                f"| {data_name} | {size} | "
                f"{times[0]:.3f} | {times[1]:.3f} | {times[2]:.3f} |"
            )
