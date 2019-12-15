#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Dec 2019
# This program shows the average of numbers in 2d array

import random


def calculate_average(passed_in_2D_list):
    # this function calculates the average

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    average = total / (len(row_value) * len(passed_in_2D_list))

    return average


def main():
    # this function shows the average of numbers in 2d array

    a_2d_list = []

    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(1, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    average = calculate_average(a_2d_list)
    print("The average of random numbers in 2d array is: {:.2f} "
          .format(average))


if __name__ == "__main__":
    main()
