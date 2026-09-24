class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num_string = ""
        for i in digits:
            num_string += str(i)

        num = int(num_string) + 1
        digits_2 = list(map(int , str(num)))
        
        return (digits_2)