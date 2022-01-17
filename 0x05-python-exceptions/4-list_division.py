#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_3 = []
    val3 = 0
    for i in range(list_length):
        try:
            val3 = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            val3 = 0
            print("division by 0")
        except TypeError:
            val3 = 0
            print("wrong type")
        except IndexError:
            val3 = 0
            print("out of range")
        finally:
            list_3.append(val3)
    return list_3
