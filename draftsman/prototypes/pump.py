# pump.py

from draftsman.prototypes.mixins import (
    CircuitConditionMixin, ControlBehaviorMixin, CircuitConnectableMixin, 
    DirectionalMixin, Entity
)
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import pumps

import warnings


class Pump(CircuitConditionMixin, ControlBehaviorMixin, CircuitConnectableMixin, 
           DirectionalMixin, Entity):
    """
    """
    def __init__(self, name = pumps[0], **kwargs):
        # type: (str, **dict) -> None
        super(Pump, self).__init__(name, pumps, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )