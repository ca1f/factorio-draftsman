# container.py

from draftsman.prototypes.mixins import (
    CircuitConnectableMixin, InventoryMixin, Entity
)
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import containers

import warnings

class Container(CircuitConnectableMixin, InventoryMixin, Entity):
    """
    * `wooden-chest`
    * `iron-chest`
    * `steel-chest`
    * `logistic-chest-active-provider`
    * `logistic-chest-passive-provider`
    """
    def __init__(self, name = containers[0], **kwargs):
        # type: (str, **dict) -> None
        super(Container, self).__init__(name, containers, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )