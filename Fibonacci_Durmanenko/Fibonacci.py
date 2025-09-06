def fibonacci(steps, array):
    if steps == 0:
        return array
    if len(array) >= 2:
        array.append(array[-1] + array[-2])
        steps = steps - 1
        return fibonacci(steps, array)
    else:
        return array
def fibonaccirange(start, end, array):
    if len(array) < 2:
        return array
    lastvalue = array[-1]
    if lastvalue >= end:
        result = []
        for elem_array in array:
            if elem_array >= start and elem_array <= end:
                result.append(elem_array)
        return result
    array.append(array[-1] + array[-2])
    return fibonaccirange(start, end, array)
with open('input_2_numbers.txt', 'r') as file:
    lines = file.readlines()
    numbers = [float(i) for i in lines]
with open('fibonacci_steps.txt', 'r') as file:
    lines = file.readline()
    steps = int(lines)
with open('range_start_end.txt', 'r') as file:
    lines = file.readlines()
    startrange = int(lines[0])
    endrange = int(lines[1])
fibonaccimanual = fibonacci(steps, numbers)
fibonaccirange = fibonaccirange(startrange, endrange, numbers.copy())
with open('output.txt', 'w') as file:
    file.write("Algorithm Fibonacci with " + str(steps) + " steps:\n")
    file.write(' '.join(map(str, fibonaccimanual)))
    file.write("\nAlgorithm Fibonacci in range from " + str(startrange) + " to " + str(endrange) + ":\n")
    file.write(' '.join(map(str, fibonaccirange)))