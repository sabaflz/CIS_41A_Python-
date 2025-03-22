# CIS 41A
# Ch.12, Ex.1
# Saba Feilizadeh
# Read the CSV file "order.csv"
# Write the total in the CSV file "outputfile.csv"

import csv
# ------------------------------------------------------
if __name__ == "__main__":
    order_dict = dict()

    with open("ch12_ex1/order.csv") as infile:
        reader = csv.reader(infile)

        for line in reader:
            order_dict[line[0]] = list()

            for quantity in line[1:]:
                order_dict[line[0]].append(int(quantity))

    total_order_dict = dict()
    for key, value in order_dict.items():
        sum = 0
        for quantity in value:
            sum += quantity

        total_order_dict[key] = sum

    expected_result_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}
    assert expected_result_dict['1'] == 91 , "The actual result is not the \
    same as expected result for the order number 1!"
    assert expected_result_dict['2'] == 100 , "The actual result is not the \
    same as expected result for the order number 2!"
    assert expected_result_dict['3'] == 32 , "The actual result is not the \
    same as expected result for the order number 3!"
    assert expected_result_dict['4'] == 62 , "The actual result is not the \
    same as expected result for the order number 4!"
    assert expected_result_dict['5'] == 64 , "The actual result is not the \
    same as expected result for the order number 5!"


    with open("ch12_ex1/" + "outputfile.csv", 'w') as outfile:
        writer = csv.writer(outfile)

        for key, value in total_order_dict.items():
            writer.writerow([key,value])
# ------------------------------------------------------ 