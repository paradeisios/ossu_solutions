# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence
    else:
        result = []
        for c in sequence:
            for permutation in get_permutations(sequence.replace(c,"",1)):
                result.append(c+permutation)

    return list(set(result))
if __name__ == '__main__':
#    
#   #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    test_one = "ab"
    print(f"Input: {test_one}")
    print("Expected output: ['ab','ba']")
    print('Actual Output:', get_permutations(test_one))

    if sorted(['ab','ba']) == sorted(get_permutations(test_one)):
        print("Passed test 1")
    else:
        print("Failed test 1")

    test_two = "abc"
    print(f"Input: {test_two}")
    print("Expected output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']")
    print('Actual Output:', get_permutations(test_two))

    if sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == sorted(get_permutations(test_two)):
        print("Passed test 2")
    else:
        print("Failed test 2")

    test_three = "xxy"
    print(f"Input: {test_three}")
    print("Expected output: ['xxy', 'xyx', 'yxx']")
    print('Actual Output:', get_permutations(test_three))

    if sorted(['xxy', 'xyx', 'yxx']) == sorted(get_permutations(test_three)):
        print("Passed test 2")
    else:
        print("Failed test 2")

