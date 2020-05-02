import otk.geo3
import numpy as np
from otk.rt1 import interfaces
from otk import v4hb, v4h


def test_make_perpendicular():
    assert np.array_equal(otk.geo3.make_perpendicular(v4h.xhat, v4h.yhat), v4h.zhat)

    # Single degenerate vector.
    v = otk.geo3.make_perpendicular(v4h.xhat, v4h.xhat)
    assert np.isclose(v4hb.dot(v4h.xhat, v), 0)
    assert np.isclose(v4hb.dot(v), 1)

    # Single degenerate vector.
    m = np.c_[v4h.xhat, v4h.yhat].T
    v = otk.geo3.make_perpendicular(m, m)
    assert np.allclose(v4hb.dot(m, v), 0)
    assert np.allclose(v4hb.dot(v), 1)