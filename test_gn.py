from ast import Num
import unittest
from guess_number import GuessNumberComputer

# TODO 
class GuessNumCompTestCase(unittest.TestCase):
    ''' tests computer guessing number '''

    def test_gnc(self):
        ''' Test whether comparisons are true or false '''

        gnc = GuessNumberComputer()
        max_input = gnc.settings.max
        
        
        
    #    # if result is 0, return error/failure
    #     nums = list(range(1,max_input + 1))
    #     for i in nums:
    #         result = gnc._binary_search_guess(i)
    #         print(i)
    #         count = 1
    #         while count <= len(nums):
    #             if result in nums:
    #                 self.assertIn(result, nums)
    #             count += 1        
        

if __name__ == '__main__':
    unittest.main()