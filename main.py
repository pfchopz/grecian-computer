# Script which finds all available solutions for Grecian Computer Puzzle

import json
import timeit

# Variables
solution_index = 1
disks = ["disk1", "disk2", "disk3", "disk4", "disk5"]
layers = ["layer1", "layer2", "layer3", "layer4"]
puzzle = {
    "disk1": {
        "layer1": [3, 0, 6, 0, 10, 0, 7, 0, 15, 0, 8, 0],
        "position": 0
    },
    "disk2": {
        "layer1": [7, 3, 0, 6, 0, 11, 11, 6, 11, 0, 6, 17],
        "layer2": [4, 0, 7, 15, 0, 0, 14, 0, 9, 0, 12, 0],
        "position": 0
    },
    "disk3": {
        "layer1": [9, 13, 9, 7, 13, 21, 17, 4, 5, 0, 7, 8],
        "layer2": [21, 6, 15, 4, 9, 18, 11, 26, 14, 1, 12, 0],
        "layer3": [5, 0, 10, 0, 8, 0, 22, 0, 16, 0, 9, 0],
        "position": 0
    },
    "disk4": {
        "layer1": [7, 0, 9, 0, 7, 14, 11, 0, 8, 0, 16, 2],
        "layer2": [9, 20, 12, 3, 6, 0, 14, 12, 3, 8, 9, 0],
        "layer3": [3, 26, 6, 0, 2, 13, 9, 0, 17, 19, 3, 12],
        "layer4": [1, 0, 9, 0, 12, 0, 6, 0, 10, 0, 10, 0],
        "position": 0
    },
    "disk5": {
        "layer1": [11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14, 11],
        "layer2": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 4],
        "layer3": [4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9, 4],
        "layer4": [3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8, 8],
    }
}

# Functions
def main(puzzle):
    while True:
        if check_solution(puzzle) == True:
            write_solution(puzzle)
        
        cycle = next_cycle(puzzle)
        if cycle["complete"]:
            break
        puzzle = cycle["state"]

def rotate_disk(disk) -> dict:
    for key in disk:
        if key != "position":
            disk[key] = disk[key][1:] + disk[key][:1]       
    disk["position"] = (disk["position"] + 1) % 12
    return disk
    
def next_cycle(state) -> dict:
    for disk in disks:
        if disk != "disk5":
            state[disk] = rotate_disk(state[disk])
            if state[disk]["position"] != 0:
                return {"state": state, "complete": False}
    return {"state": state, "complete": True}

def get_value(state, layer, column_index) -> int:
    for disk in disks:
        if layer in state[disk]:
            if state[disk][layer][column_index] != 0:
                return state[disk][layer][column_index]
    
def sum_column(state, column_index) -> int:  
    column = []
    for layer in layers:
        value = get_value(state, layer, column_index)
        column.append(value)
    return sum(column)

def check_solution(state) -> bool:
    for column in range(12):
            sum = sum_column(state, column)
            if sum != 42:
                return False
    return True

def write_solution(state) -> None:
    global solution_index
    json_object = json.dumps(state, indent=4)
    filename = f"solution-{solution_index}.json"
    with open(filename, "w") as outfile:
        outfile.write(json_object)
    solution_index += 1
        
if __name__ == "__main__":
    start = timeit.default_timer()
    main(puzzle)
    stop = timeit.default_timer()
    runtime = (stop - start) * 1000
    print('Runtime: %.2f ms' % runtime)