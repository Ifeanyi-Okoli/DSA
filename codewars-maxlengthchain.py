
# def len_longest_chain(pairs):
#     #Your code here
#     sorted_pairs = sorted(pairs, key=lambda x: x[0])
#     valid_pairs = [sorted_pairs[0]]
#     for i in range(1, len(sorted_pairs)):
#         if valid_pairs[-1][1] < sorted_pairs[i][0]:
#             valid_pairs.append(sorted_pairs[i])
#             # sorted_pairs[i] = None
#     return len(valid_pairs)


def len_longest_chain(pairs):
    if not pairs:
        return 0

    # Sort by the second element
    sorted_pairs = sorted(pairs, key=lambda x: x[1])

    last_end = sorted_pairs[0][1]
    count = 1

    for i in range(1, len(sorted_pairs)):
        if sorted_pairs[i][0] > last_end:
            count += 1
            last_end = sorted_pairs[i][1]

    return count


print(len_longest_chain([(2, 3), (3, 4), (3, 5)]))
print(len_longest_chain([(2, 3), (3, 4), (1, 2)]))
print(len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]))
print(len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]))
