# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by Jack Jiang and Eric Martin for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message


class Permutation:
    def __init__(self, *args, length=None):
        ''' initialazation
        check validity of input, generate L_input and length in case length is not specified.
        '''
        # print(*args)
        # print(args)
        error_msg = 'Cannot generate permutation from these arguments'
        if args and length:
            if type(args[0]) != int or type(length) != int:
                raise PermutationError(error_msg)
            if length < 0:
                raise PermutationError(error_msg)
            if set(args) != set(length - i for i in range(length)):
                raise PermutationError(error_msg)
            self.L_input= args
        if args and not length:
            if type(args[0]) != int:
                raise PermutationError(error_msg)
            if set(args) != set(len(args) - i for i in range(len(args))):
                raise PermutationError(error_msg)
            self.L_input = args
        if not args and length:
            if type(length) != int:
                raise PermutationError(error_msg)
            if length < 0:
                raise PermutationError(error_msg)
            self.L_input = tuple(i+1 for i in range(length))
        if not args and not length:
            self.L_input = args    
        # generate attributes: L_sorted and nb_of_cycles, length
        self.length = len(self.L_input)
        L_generated = self._generate()
        self.L_sorted = self._sort(L_generated)
        self.nb_of_cycles = len(L_generated)
        # print(L_generated)
        # print(L_sorted)


    def __len__(self):
        return self.length


    def __repr__(self):
        return f'Permutation{self.L_input}'


    def __str__(self):
        if self.L_sorted:
            print_str = ''
            for sub_list in self.L_sorted:
                print_str += '(' + ' '.join(map(str, sub_list)) + ')'
        else:
            print_str = '()'
        return print_str


    def __mul__(self, permutation):
        '''
        indicator   = (1, 2, 3, 4, 5)
        self        = (5, 4, 3, 2, 1)
        permutation = (4, 2, 5, 1, 3)
        '''
        if self.length == permutation.length:
            mul_list = []
            for i in self.L_input:
                mul_list.append(permutation.L_input[i - 1])
            return Permutation(*mul_list)
        else:
            raise PermutationError('Cannot compose permutations of different lengths')


    def __imul__(self, permutation):
        return self.__mul__(permutation)


    def inverse(self):
        '''
        indicator = (1, 2, 3, 4, 5)
        origin    = (2, 5, 4, 3, 1)
        inversed  = (5, 1, 4, 3, 2)
        descrition:
        first, find 1 in origin list, use its indicator+1 as new number to form a inversed list
        loop until reached length+1
        '''
        L_output = []
        for i in range(1, self.length+1):
            L_output.append(self.L_input.index(i) + 1)
        return Permutation(*L_output)
    

    def _generate(self):
        '''
        read a number, check whether the number is already in the sub_list
        if yes, append L_sub_list to L_generated and continue loop
        if not, put the number in L_sub_list and change the indicator i
        put the number in a sub_list
        '''
        L_generated = []
        L_not_used = [True for _ in range(self.length)]
        L_sub_list = []
        i = 0
        for i in range(self.length):
            if L_not_used[i]:
                L_sub_list = []
                j = i
                while True:
                    j = self.L_input[j] - 1
                    if self.L_input[j] in L_sub_list:
                        L_generated.append(L_sub_list)
                        break
                    else:
                        L_sub_list.append(self.L_input[j])
                        L_not_used[j] = False
        return L_generated


    def _sort(self, unsorted_list):
        '''
        about how to sort sub_list:
        input sublist:  (3, 4, 5, 1, 2)
        output sublist: (5, 1, 2, 3, 4)
        description:
            locate the max number, assume its indicator is i
            pop the left most number and append it to the list
            loop i times
        '''
        sorted_list = unsorted_list[:]
        for sub_list in sorted_list:
            i = sub_list.index(max(sub_list))
            for _ in range(i):
                sub_list.append(sub_list.pop(0))
        sorted_list.sort()
        return sorted_list     


if __name__ == '__main__':
    p1 = Permutation(5, 4, 3, 2, 1)
    p2 = Permutation(2, 4, 1, 5, 3)
    q = p1 * p2
    print(q)
    p2 *= p1
    print(p2)
    