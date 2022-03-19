class Calculator:
    @staticmethod
    def add(sum_string):
        if not sum_string:
             return 0    
        if ',' not in sum_string:
             return int(sum_string)


