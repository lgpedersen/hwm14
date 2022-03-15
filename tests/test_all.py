#!/usr/bin/env python
from pytest import approx
import pytest
from datetime import datetime
import hwm14


def test_hwm():
    t = datetime(2013, 3, 31, 12)
    glat = 65
    glon = -148
    altkm = 150
    f107a = 100
    f107 = 100
    ap = 4

    wind = hwm14.run(t, altkm, glat, glon, f107a, f107, ap)

    assert wind["meridional"] == approx(-20.73515701, rel=1e-4)
    assert wind["zonal"] == approx(35.82102585, rel=1e-4)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
