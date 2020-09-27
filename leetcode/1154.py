class Solution:
    def get_february(self, year):
        if year % 4 == 0:
            if year % 100 != 0:
                return 29
            else:
                if year % 400 == 0:
                    return 29
        return 28
    
    def dayOfYear(self, date: str) -> int:
        days = {
            1: 31,
            2: -1, # 28 or 29
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        
        year, month, day = date.split('-')
        days[2] = self.get_february(int(year))
        
        count = 0
        for i in range(1, int(month)):
            count += days[i]
        
        return count + int(day)