from typing import Sized
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.population import Population
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import numpy as np
from problem import ImageToAscii
import matplotlib.pyplot as plt

# Pseudo-Code 8x16 px
# - Load table of Ascii from /ascii
# - Open Image
# - Image to gray scale
# - Trunc to multiple of char size
# - 


