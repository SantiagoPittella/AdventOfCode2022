# Day 1 solution is pretty nasty. Had a ton of thing done that day. Sorry for this haha.

def part_a():
    with open("day1.input") as f:
        max_sum = 0
        actual_sum = 0
        for line in f:
            line = line.strip()
            if line == "":
                if actual_sum > max_sum:
                    max_sum = actual_sum
                actual_sum = 0
            else:
                actual_sum += int(line)
        print(f"max sum: {max_sum}")
        print(f"actual_sum: {actual_sum}")

part_a()

def part_b():
    with open("day1.input") as f:
        sums = []
        actual_sum = 0
        for line in f:
            line = line.strip()
            if line == "":
                sums.append(actual_sum)
                actual_sum = 0
            else:
                actual_sum += int(line)
        sums.sort()
        sums.reverse()
        print(f"sums sorted: {sums}")
        print(f"max 3 sum: {sum(sums[:3])}")

part_b()
