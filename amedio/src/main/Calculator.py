from src.main.constants import _constants

class Calculator(object):
    
    def __init__(self):
        pass
    
    def add(self, addParams):
        
        result = 0
        
        if addParams != "":
            const = _constants()
            for calcParam in addParams.replace(const.COMMA_SEP(), const.NEW_LINE_SEP()).split(const.NEW_LINE_SEP()):
                result += int(calcParam)
        
        return result