# Script which finds all available solutions for Grecian Computer Puzzle

import json

puzzle = {
    "disk1": {
        "layer1": [3, 0, 6, 0, 10, 0, 7, 0, 15, 0, 8, 0],
        "position": 0
    },
    "disk2": {
        "layer1": [4, 0, 7, 15, 0, 0, 14, 0, 9, 0, 12, 0],
        "layer2": [7, 3, 0, 6, 0, 11, 11, 6, 11, 0, 6, 17],
        "position": 0
    },
    "disk3": {
        "layer1": [5, 0, 10, 0, 8, 0, 22, 0, 16, 0, 9, 0],
        "layer2": [21, 6, 15, 4, 9, 18, 11, 26, 14, 1, 12, 0],
        "layer3": [9, 13, 9, 7, 13, 21, 17, 4, 5, 0, 7, 8],
        "position": 0
    },
    "disk4": {
        "layer1": [1, 0, 9, 0, 12, 0, 6, 0, 10, 0, 10, 0],
        "layer2": [3, 26, 6, 0, 2, 13, 9, 0, 17, 19, 3, 12],
        "layer3": [9, 20, 12, 3, 6, 0, 14, 12, 3, 8, 9, 0],
        "layer4": [7, 0, 9, 0, 7, 14, 11, 0, 8, 0, 16, 2],
        "position": 0
    },
    "disk5": {
        "layer1": [3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8, 8],
        "layer2": [4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9, 4],
        "layer3": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 4],
        "layer4": [11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14, 11],
        "position": -1
    }
}

def main():
    global puzzle
    while True:
        cycle = next_cycle(puzzle)
        if not cycle[1]:
            break
        puzzle = cycle[0]
        print(puzzle["disk1"]["layer1"])

def rotate_disc(disc):
    for key in disc:
        if key != "position":
            disc[key] = disc[key][1:] + disc[key][:1]       
    disc["position"] = (disc["position"] + 1) % 12
    return disc
    
def next_cycle(state):
    state["disk1"] = rotate_disc(state["disk1"])
    if state["disk1"]["position"] == 0:
        state["disk2"] = rotate_disc(state["disk2"])
        if state["disk2"]["position"] == 0:
            state["disk3"] = rotate_disc(state["disk3"])
            if state["disk3"]["position"] == 0:
                state["disk4"] = rotate_disc(state["disk4"])
                if state["disk4"]["position"] == 0:
                    return state, False
    return state, True

if __name__ == "__main__":
    main()