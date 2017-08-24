from check_steps import check_steps

# funtion: count_steps
# dependency: check_steps()
# input: state_1, state_2
# output: steps
# description: use check_steps() to calculate steps from state_1 to state_2
def count_steps(state_1, state_2):
    steps = int(0)
    if state_1 == state_2:
        return(steps)
    while True:
        steps += 1
        if check_steps(state_1, state_2, steps):
            return(steps)


# test code
if __name__ == "__main__":
    def check_steps(state_1, state_2, steps):
        return True
    current_state = [1, 2, 3, 4, 5, 6, 7, 8]
    final_configuration = [1, 2, 3, 4, 5, 6, 7, 8]
    steps = count_steps(current_state, final_configuration)
    print('steps =', steps)