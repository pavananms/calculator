class Calculator:
    delim = ','
    @staticmethod
    def add(sum_string):
        delim = Calculator.delim
        if not sum_string:
            return 0    
        if ',' not in sum_string and '\n' not in sum_string:
            return int(sum_string)
        elif sum_string[0:2] == '//':
            delim = sum_string[2:3]
            sum_string = sum_string[4:]
        else:
            sum_string = sum_string.replace('\n', delim)

        return sum([int(i) for i in sum_string.split(delim)])
        

