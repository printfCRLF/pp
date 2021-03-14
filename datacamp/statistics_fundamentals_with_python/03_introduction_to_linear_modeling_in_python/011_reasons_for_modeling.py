import numpy as np
import matplotlib.pyplot as plt 
import util 

times = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.])
distances = np.array([0., 44.04512153, 107.16353484, 148.43674052, 196.39705633,  254.4358147 ,  300.])

def plot_abline(slope, intercept): 
    x = np.array([0, 100])
    y = slope * x + intercept
    _ = plt.plot(x, y)

def reasons_for_modeling_interpolation(): 
    total_distance = distances[-1] - distances[0]
    total_time = times[-1] - times[0]
    average_speed = total_distance / total_time
    elapse_time = 2.5
    distance_traveled = average_speed * elapse_time
    print("THe distance traveled is {}".format(distance_traveled))
    x = np.array([0, 10])
    y = 50 * x + 0;

    _ = plt.plot(times, distances, marker='.', linestyle='none', color='red')
    _ = plt.plot(x, y, color='black')
    _ = plt.xlabel('X Data,  Time Drive [hours]')
    _ = plt.ylabel('Y Data,  Distance Travelled [miles]')
    plt.show()

def reasons_for_modeling_extrapolation(): 
    # Select a time not measured.
    time = 8

    # Use the model to compute a predicted distance for that time.
    distance = util.model1(time)

    # Inspect the value of the predicted distance traveled.
    print(distance)

    # Determine if you will make it without refueling.
    answer = (distance <= 400)
    print(answer)

# Complete the function to model the efficiency.
def efficiency_model(miles, gallons):
    return np.mean( miles / gallons )

def reasons_for_modeling_estimating_relationships(): 
    car1 = {'gallons': np.array([  0.03333333,   1.69666667,   3.36      ,   5.02333333,
          6.68666667,   8.35      ,  10.01333333,  11.67666667,
         13.34      ,  15.00333333,  16.66666667]),
            'miles': np.array([   1. ,   50.9,  100.8,  150.7,  200.6,  250.5,  300.4,  350.3,
                    400.2,  450.1,  500. ])}
    
    car2 = {'gallons': np.array([  0.02 ,   1.018,   2.016,   3.014,   4.012,   5.01 ,   6.008,
          7.006,   8.004,   9.002,  10.   ]),
            'miles': np.array([   1. ,   50.9,  100.8,  150.7,  200.6,  250.5,  300.4,  350.3,
                    400.2,  450.1,  500. ])}

    # Use the function to estimate the efficiency for each car.
    car1['mpg'] = efficiency_model(car1['miles'] , car1['gallons'] )
    car2['mpg'] = efficiency_model(car2['miles'] , car2['gallons'] )

    # Finish the logic statement to compare the car efficiencies.
    if car1['mpg'] > car2['mpg'] :
        print('car1 is the best')
    elif car1['mpg'] < car2['mpg'] :
        print('car2 is the best')
    else:
        print('the cars have the same efficiency')    

#reasons_for_modeling_interpolation()
#reasons_for_modeling_extrapolation()
reasons_for_modeling_estimating_relationships()

