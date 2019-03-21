
import arx
import pandas as pd
#import tripleA_datacontainer

#dataset
dataset = pd.read_csv('data.csv', index_col=['datetime'])

# model configuration


input_labels = ('external_temp', 'external_humidity')


output_label = 'electric_consumption'

offset = False
minimum_input_delay = 0
inputs_maximum_delays = 1
ouput_maximum_delay = 2

# training data

training_starting_stringdatetime = '05/09/2018  00:04:30'
training_ending_stringdatetime = '31/10/2018 15:44:30'

# validation data

validation_starting_stringdatetime = '31/10/2018 15:54:30'
validation_ending_stringdatetime = '28/11/2018 23:34:30'

# display

correlation = False
pole_zeros = False

################################################

sample_time_in_minutes = 10

cycle = sample_time_in_minutes

print('TRAINING')

inputs = [dataset.iloc[0:8159][x] for x in input_labels]
print(inputs)
output = dataset.iloc[0:8159]['electric_consumption']
arx_model = arx.Arx(minimum_input_delay=minimum_input_delay, inputs_maximum_delays=inputs_maximum_delays, output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs, learning_output=output, offset=offset)
output_estimated = arx_model.simulate(inputs=inputs, output=output, cycle=cycle)
arx.plot_result(output_estimated, output, inputs)

if correlation:
    arx.plot_correlations(output_estimated, output, inputs, maxlags=5)
if pole_zeros:
    arx.plot_zeros_pole(arx_model.get_zeros(), arx_model.get_poles())
data = list(inputs)
data.append(output)

print('VALIDATION')


inputs = [dataset.iloc[8159:12237][x] for x in input_labels]
output = dataset.iloc[8159:12237]['electric_consumption']
output_estimated = arx_model.simulate(inputs=inputs, output=output)
print('y: %s' % output_label)
for i in range(len(input_labels)):
    print('u%i: %s' % (i, input_labels[i]))

data = list(inputs)
data.append(output)
arx.plot_result(output_estimated, output, inputs)
print(arx_model)
arx.show()
