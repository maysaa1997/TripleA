import arx
import pandas as pd


data = pd.read_csv("wholedata.csv")


# model configuration


input_labels = ('external_temp', 'external_humidity', 'Total Precipitation', 'Total Cloud Cover', 'Shortwave Radiation','Wind Speed', 'Wind Direction', 'Snowfall Amount')

output_label = 'value'


offset = False

minimum_input_delay = 0
inputs_maximum_delays = 0
ouput_maximum_delay = 1

# training data

training_starting_stringdatetime = '01/10/2018 0:00:00'
training_ending_stringdatetime = '31/01/2019 23:00:00'

# validation data

validation_starting_stringdatetime = '01/02/2019 0:00:00'
validation_ending_stringdatetime = '27/02/2019 23:00:00'

# display

correlation = True
pole_zeros = True

################################################

print('TRAINING')
print('#####################################################')


inputs = list()

#external_temp
input1 = list()

#external_humidity
input2 = list()

#Total Precipitation
input3 = list()

#Total Cloud Cover
input4 = list()

#Shortwave Radiation
input5 = list()

#Wind Speed
input6 = list()

datetimetrain = list()

for x in range(0, 10050):
    datetimetrain.append(data.iloc[x]['fulldate'])


for x in range(0, 10050):
    input1.append(data.iloc[x]['external_temp'])
inputs.append(input1)
for x in range(0, 10050):
    input2.append(data.iloc[x]['external_humidity'])
inputs.append(input2)
for x in range(0, 10050):
    input3.append(data.iloc[x]['Wind Direction'])
inputs.append(input3)

for x in range(0, 10050):
    input5.append(data.iloc[x]['Shortwave Radiation'])
inputs.append(input5)
for x in range(0, 10050):
    input6.append(data.iloc[x]['Wind Speed'])
inputs.append(input6)

print('Inputs for training')
print(inputs)


output = list()
for x in range(0, 10050):
    output.append(data.iloc[x]['value'])


print('Outputs for training')
print(output)


arx_model = arx.Arx(minimum_input_delay=minimum_input_delay, inputs_maximum_delays=inputs_maximum_delays, output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs, learning_output=output, offset=offset)

output_estimated = arx_model.simulate(cycle=60)
arx.plot_result(output_estimated, output, datetimetrain, inputs)
if correlation:
    arx.plot_correlations(output_estimated, output, inputs, maxlags=5)
if pole_zeros:
    arx.plot_zeros_pole(arx_model.get_zeros(), arx_model.get_poles())

print('VALIDATION')
print('#####################################################/n')


inputs_valid = list()

input7 = list()
input8 = list()
input9 = list()
input10 = list()
input11 = list()
input12 = list()

datetimevalid = list()

for x in range(10051, 10152):
    datetimevalid.append(data.iloc[x]['fulldate'])


for x in range(10051, 10152):
    input7.append(data.iloc[x]['external_temp'])
inputs_valid.append(input5)
for x in range(10051, 10152):
    input8.append(data.iloc[x]['external_humidity'])
inputs_valid.append(input8)
for x in range(10051, 10152):
    input9.append(data.iloc[x]['Wind Direction'])
inputs_valid.append(input9)
for x in range(10051, 10152):
    input11.append(data.iloc[x]['Shortwave Radiation'])
inputs_valid.append(input11)
for x in range(10051, 10152):
    input12.append(data.iloc[x]['Wind Speed'])
inputs_valid.append(input12)


print("Inputs for validation:")
print(inputs_valid)


output_valid = list()
for x in range(10051, 10152):
    output_valid.append(data.iloc[x]['value'])


print("Output for validation:")
print(output_valid)


output_estimated = arx_model.simulate(inputs=inputs_valid, output=output_valid)


print('y: %s' % output_label)

for i in range(len(input_labels)):
    print('u%i: %s' % (i, input_labels[i]))

arx.plot_result(output_estimated, output_valid, datetimevalid, inputs_valid)
print(arx_model)
arx.show()

