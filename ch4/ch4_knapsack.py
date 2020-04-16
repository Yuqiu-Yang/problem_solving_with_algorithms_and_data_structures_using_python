from copy import deepcopy
def knapsack(W, item_list):
    # we will take into consideration
    # the situations that there are duplicate weights,
    # constraints on number of each items to take etc.
    dp_value_list = []
    for i in range(W + 1):
        # the first entry would be the value
        # the second entry would hold the ids
        # since there might be constraints on quantities of each item
        dp_value_list.append([0,[0]])
    for i in range(W + 1):
        if i == 0:
            continue
        for j in range(min([(i + 1), max(item_list[1]) + 1])):
            # We do not need to worry about combining two
            # or more previous results since all previous
            # results are constructed by adding items one by one
            # to the list. If the list not optimal during this search
            # it won't be optimal however you split it
            ############################################
            # for every weight deduction, we need to find
            # all possible items
            candidate_list = findCandidate(j, item_list)
            if len(candidate_list) == 0:
                if (dp_value_list[i-j][0]) >= (dp_value_list[i][0]):
                    dp_value_list[i][0] = dp_value_list[i - j][0]
                    dp_value_list[i][1] = deepcopy(dp_value_list[i - j][1])
            else:
                for id in candidate_list:
                    temp_ind = (item_list[0]).index(id)
                    temp_weight = item_list[1][temp_ind]
                    if  ((dp_value_list[i - temp_weight][0] + \
                        (item_list[2])[temp_ind]) >= dp_value_list[i][0]) and \
                        (dp_value_list[i - temp_weight][1].count(id) + 1 <= item_list[3][temp_ind]):
                        dp_value_list[i][0] = (dp_value_list[i - temp_weight][0] + (item_list[2])[temp_ind])
                        temp = deepcopy(dp_value_list[i - temp_weight][1])
                        temp.append(id)
                        dp_value_list[i][1] = deepcopy(temp)


    return dp_value_list

def findCandidate(weight, item_list):
    candidate_list = []
    for i in range(len(item_list[0])):
        if item_list[1][i] <= weight:
            candidate_list.append(item_list[0][i])
    return candidate_list


item_list = []
id_list = [1,2,3,4,5]
weight_list = [2,3,4,5,9]
value_list = [5,6,8,8,10]
quantity_list = [2,1,1,1,1]
item_list.append(id_list)
item_list.append(weight_list)
item_list.append(value_list)
item_list.append(quantity_list)


print(knapsack(5, item_list))
