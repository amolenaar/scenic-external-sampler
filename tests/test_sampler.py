import pytest

from scenic_external_sampler.sampler import SimpleSampler, Values


def test_sample_a_value():
    values = Values([1, 3, 8])
    sampler = SimpleSampler([values], globalParams={})

    sampler.sample("")
    assert values.sample() == 1
    sampler.sample("")
    assert values.sample() == 3
    sampler.sample("")
    assert values.sample() == 8


def test_sampler_terminates():
    values = Values([1, 3])
    sampler = SimpleSampler([values], globalParams={})

    sampler.sample("")
    sampler.sample("")

    with pytest.raises(IndexError):
        sampler.sample("")
