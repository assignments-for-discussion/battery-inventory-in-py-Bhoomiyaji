def count_batteries_by_usage(cycles, low, med):
    hashset = {"lowCount": 0, "mediumCount": 0, "highCount": 0}

    for c in cycles:

        if c < low:
            hashset["lowCount"] += 1

        elif low <= c <= med:
            hashset["mediumCount"] += 1

        else:
            hashset["highCount"] += 1

    return hashset


def test_bucketing_by_number_of_cycles_preset():
    cycles_list = [100, 200, 300, 399, 400, 500, 600, 900, 919, 920, 999, 1000]

    low_count, med_count = 400, 919

    counts = count_batteries_by_usage(cycles_list, low = low_count, med = med_count)

    print("Count\tValue")
    for k, v in counts.items():
        print(f"{k}\t{v}")

    assert(counts["lowCount"] == 4)
    assert(counts["mediumCount"] == 5)
    assert(counts["highCount"] == 3)

    print("Done counting")


def test_bucketing_by_number_of_cycles_user_input():
    
    def ordinal(num):
        if num == 1:
            return "st"

        elif num == 2:
            return "nd"

        elif num == 3:
            return "rd"

        return "th"

    n = int(input("Enter the number of cycles: "))

    cycles_list = list()
    for i in range(n):
        cycles_list.append(int(input(f"Enter the {i+1}{ordinal(i+1)} cycle: ")))
    
    low_count = int(input("Enter the low count: "))
    med_count = int(input("Enter the medium count: "))

    counts = count_batteries_by_usage(cycles_list, low=low_count, med=med_count)
    
    print("Count\tValue")
    for k, v in counts.items():
        print(f"{k}\t{v}")

    print("Done counting")


def main():
    print("1. To use preset values.\n2. To input your values\n")
    option = int(input("Enter your choice:"))

    print("\nCounting batteries by usage cycles...\n")

    if option == 1:
        return test_bucketing_by_number_of_cycles_preset()

    elif option == 2:
        return test_bucketing_by_number_of_cycles_user_input()

    else:
        return print("Invalid input")


if __name__ == "__main__":
    main()

