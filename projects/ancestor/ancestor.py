

# a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):

    # build an 'ancesters' list (models a reversed directed graph)
    anct_list = {}
    for i in ancestors:
        if i[1] not in anct_list:
            anct_list[i[1]] = [i[0]]
        else:
            anct_list[i[1]].append(i[0])

    # if 'starting node' has no parents it will not appear in the reversed graph
    if starting_node not in anct_list:
        return -1

    # depth first traversal
    stack = [[starting_node]]
    visited = set()
    visited.add(starting_node)
    results = []
    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        if current_node not in anct_list:
            if len(current_path) > len(results):
                results = current_path
            elif len(current_path) == len(results):
                if current_path[-1] < results[-1]:
                    results = current_path
        else:
            for i in anct_list[current_node]:
                if i not in visited:
                    visited.add(i)
                    new_path = current_path + [i]
                    stack.append(new_path)

    return results[-1]


# print(earliest_ancestor(a, 6))

# def earliest_ancestor(ancestors, starting_node):

#     # build an 'ancesters' list (models a reversed directed graph)
#     anct_list = {}
#     for i in ancestors:
#         if i[1] not in anct_list:
#             anct_list[i[1]] = [i[0]]
#         else:
#             anct_list[i[1]].append(i[0])

#     # if 'starting node' has no parents it will not appear in the reversed graph
#     if starting_node not in anct_list:
#         return -1

#     # depth first traversal
#     stack = [[starting_node]]
#     visited = set()
#     visited.add(starting_node)
#     results = []
#     while len(stack) > 0:
#         current_path = stack.pop()
#         current_node = current_path[-1]
#         if current_node not in anct_list:
#             results.append(current_path)
#         else:
#             for i in anct_list[current_node]:
#                 if i not in visited:
#                     visited.add(i)
#                     new_path = current_path + [i]
#                     stack.append(new_path)

#     # Find the longest path and return last value in the list
#     final = []
#     for i in results:
#         if len(i) > len(final):
#             final = i
#         elif len(i) == len(final):
#             if i[-1] < final[-1]:
#                 final = i

#     return final[-1]
