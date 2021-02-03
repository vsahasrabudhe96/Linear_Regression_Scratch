import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random



'''
Generation of random data   
'''
def create_data(num_points,variance,step=2,correlation='pos'):
    val=1
    ys = []
    for _ in range(num_points):
        y = val+random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation=='pos':
            val+=step
        elif correlation and correlation== 'neg':
            val-=step
    
    xs = [i for i in range(len(ys))] 
    return np.array(xs),np.array(ys)

'''
Now let's write the function for getting the slope and  y intercept
'''
def slope_intercept(x,y):
    slope = (np.mean(x)*np.mean(y) - np.mean(x*y))/(np.square(np.mean(x))-np.mean(np.square(x)) )
    intercept = np.mean(y) - slope*np.mean(x)
    return slope, intercept

'''

Writing the function for squared error between predicted and original
'''
def squared_error(y_or,y_line):
    return sum((y_line-y_or)**2)

'''

square_error_reg => square error between the original y and best fit line
square_error_y_mean => square error between the original y and list of mean value of y
r_squared = 1 - (square_error_reg/square_error_y_mean)


Higher the value of rsquared better is the result
'''

def coefficient_of_determination_rsquare(y_or,y_line):
    y_mean_line = [np.mean(y_or) for i in y_or]
    square_error_reg = squared_error(y_or,y_line)
    square_error_y_mean = squared_error(y_or,y_mean_line)
    return 1 - (square_error_reg/square_error_y_mean)


def main():
    x,y = create_data(40,40,2,correlation='pos')
    slope, intercept = slope_intercept(x,y)


    best_fit_line = [(slope*i) + intercept for i in x]

    new_point = np.random.rand()

    predict = slope*new_point + intercept

    r_squared = coefficient_of_determination_rsquare(y, best_fit_line)

    print(r_squared)
    plt.scatter(x,y)
    plt.scatter(new_point,predict,s=100,color='red')
    plt.plot(x,best_fit_line)
    plt.show()


if  __name__=='__main__':
    main()

