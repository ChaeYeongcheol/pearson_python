import math


def sim_msd(data,name1,name2):
    sum = 0
    count = 0
    for resultData in data[name1]:
        if resultData in data[name2]:
            sum += pow(data[name1][resultData] - data[name2][resultData],2)
            count+=1
        return 1/(1+(sum/count))


def sim_pearson(data,name1,name2):
    avg_name1 = 0
    avg_name2 = 0
    count =0
    for resultData in data[name1]:
        if resultData in data[name2]:
            avg_name1 = data[name1][resultData]
            avg_name2 = data[name2][resultData]
            count += 1

    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0

    for resultData in data[name1]:
        if resultData in data[name2]:
            sum_name1 += pow(data[name1][resultData] - avg_name1,2)
            sum_name2 += pow(data[name2][resultData] - avg_name1,2)
            sum_name1_name2 += (data[name1][resultData] - avg_name1) * (data[name2][resultData] - avg_name2)

    return sum_name1_name2/(math.sqrt(sum_name1) * math.sqrt(sum_name2))


if __name__ == "__main__":
    import sys
    rows = 10
    cols = 5
    arr = [[0] * cols] * rows

    sim_msd(arr, 'Dave', 'Alex')
    sim_pearson(arr, 'Dave', 'Alex')

