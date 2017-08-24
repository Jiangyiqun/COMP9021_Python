from transformation import transformation

# funtion: check_steps
# version: 2.0
# dependency: transformation()
# input: state_1, state_2, steps
# output: Boolean
# description: use whether use steps can transform state_1 to state_2
# 1  E   S   R
# 2  EE  ES  ER  SE  SS  SR  RE  RS  RR
# 3  EEE EES EER ESE ESS ESR SER ERS ERR SEE SES SER SSE SSS SSR SRE SRS SRR REE RES RER RSE RSS RSR RRE RRS RRR
#   example:
#   for RRE the 24 value
#   24 // (3 ** 2)  = 2, so type = 2
#   24 % (3 ** 2)   = 6 // (3 ** 1)= 2, so type = 2
#   6 % 3 = 0 // (3 ** 0) = 0, so type = 0  
def check_steps(state_1, state_2, steps):
    print(f'now we are calculating {steps} step')
    for sequency_of_methods in range(0, 3 ** steps): # sequency_of_methods start from 0
        # initialize variable which will be used in next loop
        state_1_copy = state_1[:]
        remainder = sequency_of_methods
        # calculate methods(sequency_of_methods)
        for i in range(1, steps + 1):           # i in the indicator of steps of one methods, start from 1
            type = remainder // (3 ** (steps - i))
            state_1_copy = transformation(state_1_copy, type)
            remainder = remainder % (3 ** (steps- i))
        if state_1_copy == state_2:
            return True        
    return False

# test code
if __name__ == "__main__":
    state_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    state_2 = [2, 6, 8, 4, 5, 7, 3, 1]
    steps = 7
    print(check_steps(state_1, state_2, steps))