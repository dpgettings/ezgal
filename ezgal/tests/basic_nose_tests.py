from __future__ import absolute_import
from nose import with_setup
import numpy as np
import ezgal

# class BasicTest(object):

#     ## These are run ONCE for each class before any tests are run
#     @classmethod
#     def setup_class(klass):
#         pass
#     @classmethod
#     def teardown_class(klass):
#         pass


    

def setup_func():
    model = ezgal.model('bc03_ssp_z_0.02_chab.model')
    print "*************Setting Up Here"
# def teardown_func():
#     model = 0
    
# Test loading a model file
def test_load_model():
    print "*************Testing Load Module"
    assert ezgal.model('bc03_ssp_z_0.02_chab.model')


#model = ezgal.model('bc03_ssp_z_0.02_chab.model')
filters = ['sloan_r', 'ch1', 'wise_ch1', 'j']

@with_setup(setup=setup_func, teardown=None)
def test_add_filters():
    print "*************Test adding filters"
    for f in filters:
        yield check_add_filters, model, f

def check_add_filters(model_obj, filter_name):
    print "*************Actually checking filters"
    model_obj.add_filter(filter_name)
    assert filter_name in model_obj.filters
