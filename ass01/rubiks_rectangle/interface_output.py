# function: interface_output
# input: steps
# output: print
def interface_output(steps):
    if steps == 0 or steps == 1:
        unit = 'step'
    else:
        unit = 'steps'
    print(f'{steps} {unit} is needed to reach the final configuration.')
    return


# test code
if __name__ == "__main__":
    interface_output(16)