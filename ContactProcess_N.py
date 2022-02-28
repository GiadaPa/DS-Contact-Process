from random import randrange
import numpy as np
import matplotlib.pyplot as plt


# PROBLEM
# How many time-steps are needed for a population to go from all its individuals infected (i.e. = 1)
# to all individuals susceptibles (i.e. = 0)


# INPUT PARAMETERS
# The infection rate lambda is 0.1 and 0.9
# Size of the population inceases
# How many times the simulation is run in order to get the average time steps


# OUTPUTS
# Time-steps 



# POPULATION FUNCTIONS
def return_population(n):
    population = np.ones((n,), dtype=int)

    return np.array(population)

def reset_to_pop(old_population):
    old_population[old_population==0] = 1

    return np.array(old_population)



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
    
    return time_to_completion 



# Function to return the average time steps of multiple simulations
def return_average_time_steps(lambda_input, number_of_runs, pop_size):    
    total_time_steps = 0

    for i in range(0, number_of_runs):
        pop_size = reset_to_pop(pop_size) 
        total_time_steps +=  return_single_time_value(pop_size, lambda_input) 
          
    average = total_time_steps / number_of_runs
    return average



# Function to simulate the process
def simulate_pop_size(lambda_input, number_of_runs, pop_size):
    simulations = np.array([])
    individuals = np.array([])

    population_size = return_population(pop_size)

    while pop_size > 2:
        simulations = np.append(simulations, return_average_time_steps(lambda_input, number_of_runs, population_size))
        individuals = np.append(individuals, pop_size)
        pop_size -= 1000 #Change this value for different plots
        population_size = return_population(pop_size)
        
    return simulations, individuals


# FUNCTION CALLS POPULATION = 100
simuls, individuals = simulate_pop_size(0.1, 100, 100)
simuls1, individuals1 = simulate_pop_size(0.9, 100, 100)


# PLOTS POPULATION = 100
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
fig.suptitle('Evolution of the curve based on population size growing')

ax1.plot(individuals, simuls, label='100 runs  \nλ = 0.1', color='k')
ax1.set_ylabel('Average time-steps', fontsize=(8))
ax1.set_xlabel('Population size', fontsize=(8))
ax1.legend()

ax2.plot(individuals1, simuls1, label='100 runs  \nλ = 0.9', color='k')
ax2.set_ylabel('Average time-steps', fontsize=(8))
ax2.set_xlabel('Population size', fontsize=(8))
ax2.legend()

fig.savefig("Population_size_100")


#-----------------------------------------------------------------
# FUNCTION CALLS POPULATION = 1000
simuls, individuals = simulate_pop_size(0.1, 10, 1000)
simuls1, individuals1 = simulate_pop_size(0.9, 10, 1000)


# PLOTS POPULATION = 1000
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
fig.suptitle('Evolution of the curve based on population size growing')

ax1.plot(individuals, simuls, label='10 runs  \nλ = 0.1')
ax1.set_ylabel('Average time-steps', fontsize=(8))
ax1.set_xlabel('Population size', fontsize=(8))
ax1.legend()

ax2.plot(individuals1, simuls1, label='10 runs  \nλ = 0.9')
ax2.set_ylabel('Average time-steps', fontsize=(8))
ax2.set_xlabel('Population size', fontsize=(8))
ax2.legend()

fig.savefig("Population_size_1000")


#-----------------------------------------------------------------
# FUNCTION CALLS POPULATION = 5000
simuls, individuals = simulate_pop_size(0.1,5,5000)
simuls1, individuals1 = simulate_pop_size(0.9,5, 5000)


# PLOTS POPULATION = 5000
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
fig.suptitle('Evolution of the curve based on population size growing')

ax1.plot(individuals, simuls, label='5 runs  \nλ = 0.1', color='y')
ax1.set_ylabel('Average time-steps', fontsize=(8))
ax1.set_xlabel('Population size', fontsize=(8))
ax1.legend()

ax2.plot(individuals1, simuls1, label='5 runs  \nλ = 0.9', color='y')
ax2.set_ylabel('Average time-steps', fontsize=(8))
ax2.set_xlabel('Population size', fontsize=(8))
ax2.legend()

fig.savefig("Population_size_5000_2")

