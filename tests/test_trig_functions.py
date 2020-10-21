import numpy as np

from trig_functions import sin

class TestSin(object):

    def test_sin(self):

        my_sin = sin(6, 10000)

        assert np.isclose(my_sin, np.sin(6), atol=1e-12)

