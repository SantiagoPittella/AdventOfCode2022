# --- Part One ---
# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

def get_priority_from_char(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96
    
def get_repeated_item(tuple):
    (list_1, list_2) = tuple
    for item in list_1:
        if item in list_2:
            return item

def separate_compartments(string):
    first_half = string[:len(string) // 2]
    second_half = string[len(string) // 2:]
    return (first_half, second_half)


def calculate_total_points_part_1():
    with open("day3.input") as f:
        return sum(list(map(lambda x: get_priority_from_char(get_repeated_item(separate_compartments(x))), f)))

print(f"PART 1:\n result: {calculate_total_points_part_1()}")

# --- Part Two ---
# As you finish identifying the misplaced items, the Elves come to you with another issue.

# For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

# Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

# Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

def get_group_badge(str1, str2, str3):
    for item in str1:
        if item in str2 and item in str3:
            return item


def calculate_total_points_part_2():
    with open("day3.input") as f:
        badges = []
        f = list(f)
        for (index, line) in enumerate(f[::3]):
            first = f[index * 3]
            second = f[(index * 3) + 1]
            third = f[(index * 3) + 2]
            badge = get_group_badge(first, second, third)
            badges.append(badge)
        return sum(list(map(get_priority_from_char, badges)))

print(f"PART 2:\n result: {calculate_total_points_part_2()}")
