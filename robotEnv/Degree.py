class Degree(object):

    def __init__(self):
        self.change_degree = 0

    def _check(self, degree):
        try:
            float(degree)
            return True
        except ValueError:
            return False

    def _change_C(self, degree):
        if self._check(degree) == False:
            raise DegreeChangeError("Invalid degree '%s'."% degree)

        else:
            try:
                change_degree = round((float(degree)-32)/1.8, 2)
                return change_degree
            except SyntaxError:
                raise CalculationError('Invalid expression.')
            except ZeroDivisionError:
                raise CalculationError('Division by zero.')

    def _change_F(self, degree):
        if self._check(degree) == False:
            raise DegreeChangeError("Invalid degree '%s'."% degree)
        else:
            try:
                change_degree = round((float(degree)*1.8)+32, 2)
                return change_degree
            except SyntaxError:
                raise CalculationError('Invalid expression.')

class DegreeChangeError(Exception):
    pass
                
