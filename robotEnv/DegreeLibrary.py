from Degree import Degree, DegreeChangeError

class DegreeLibrary(object):

    def __init__(self):
        self._deg = Degree()
        self._result = 0

    def degree_change_C(self, degree):
        self._result = self._deg._change_C(degree)

    def degree_change_F(self, degree):
        self._result = self._deg._change_F(degree)

    def result_should_BE(self, expected):
        if self._result != float(expected):
            raise AssertionError('%s != %s' % (self._result, expected))
