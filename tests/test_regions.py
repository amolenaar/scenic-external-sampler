from scenic_external_sampler.regions import NorthEast, NorthWest, SouthEast, SouthWest


def test_region_dimensions():
    assert NorthEast.AABB == ((0.0, 0.0), (100.0, 100.0), (0, 0))
    assert NorthWest.AABB == ((-100.0, 0.0), (0.0, 100.0), (0, 0))
    assert SouthEast.AABB == ((0.0, -100.0), (100.0, 0.0), (0, 0))
    assert SouthWest.AABB == ((-100.0, -100.0), (0.0, 0.0), (0, 0))
