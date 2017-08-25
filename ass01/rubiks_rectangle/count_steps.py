from calculate_next_step import calculate_next_step
import time

# funtion: count_steps
# dependency: check_steps()
# input: state_1, state_2
# output: steps
# description: use check_steps() to calculate steps from state_1 to state_2
def count_steps(state_1, state_2):
    steps = int(0)
    if state_1 == state_2:
        return(steps)

    this_step = [state_1]
    while True:
        steps += 1
        this_step = calculate_next_step(this_step)
        for e in this_step:
            if state_2 == e:
                return(steps)


# test code
if __name__ == "__main__":
    state_1 = (1, 2, 3, 4, 5, 6, 7, 8)
    # state_2 = (1, 2, 3, 4, 5, 6, 7, 8)
    # state_2 = (2, 6, 8, 4, 5, 7, 3, 1)
    # state_2 = (1, 5, 3, 2, 4, 6, 7, 8)
    state_2 = (7, 2, 1, 5, 4, 3, 6, 8)
    steps = count_steps(state_1, state_2)
    print('steps =', steps)