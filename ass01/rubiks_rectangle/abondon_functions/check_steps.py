from transformation import transformation
import time

# funtion: check_steps
# version: 2.0
# dependency: transformation()
# input: last_transformation{}, final_state, steps
# output: return False or new_transformation{}
# description: use whether use steps can transform state_1 to state_2
# 1  E   S   R
# 2  EE  ES  ER  SE  SS  SR  RE  RS  RR
# 3  EEE EES EER ESE ESS ESR SER ERS ERR SEE SES SER SSE SSS SSR SRE SRS SRR REE RES RER RSE RSS RSR RRE RRS RRR
#   example:
#   for RRE the 24 value
#   24 // 3  = 8, so the former transformation is from last_transformation[8]
#   24 %  3  = 0, so the last transformation is 0

def check_steps(last_transformation, final_state, steps):
    new_transformation = {}             # initialize new transformation
    for sequency_of_methods in range(0, 3 ** steps): # sequency_of_methods start from 0
        current_state = transformation(last_transformation[sequency_of_methods // 3], sequency_of_methods % 3)
        if current_state == final_state:
            return False        
        else:
            new_transformation[sequency_of_methods] = current_state
    return(new_transformation)

# test code
if __name__ == "__main__":
    final_state = [2, 6, 8, 4, 5, 7, 3, 1]

    before = time.time()
    print(check_steps(last_transformation, final_state, steps))
    after = time.time()
    print(f'it took {after - before} seconds to excute the function')