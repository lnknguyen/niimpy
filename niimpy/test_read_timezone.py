import dateutil
from dateutil.tz import gettz
import pandas as pd

import niimpy
from  niimpy import sampledata

def test_read_timezone_default():
    """Default timezone is Europe/Helsinki"""
    data = niimpy.read_csv(sampledata.TEST_TIMEZONE)
    assert isinstance(data.index, pd.DatetimeIndex)
    assert data.index[0].hour == 0

    assert data.index.tzinfo == gettz('Europe/Helsinki')

def test_read_timezone():
    """Test specifying different timezones"""
    data = niimpy.read_csv(sampledata.TEST_TIMEZONE, tzinfo='UTC')
    assert data.index[0].hour == 22

    data = niimpy.read_csv(sampledata.TEST_TIMEZONE, tzinfo=gettz('Europe/Paris'))
    assert data.index[0].hour == 23

    assert data.index.tzinfo == dateutil.tz.gettz('Europe/Paris')
