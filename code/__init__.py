import os
import re

import numpy as np
import pandas as pd

import kraft
from read_ws_hs import read_ws_hs

SETTING = kraft.json.read("setting.json")
