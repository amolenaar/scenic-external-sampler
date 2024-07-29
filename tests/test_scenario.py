from textwrap import dedent

import pytest
from scenic import scenarioFromString

from scenic_external_sampler.regions import NorthEast, SouthWest


def test_simple_sampler_with_values():
    scenario = scenarioFromString(
        dedent(
            """\
            from scenic_external_sampler.sampler import SimpleSampler, Values
            param externalSampler = SimpleSampler

            values = Values([1, 3, 8])
            ego = new Object with value values
            """
        )
    )

    scene_1, _ = scenario.generate()
    scene_2, _ = scenario.generate()
    scene_3, _ = scenario.generate()

    assert scene_1.egoObject.value == 1
    assert scene_2.egoObject.value == 3
    assert scene_3.egoObject.value == 8


def test_regions():
    scenario = scenarioFromString(
        dedent(
            """\
            from scenic_external_sampler.regions import NorthEast

            ego = new Object in NorthEast
            """
        )
    )

    scene, _ = scenario.generate()

    assert NorthEast.containsPoint(scene.egoObject.position)


def test_regions_in_uniform_distribution():
    scenario = scenarioFromString(
        dedent(
            """\
            from scenic_external_sampler.regions import NorthEast, SouthWest

            ego = new Object in Uniform(NorthEast, SouthWest)
            """
        )
    )

    scene, _ = scenario.generate()

    assert NorthEast.containsPoint(scene.egoObject.position) or SouthWest.containsPoint(scene.egoObject.position)


# @pytest.mark.xfail(
#     reason="This scenario works with internal distributions, but fails as soon as we depend on an external sampler"
# )
def test_regions_with_externally_sampled_distribution():
    scenario = scenarioFromString(
        dedent(
            """\
            from scenic_external_sampler.regions import NorthEast, SouthWest
            from scenic_external_sampler.sampler import SimpleSampler, Values
            param externalSampler = SimpleSampler

            ego = new Object in Values(NorthEast, SouthWest)
            """
        )
    )

    scene, _ = scenario.generate()

    assert NorthEast.containsPoint(scene.egoObject.position) or SouthWest.containsPoint(scene.egoObject.position)
