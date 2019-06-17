import arx
import pandas as pd
import numpy as np
import SALib.sample.morris
import SALib.analyze.morris
from matplotlib.pylab import *

number_of_trajectories = 1200
number_of_levels = 4



def avg_values(T_in_estimate):
    n = len(T_in_estimate)
    room_temperatures_avg = sum([abs(temperature) for temperature in T_in_estimate]) / n
    return room_temperatures_avg



if __name__ == '__main__':
    print('Reading database')

    minimum_input_delay = 0
    inputs_maximum_delays = 0
    ouput_maximum_delay = 1
    offset = False

    pset = pd.read_csv("whole2.csv")

    inputs = list()
    input1 = list()
    input2 = list()
    input3 = list()
    input5 = list()
    input6 = list()
    input7 = list()
    input8 = list()
    input9 = list()

    datetimetrain = list()
    for x in range(0, 10151):
        datetimetrain.append(pset.iloc[x]['fulldate'])

    for x in range(0, 10151):
        input1.append(pset.iloc[x]['external_temp'])
    inputs.append(input1)
    for x in range(0, 10151):
        input2.append(pset.iloc[x]['external_humidity'])
    inputs.append(input2)
    for x in range(0, 10151):
        input3.append(pset.iloc[x]['Total Precipitation'])
    inputs.append(input3)

    for x in range(0, 10151):
        input5.append(pset.iloc[x]['Total Cloud Cover'])
    inputs.append(input5)
    for x in range(0, 10151):
        input6.append(pset.iloc[x]['Shortwave Radiation'])
    inputs.append(input6)
    for x in range(0, 10151):
        input7.append(pset.iloc[x]['Wind Speed'])
    inputs.append(input7)
    for x in range(0, 10151):
        input8.append(pset.iloc[x]['Wind Direction'])
    inputs.append(input8)
    for x in range(0, 10151):
        input9.append(pset.iloc[x]['Snowfall Amount'])
    inputs.append(input9)

    print('Inputs for training')
    print(inputs)

    output = list()
    for x in range(0, 10151):
        output.append(pset.iloc[x]['value'])

    arx_model = arx.Arx(minimum_input_delay=minimum_input_delay, inputs_maximum_delays=inputs_maximum_delays,
                        output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs, learning_output=output,
                        offset=offset)


    input_labels = ('external_temp', 'external_humidity', 'Total Precipitation', 'Total Cloud Cover', 'Shortwave Radiation',
                    'Wind Speed', 'Wind Direction', 'Snowfall Amount')

    output_label = 'value'



    problem = dict()
    problem['num_vars'] = 0
    problem['names'] = []
    problem['bounds'] = []
    for parameter_name in input_labels:

        problem['num_vars'] += 1
        problem['names'].append(parameter_name)
        problem['bounds'].append([pset[parameter_name].min(), pset[parameter_name].max()])
    print("problem", problem)
    print('Generating parameter values')
    parameter_value_sets = SALib.sample.morris.sample(problem, number_of_trajectories, num_levels=number_of_levels)
    print('parameter value sets', parameter_value_sets, sep='\n')
    output_value_sets = []

    print('Simulating')

    expected_output_ref = avg_values(output)
    simulation_id = 0
    estimated_output = arx_model.simulate(inputs=inputs, output=output)
    corrected = np.array(estimated_output)
    print(parameter_value_sets.dtype)


    print(estimated_output)
    print(np.isnan(output_value_sets))
    for i in range(len(output_value_sets)):
        if isnan(output_value_sets[i]) == True:
            print('replacing nan value')
            output_value_sets[i] = 0.2
    print(output_value_sets)
    output_value_sets = array(output_value_sets)
    print('OVS', output_value_sets)
    print('Analyzing simulation results')
    print(len(parameter_value_sets), len(corrected))
    results = SALib.analyze.morris.analyze(problem, parameter_value_sets, corrected, conf_level=0.95,
                                           print_to_console=True, num_levels=number_of_levels)
    print ('results : ', results, sep='\n')
    fig, ax = subplots()
    ax.scatter(results['mu_star'], results['sigma'])
    for i in range(problem['num_vars']):
        ax.annotate(problem['names'][i], (results['mu_star'][i], results['sigma'][i]))
    show()