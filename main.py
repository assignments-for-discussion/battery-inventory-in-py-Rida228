def count_batteries_by_health(present_capacities):
    capacity = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
      }
  #calculating and classifying soh
    for capacity_ in present_capacities:
        soh = 100*(capacity_/120)
        if soh >= 80:
            capacity["healthy"] += 1
        elif soh < 80 and soh >= 65:
            capacity["exchange"] += 1
        else:
            capacity["failed"] += 1
    return capacity


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
