from statistics import mean

def print_statistics(sequence):
    print('minimum value = {}'.format(min(sequence)))
    print('maximum value = {}'.format(max(sequence)))
    print('number of elements in the sequence = {}'.format(len(sequence)))
    print('average value = {0:8.6f}'.format(mean(sequence)))

print_statistics([1, 4, 7, 8, 45, 24, 4.1, 222.432, 0.63])
