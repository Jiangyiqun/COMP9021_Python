# function: interface_output
# input: steps
# output: print
def interface_output(steps):
    if steps == 0 or steps == 1:
        unit = 'step is'
    else:
        unit = 'steps are'
    print(f'{steps} {unit} needed to reach the final configuration.')
    return


# test code
if __name__ == "__main__":
    interface_output(16)