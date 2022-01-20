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

    print("Count\t\tValue")
    for k, v in counts.items():
        print(f"{k}\t{v}")

    assert(counts["lowCount"] == 4)
    assert(counts["mediumCount"] == 5)
    assert(counts["highCount"] == 3)

    print("Done counting")



def main():
  
    test_bucketing_by_number_of_cycles_preset()

   
if __name__ == "__main__":
    main()
