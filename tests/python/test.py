import os,sys
from pprint import pprint

PYTHON_TEST_HOME=os.path.abspath(os.path.dirname(__file__))
TEST_HOME=os.path.abspath(PYTHON_TEST_HOME+'/..')
PROJ_HOME=os.path.abspath(TEST_HOME+'/..')
PYTHON_SRC_HOME=os.path.abspath(PROJ_HOME+'/python')

sys.path.append(PYTHON_SRC_HOME)

import config

print(config.HELLOWORLD)