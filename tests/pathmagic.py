"""Path hack to make tests work."""

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/../database/')
