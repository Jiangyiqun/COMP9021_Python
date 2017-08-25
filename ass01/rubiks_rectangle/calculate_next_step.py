from transformation import transformation

# funtion: calculate_next_step
# version: v01
# dependency: transformation()
# input: this_step[]
# output: next_step[]
# description: just add new elements to next_step[], I mean this_step is included into next_step
def calculate_next_step(this_step):
    this_step = list(this_step)
    next_step = set()
    for i in range(len(this_step)):         # find every elements this_step[i]
        for type in range(3):               # apply 3 transformations on each elements
            next_step.add(transformation(this_step[i], type))  
    return(next_step)

# test code
if __name__ == "__main__":
    this_step = set([(8, 7, 6, 5, 4, 3, 2, 1), (1, 7, 2, 4, 5, 3, 6, 8), (4, 1, 2, 3, 6, 7, 8, 5)])
    print(this_step)
    this_step = calculate_next_step(this_step)
    print(this_step)