import unittest
import ezgal
import numpy as np

class Test(unittest.TestCase):

    model = ezgal.model('bc03_ssp_z_0.02_chab.model')

    def test_loadmodel(self):
        # assertTrue should fail if ezgal.model returns None
        self.assertTrue(self.model)

        # Trying to load a non-existent model should fail
        with self.assertRaises(Exception):
            ezgal.model('Non_Existent.model')


    ### Testing Basic ezgal.model functionality
    def test_getage(self):
        self.assertTrue(self.model.get_age(3.0, 3.0) == 0)

    def test_addfilter(self):
        f = 'sloan_i'
        self.model.add_filter(f)
        self.assertTrue(self.model.filters[f])

    def test_getzs(self):
        self.assertIsInstance(self.model.get_zs(1.0), np.ndarray)
    

    ### Templates for future tests
    # def test_getzs(self):
    #     pass

    # def test_getzs(self):
    #     pass



if __name__ == "__main__":
    unittest.main()
