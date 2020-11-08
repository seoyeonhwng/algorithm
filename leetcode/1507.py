class Solution:
    def reformatDate(self, date: str) -> str:
        month_info = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }
        d, m, y = date.split(' ')
        date = d[:-2] if len(d[:-2]) == 2 else '0'+d[:-2]
        
        reformated = y + '-' + month_info[m] + '-' + date
        return reformated
        