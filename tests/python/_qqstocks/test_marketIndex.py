import os,sys
from pprint import pprint

import config

import _qqstocks.marketIndex


def test():
  print(_qqstocks.marketIndex.getHSI())
  print(_qqstocks.marketIndex.getSZ399001())
  print(_qqstocks.marketIndex.getSH000001())



test()