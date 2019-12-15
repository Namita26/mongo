import os
import sys

parent_dir = os.path.dirname(os.getcwd())
if parent_dir not in sys.path:
    sys.path.insert(0, os.path.dirname(os.getcwd()))
