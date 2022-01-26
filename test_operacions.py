#!/usr/bin/env python3

import pytest
import operacions

def test_suma():
     assert operacions.suma(3,3) == 6
     assert operacions.suma(-3,3) == 0
     assert operacions.suma(-3,-3) == -6
     
      
def test_resta():
     assert operacions.resta(3,3) == 0
     assert operacions.resta(-3,3) == -6
  