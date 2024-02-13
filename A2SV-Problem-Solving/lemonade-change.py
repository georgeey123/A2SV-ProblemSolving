class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill, ten_bill = 0, 0

        for bill in bills:
            if bill == 5:
                five_bill += 1
            if bill == 10:
                ten_bill += 1
                if five_bill < 1:
                    return False
                five_bill -= 1
            if bill == 20:
                if ten_bill < 1:
                    if 5 * five_bill >= 15:
                        five_bill -= 3
                        continue
                if five_bill < 1 or ten_bill < 1:
                    return False
                five_bill -= 1
                ten_bill -= 1
                
        return True