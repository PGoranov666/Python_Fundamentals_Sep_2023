data = input().split()

def merge(data, start, end):
    start = max(0, start)
    end = min(len(data) - 1, end)
    merged = ''.join(data[start:end + 1])
    data = data[:start] + [merged] + data[end + 1:]
    return data

def divide(data, index, partitions):
    element = data[index]
    partition_size = len(element) // partitions
    extra = len(element) % partitions
    divided = [element[i * partition_size:(i + 1) * partition_size] for i in range(partitions - 1)]
    divided.append(element[(partitions - 1) * partition_size:])
    data = data[:index] + divided + data[index + 1:]
    return data

while True:
    command = input().split()
    if command[0] == '3:1':
        break
    elif command[0] == 'merge':
        start, end = map(int, command[1:])
        data = merge(data, start, end)
    elif command[0] == 'divide':
        index, partitions = map(int, command[1:])
        data = divide(data, index, partitions)

print(' '.join(data))
