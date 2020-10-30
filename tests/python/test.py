import os,sys
from pprint import pprint


PYTHON_TEST_HOME=os.path.abspath(os.path.dirname(__file__))
TEST_HOME=os.path.abspath(PYTHON_TEST_HOME+'/..')
PROJ_HOME=os.path.abspath(TEST_HOME+'/..')
PYTHON_SRC_HOME=os.path.abspath(PROJ_HOME+'/python')

sys.path.append(PYTHON_SRC_HOME)


import config

import _aastocks.test_get_ticket

# import _qqstocks.test_get_ticket
import _qqstocks.test_marketIndex