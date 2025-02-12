import pandas as pd
import numpy as np

import niimpy
from niimpy.reading import read
from niimpy.preprocessing import sampledata
from niimpy.config import config

TZ = 'Europe/Helsinki'

def test_read_csv():
    data = niimpy.read_csv(config.MULTIUSER_AWARE_BATTERY_PATH, tz=TZ)
    # The index should be set to the times
    assert isinstance(data.index, pd.DatetimeIndex)
    # There should be a column 'datetime' added in the setup.
    assert 'datetime' in data
