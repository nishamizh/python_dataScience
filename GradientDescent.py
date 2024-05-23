import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,5,7,9,10])

def gradient_descent(x,y):
    m=0
    c=0
    learning_rate = 0.01
    number_of_steps = 1000
    n = len(x)

    for step in range(number_of_steps):
        y_pred = (m*x) + c
        cost = (1/n) * sum([val**2 for val in (y-y_pred)])   # [Sigma 1 to n (y- y_pred)^2]/n
        dm = (-2/n) * (sum(x * (y- y_pred)))
        dc = (-2/n) * (sum(y-y_pred))
        m = m-learning_rate * dm
        c = c-learning_rate * dc

        print(f'Slope = {m} , Intercept = {c}  **, Step = {step} , cost = {cost} ')

gradient_descent(x,y)

# the output shows cost =0.240000..... for n times, it means the model is converged. So we take that slope and intercept