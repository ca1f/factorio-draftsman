# test_mining_drill.py

from draftsman.constants import MiningDrillReadMode
from draftsman.entity import MiningDrill, mining_drills
from draftsman.error import (
    InvalidEntityError, InvalidSignalError, InvalidModuleError
)
from draftsman.warning import (
    DraftsmanWarning, ModuleCapacityWarning, ModuleLimitationWarning
)

from schema import SchemaError

from unittest import TestCase

class MiningDrillTesting(TestCase):
    def test_constructor_init(self):
        reactor = MiningDrill(
            "electric-mining-drill",
            items = {
                "productivity-module": 1,
                "productivity-module-2": 1
            }
        )

        # Warnings
        with self.assertWarns(DraftsmanWarning):
            MiningDrill(unused_keyword = "whatever")
        with self.assertWarns(ModuleCapacityWarning):
            MiningDrill(
                "electric-mining-drill",
                items = {
                    "productivity-module": 5
                }
            )

        # Errors
        with self.assertRaises(InvalidEntityError):
            MiningDrill("not a mining drill")

    def test_set_item_request(self):
        mining_drill = MiningDrill("electric-mining-drill")
        mining_drill.set_item_request("speed-module-3", 3)
        self.assertEqual(
            mining_drill.to_dict(),
            {
                "name": "electric-mining-drill",
                "position": {"x": 1.5, "y": 1.5},
                "items": {
                    "speed-module-3": 3
                }
            }
        )
        with self.assertWarns(ModuleCapacityWarning):
            mining_drill.set_item_request("productivity-module-3", 3)
        self.assertEqual(
            mining_drill.to_dict(),
            {
                "name": "electric-mining-drill",
                "position": {"x": 1.5, "y": 1.5},
                "items": {
                    "speed-module-3": 3,
                    "productivity-module-3": 3
                }
            }
        )
        mining_drill.set_item_request("speed-module-3", None)
        self.assertEqual(
            mining_drill.items,
            {
                "productivity-module-3": 3
            }
        )
        mining_drill.set_item_requests(None)
        self.assertEqual(mining_drill.items, {})
        with self.assertWarns(ModuleLimitationWarning):
            mining_drill.set_item_request("iron-ore", 2)

        # Errors
        with self.assertRaises(InvalidSignalError):
            mining_drill.set_item_request("incorrect", 2)

    def test_set_read_resources(self):
        mining_drill = MiningDrill()
        mining_drill.set_read_resources(True)
        self.assertEqual(
            mining_drill.control_behavior,
            {
                "circuit_read_resources": True
            }
        )
        mining_drill.set_read_resources(None)
        self.assertEqual(mining_drill.control_behavior, {})
        with self.assertRaises(SchemaError):
            mining_drill.set_read_resources("incorrect")

    def test_set_read_mode(self):
        mining_drill = MiningDrill()
        mining_drill.set_read_mode(MiningDrillReadMode.UNDER_DRILL)
        self.assertEqual(
            mining_drill.control_behavior,
            {
                "circuit_resource_read_mode": MiningDrillReadMode.UNDER_DRILL
            }
        )
        mining_drill.set_read_mode(None)
        self.assertEqual(mining_drill.control_behavior, {})
        # with self.assertRaises(SchemaError):
        #     mining_drill.set_read_mode("incorrect")