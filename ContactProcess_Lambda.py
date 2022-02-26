from random import randrange
import numpy as np
import matplotlib.pyplot as plt


# PROBLEM
# How many time-steps are needed for a population to go from all its individuals infected (i.e. = 1)
# to all individuals susceptibles (i.e. = 0)


# INPUT PARAMETERS
# The infection rate lambda starts is a positive number starting from 0.1
# Population of 10 individuals
# How many times the simulation is run in order to get the average time steps


# OUTPUTS
# Time-steps 




# Function to print the index of the neighbour for line graph
def return_neighbour_index(target_index, population):   
    if target_index == 0:
        target_neighbour_index = 1

    elif target_index == len(population) - 1:
        target_neighbour_index = target_index  - 1

    else:
        if np.random.rand() < 0.5:
            target_neighbour_index = target_index + 1
        else:
            target_neighbour_index = target_index - 1
    
    return target_neighbour_index 



# Function to return the time steps to get all vertices to state zero (i.e. susceptible)
def return_single_time_value(population_graph, lambda_input):
    time_to_completion = 0

    while sum(population_graph) > 0:
        target_index = randrange(len(population_graph))
        target_neighbour_index = None
        
        target_neighbour_index = return_neighbour_index(target_index, population_graph)
        
        if population_graph[target_index] == 1:
            probability = lambda_input / (1 + lambda_input)
            if np.random.rand() < probability:
                population_graph[target_neighbour_index] = 1
            else:
                population_graph[target_index] = 0
        time_to_completion += 1
    #print("MC",time_to_completion) #Debugging
    return time_to_completion 



# Function to return the average time steps of multiple simulations
def return_average_time_steps(lambda_input, number_of_runs):    
    total_time_steps = 0

    for i in range(0, number_of_runs):
        total_time_steps += return_single_time_value(np.array([1,1,1,1,1,1,1,1,1,1]), lambda_input)
    #print("Total",total_time_steps) #Debugging
    
    average = total_time_steps / number_of_runs
    return average




# Function to simulate the process
# lambda starts from 0.1, increases by 0.5 up to 1.
def simulate_to_lambda_1(number_of_runs):

    simulations = np.array([])
    array_of_lambdas = np.array([])
    lambda_index = 0.1

    while lambda_index <= 1:
        simulations = np.append(simulations, return_average_time_steps(lambda_index, number_of_runs))
        lambda_index += 0.1
        array_of_lambdas = np.append(array_of_lambdas, lambda_index)

    return simulations, array_of_lambdas


# Function to simulate the process
# lambda starts from 0.1, increases by 0.5 up to 5.
def simulate_to_lambda_5(number_of_runs):

    simulations = np.array([])
    array_of_lambdas = np.array([])
    lambda_index = 0.1

    while lambda_index <= 5:
        simulations = np.append(simulations, return_average_time_steps(lambda_index, number_of_runs))
        lambda_index += 0.5
        array_of_lambdas = np.append(array_of_lambdas, lambda_index)

    return simulations, array_of_lambdas



# FUNCTION CALLS
simuls1_100, lambdas1_100 = simulate_to_lambda_1(100)
simuls1_1000, lambdas1_1000 = simulate_to_lambda_1(1000)

simuls5_100, lambdas5_100 = simulate_to_lambda_5(100)
simuls5_1000, lambdas5_1000 = simulate_to_lambda_5(1000)



# PLOTS
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(15,10))
fig.suptitle('Evolution of the curve based on λ growing')

#Lambda goes from 0.1 to 1
ax1.plot(lambdas1_100, simuls1_100, label='100 runs', color='r')
ax1.plot(lambdas1_1000, simuls1_1000, label='1000 runs', color='b')
ax1.set_ylabel('Average time-steps', fontsize=(8))
ax1.set_xlabel('λ', fontsize=(8))
ax1.legend()


#Lambda goes from 0.1 to 5
ax3.plot(lambdas5_100, simuls5_100, label='100 runs', color='r')
ax3.plot(lambdas5_1000, simuls5_1000, label='1000 runs', color='b')
ax3.set_ylabel('Average time-steps', fontsize=(8))
ax3.set_xlabel('λ', fontsize=(8))
ax3.legend()


fig.savefig("Increasing lambda")








########################
'''
# Function to print the index of the neighbour for ring graph
def return_neighbour_index(target_index, population_graph):   
    if target_index == 0:
        target_neighbour_index = 1

    elif target_index == len(population_graph) - 1:
        target_neighbour_index = target_index  - 1
        
    elif np.random.rand() < (1/3):
        target_neighbour_index = target_index - 1
    
    elif  np.random.rand() < (2/3):
        target_neighbour_index = target_index
    
    else:
        target_neighbour_index = target_index + 1
    return target_neighbour_index
'''
