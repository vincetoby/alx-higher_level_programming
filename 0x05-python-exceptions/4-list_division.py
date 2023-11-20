#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listed = []
    for i in range(0, list_length):
        try:
            liste = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            liste = 0
        except ZeroDivisionError:
            print("division by 0")
            liste = 0
        except IndexError:
            print("out of range")
            liste = 0
        except Exception as a:
            pass
        finally:
            listed.append(liste)
    return listed
