def rev_list(aList, result_list):
    if len(aList) == 1:
        result_list.append(aList.pop())
        return result_list
    else:
        result_list.append(aList.pop())
        rev_list(aList, result_list)
        return result_list


print(rev_list([1,2,3],[]))
