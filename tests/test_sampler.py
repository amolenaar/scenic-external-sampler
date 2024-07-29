from scenic_external_sampler.sampler import DoubleSampler, Values


def test_sample_a_value():
    values = Values([1, 3, 8])
    sampler = DoubleSampler([values], globalParams={})

    sampler.sample("")
    assert values.sample() == 2
    sampler.sample("")
    assert values.sample() == 6
    sampler.sample("")
    assert values.sample() == 16


def test_sampler_terminates():
    values = Values([1, 3])
    sampler = DoubleSampler([values], globalParams={})

    sampler.sample("")
    sampler.sample("")
    sampler.sample("")
