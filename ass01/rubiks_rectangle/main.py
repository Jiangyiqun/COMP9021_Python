from interface_input import interface_input
from interface_output import interface_output
from count_steps import count_steps

# initialization
current_state = [1, 2, 3, 4, 5, 6, 7, 8]
final_configuration = interface_input() # final_configuration
steps = count_steps(current_state, final_configuration)
interface_output(steps)