def doors_status(num_doors):
    doors = [False] * num_doors
    
    for pass_num in range(1, num_doors + 1):
        for door in range(pass_num - 1, num_doors, pass_num):
            doors[door] = not doors[door]
    
    open_doors = [i + 1 for i, door in enumerate(doors) if door]
    return open_doors


open_doors = doors_status(100)
print(open_doors)


# O(n):
# def doors_status(n):
#     open_doors = [i * i for i in range(1, int(n**0.5) + 1)]
#     return open_doors

# open_doors = doors_status(100)
# print(open_doors)
