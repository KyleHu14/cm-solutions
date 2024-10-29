class Solution:
    def romanToInt(self, s: str) -> int:
        # For ease of access of roman numeral and their value
        romanNum = {
            'I' : 1, 
            'V' : 5, 
            'X' : 10, 
            'L' : 50, 
            'C' : 100, 
            'D' : 500, 
            'M' : 1000
        }

        # Final total
        finalTotal = 0

        # For loop
        for index, numeral in enumerate(s):
            # Convert numeral to number
            curInt = romanNum[numeral]

            # Check if we are on the last index
            if index == len(s)-1:
                return finalTotal+curInt

            nextInt = romanNum[s[index+1]]
            # Next check if curInt is larger / equal to nextInt
            # If this is the case, we can normally add the numeral
            if curInt >= nextInt:
                finalTotal+=curInt
            # If this is not the case, we are dealing with a special case
            # Like IV, XC, CM
            # We can subtract the first numeral from the total instead
            else: 
                finalTotal-=curInt
