# Script which finds all available solutions for Grecian Computer Puzzle

import json

puzzle = {
    "disc1": {
        "layer1": [3, 0, 6, 0, 10, 0, 7, 0, 15, 0, 8, 0],
        "position": 0
    },
    "disc2": {
        "layer1": [7, 3, 0, 6, 0, 11, 11, 6, 11, 0, 6, 17],
        "layer2": [4, 0, 7, 15, 0, 0, 14, 0, 9, 0, 12, 0],
        "position": 0
    },
    "disc3": {
        "layer1": [9, 13, 9, 7, 13, 21, 17, 4, 5, 0, 7, 8],
        "layer2": [21, 6, 15, 4, 9, 18, 11, 26, 14, 1, 12, 0],
        "layer3": [5, 0, 10, 0, 8, 0, 22, 0, 16, 0, 9, 0],
        "position": 0
    },
    "disc4": {
        "layer1": [7, 0, 9, 0, 7, 14, 11, 0, 8, 0, 16, 2],
        "layer2": [9, 20, 12, 3, 6, 0, 14, 12, 3, 8, 9, 0],
        "layer3": [3, 26, 6, 0, 2, 13, 9, 0, 17, 19, 3, 12],
        "layer4": [1, 0, 9, 0, 12, 0, 6, 0, 10, 0, 10, 0],
        "position": 0
    },
    "disc5": {
        "layer1": [11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14, 11],
        "layer2": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 4],
        "layer3": [4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9, 4],
        "layer4": [3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8, 8],
    }
}

def main():
    global puzzle
    cycle = puzzle
    solution_index = 1
    
    while True:
        result = check_solution(puzzle)
        
        if result == True:
            json_object = json.dumps(puzzle, indent=4)
            filename = "solution-" + str(solution_index) + ".json"
            with open(filename, "w") as outfile:
                outfile.write(json_object)
            solution_index += 1
        
        cycle = next_cycle(puzzle)
        
        if not cycle[1]:
            break
        
        puzzle = cycle[0]

def rotate_disc(disc) -> dict:
    for key in disc:
        if key != "position":
            disc[key] = disc[key][1:] + disc[key][:1]       
    disc["position"] = (disc["position"] + 1) % 12
    return disc
    
def next_cycle(state) -> list[dict, bool]:
    state["disc1"] = rotate_disc(state["disc1"])
    if state["disc1"]["position"] == 0:
        state["disc2"] = rotate_disc(state["disc2"])
        if state["disc2"]["position"] == 0:
            state["disc3"] = rotate_disc(state["disc3"])
            if state["disc3"]["position"] == 0:
                state["disc4"] = rotate_disc(state["disc4"])
                if state["disc4"]["position"] == 0:
                    return state, False
    return state, True

def get_value(state, layer, column_index) -> int:
    discs = ["disc1", "disc2", "disc3", "disc4", "disc5"]
    
    for disc in discs:
        if layer in state[disc]:
            if state[disc][layer][column_index] != 0:
                return state[disc][layer][column_index]
    
def sum_column(state, column_index) -> int:
    layers = ["layer1", "layer2", "layer3", "layer4"]
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
        
if __name__ == "__main__":
    main()