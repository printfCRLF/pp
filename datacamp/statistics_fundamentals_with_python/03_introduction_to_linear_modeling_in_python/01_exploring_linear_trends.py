import numpy as np
import matplotlib.pyplot as plt 

times = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.])
distances = np.array([0., 44.04512153, 107.16353484, 148.43674052, 196.39705633,  254.4358147 ,  300.])

def reasons_for_modeling_interpolation(): 
    total_distance = distances[-1] - distances[0]
    total_time = times[-1] - times[0]
    average_speed = total_distance / total_time
    elapse_time = 2.5
    distance_traveled = average_speed * elapse_time
    print("THe distance traveled is {}".format(distance_traveled))

    _ = plt.plot(times, distances, marker='.', linestyle='none', color='red')
    _ = plt.plot()
    _ = plt.xlabel('X Data,  Time Drive [hours]')
    _ = plt.ylabel('Y Data,  Distance Travelled [miles]')
    plt.show()


reasons_for_modeling_interpolation()