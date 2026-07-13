class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pas = 0
        res = []
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] +=1 
            return digits
        for i in range(len(digits)-1,-1,-1):
            # print(i, digits)
            if digits[i] == 9 and pas != -1:
                pas = 1
                digits[i] = 0
            elif digits[i] != 9 and pas == 1:
                
                digits[i] += 1
                pas = -1
        # print(digits)
        if pas == 1:
            digits = [1] + digits
        return digits