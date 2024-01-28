input_list = [1,2,3,4,5,6]
output_list = []

for i in input_list:
    output_list.append(i*i)
print(output_list)

def square(x):
    return x * x

output_list = map(square, input_list)
for o in output_list:
    print(o)