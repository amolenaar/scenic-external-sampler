"""
The basic idea is that :obj:`Values` takes values from
the sampler and returns those.
"""

from collections.abc import Collection
from typing import Any

from scenic.core.external_params import ExternalParameter, ExternalSampler


class DoubleSampler(ExternalSampler):
    """A simple example sampler.
    
    Multiply the values given.
    """

    def __init__(self, params, globalParams: dict):
        super().__init__(params, globalParams)
        for p in params:
            p.sampler = self
        self.all_values = {p.name: p.values for p in params}
        self.current_index = -1
        self.factor = 2
        self.cachedSample = None  # see superclass code
        self.rejectionFeedback = "rejected"

    def nextSample(self, feedback):
        self.current_index += 1
        return {name: (values[self.current_index] * self.factor) for name, values in self.all_values.items()}

    def valueFor(self, param):
        """Return the value for a specific parameter."""
        return self.cachedSample[param.name]


class Values(ExternalParameter):

    def __init__(self, values: Collection[Any], name: str | None = None):
        self._name = name if name else f"param_{id(self)}"
        self._values = values
        super().__init__()

    @property
    def name(self) -> str:
        return self._name

    @property
    def values(self) -> Collection[Any]:
        return self._values

