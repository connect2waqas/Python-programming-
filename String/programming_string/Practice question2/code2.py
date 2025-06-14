def sorting(ages):
    asending_order= sorted(ages)
    descending_order = sorted(asending_order,reverse=True)

    print(asending_order)
    print(descending_order)

ages = [12,32,45,23,55,33,34,54,56,67]
sorting(ages)