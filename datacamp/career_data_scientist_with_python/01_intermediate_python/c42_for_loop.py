def loop_over_a_list():
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]
    for a in areas:
        print(a)


def loop_over_a_list_with_enumerate():
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]
    for i, a in enumerate(areas):
        print("room {0}: {1}".format(i, a))


def loop_over_a_list_with_enumerate2():
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]
    for index, area in enumerate(areas):
        print("room " + str(index + 1) + ": " + str(area))


if __name__ == "__main__":
    # loop_over_a_list()
    # loop_over_a_list_with_enumerate()
    loop_over_a_list_with_enumerate2()
