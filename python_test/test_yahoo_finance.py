import yfinance as yf
import json
import os,sys
from pprint import pprint

TEST_HOME=os.path.dirname(os.path.abspath(__file__))
SCRIPT_HOME=os.path.abspath(TEST_HOME+'/../python')
LIB_HOME=os.path.abspath(SCRIPT_HOME+'/lib')

sys.path.append(LIB_HOME)
sys.path.append(SCRIPT_HOME)

from yfinance_helloworld import fetch_yfinance

info_json = fetch_yfinance('MSFT')
pprint(info_json['open'])
