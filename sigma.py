import copy
lists = [[2,3],[4,5]]
newlists = []
newlists = copy.copy(lists)
lists[0][0] = 1
newlists[1][1] = 2
print(lists)
print(newlists)