
from copy import deepcopy
from pprint import pprint

x1, x2, x3, x4, x5, x6 = True, True, True, True, True, True


# result = ((not x5) or (not x3) or (x6) or (x1)) and (not x3) and ((not x2) or (not x4) or (not x5) or (not x1)) and ((not x5) or (x6)) and (not x3) and ((not x6) or (x4)) and (x4 or (not x3)) and (x6 or (not x1)) and (x4 or (not x2) or (not x1) or (not x6)) and (
# (not x2) or (not x3)) and ((not x5) or x1) and (x4 or (not x1)) and (not x6) and ((not x5) or x1) and ((not x6) or (not x3)) and (x2 or (not x6) or x1 or (not x3)) and ((not x4) or (not x2) or x6) and ((not x1) or (not x4) or x6) and (x3 or (not x1) or (not x6)) and (x4)


# strValue = "001010"

# x1, x2, x3, x4, x5, x6 = [int(w) for w in strValue]

strinit = [int(w) for w in list("001010")]


def bInver(num):
    return ~num & 1


def bInvered(num: list):
    """与えられたbit文字列の各桁を一つずつ反転したものをbit数作成する
    """
    result = []
    tmp = deepcopy(num)
    for i in range(len(num)):
        num = deepcopy(tmp)
        num[i] = bInver(tmp[i])
        num = "".join([str(w) for w in num])
        result.append(num)
    print(result)
    return result


def create_all_patternAnd_number_of_clauses():
    index = 0
    result = [
    ]

    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                for x4 in range(2):
                    for x5 in range(2):
                        for x6 in range(2):
                            Cs = [
                                [bInver(x5), bInver(x3), x6, x1],
                                [bInver(x3)],
                                [bInver(x2), bInver(x4),
                                 bInver(x5), bInver(x1)],
                                [bInver(x5), x6],
                                [bInver(x3)],
                                [bInver(x6), x4],
                                [x4, bInver(x3)],
                                [x6, bInver(x1)],
                                [x4, bInver(x2), bInver(x1), bInver(x6)],
                                [bInver(x2), bInver(x3)],
                                [bInver(x5), x1],
                                [x4, bInver(x1)],
                                [bInver(x6)],
                                [bInver(x5), x1],
                                [bInver(x6), bInver(x3)],
                                [x2, bInver(x6), x1, bInver(x3)],
                                [bInver(x4), bInver(x2), x6],
                                [bInver(x1), bInver(x4), x6],
                                [x3, bInver(x1), bInver(x6)],
                                [x4]
                            ]

                            count = 0
                            for a in Cs:
                                found_one = False
                                for b in a:
                                    if b == 1:
                                        found_one = True
                                        break
                                if found_one:
                                    count += 1

                            binary_combination = f'{x1}{x2}{x3}{x4}{x5}{x6}'
                            result.append(
                                {
                                    "index": index,
                                    "binary_combination": binary_combination,
                                    "clauses": count,
                                }
                            )
                            index += 1

                            # print(f"{binary_combination}:{count}")
    pprint(result)
    return result

# bInvered(strinit)
# create_all_patternAnd_number_of_clauses()


def listing():
    binversed_bits = bInvered(strinit)
    Listed = create_all_patternAnd_number_of_clauses()
    binary_combinations = [e["binary_combination"] for e in Listed]

    for e in binversed_bits:
        for ei in Listed:
            if e == ei["binary_combination"]:
                print(ei["index"])


listing()
