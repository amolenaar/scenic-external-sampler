from textwrap import dedent

from scenic import scenarioFromString


def test_default_values():
    scenario = scenarioFromString(
        dedent(
            """\
            from scenic_external_sampler.sampler import DoubleSampler, Values
            param externalSampler = DoubleSampler

            values = Values([1, 3, 8])
            ego = new Object with value values
            """
        )
    )
    scene_1, _ = scenario.generate()
    scene_2, _ = scenario.generate()
    scene_3, _ = scenario.generate()

    assert scene_1.egoObject.value == 2
    assert scene_2.egoObject.value == 6
    assert scene_3.egoObject.value == 16
