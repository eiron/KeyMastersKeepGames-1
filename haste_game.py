from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet, Choice

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class HasteArchipelagoOptions:
    haste_trial_modes: HasteTrialModes
    haste_ability_options: HasteAbilityOptions
    haste_maximum_difficulty_endless: HasteMaximumDifficultyEndless

class HasteGame(Game):
    name = "Haste: Broken Worlds"
    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False
    options_cls = HasteArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.include_shard_completions:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Beat Shard SHARD",
                    data = {
                        "SHARD": (self.shards, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Beat Shard SHARD_HARD",
                    data = {
                        "SHARD_HARD": (self.shards_hard, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = True,
                    weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat Shard SHARD using ABILITY",
                    data = {
                        "SHARD": (self.shards, 1),
                        "ABILITY": (self.abilities, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Beat Shard SHARD_HARD using ABILITY",
                    data = {
                        "ABILITY": (self.abilities, 1),
                        "SHARD_HARD": (self.shards_hard, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = True,
                    weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following Shards: SHARD",
                    data = {
                        "SHARD": (self.shards, 2)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following Shards: SHARD",
                    data = {
                        "SHARD": (self.shards, 3)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following Shards using ABILITY: SHARD",
                    data = {
                        "SHARD": (self.shards, 2),
                        "ABILITY": (self.abilities, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Beat the following Shards using ABILITY: SHARD",
                    data = {
                        "SHARD": (self.shards, 3),
                        "ABILITY": (self.abilities, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 1,
                ),
            ])

        if self.include_endless_statistics:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "In DIFFICULTY Endless Mode, complete FRAGMENTHIGH Fragments",
                    data = {
                        "DIFFICULTY": (self.difficulty, 1),
                        "FRAGMENTHIGH": (self.fragments_high, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 6,
                ),
                GameObjectiveTemplate(
                    label = "In DIFFICULTY Endless Mode, reach a top speed of at least SPEED m/s",
                    data = {
                        "DIFFICULTY": (self.difficulty, 1),
                        "SPEED": (self.speeds, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 6,
                ),
                GameObjectiveTemplate(
                    label = "In DIFFICULTY Endless Mode, get at least LANDINGS Perfect Landings",
                    data = {
                        "DIFFICULTY": (self.difficulty, 1),
                        "LANDINGS": (self.landings, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 6,
                ),
                GameObjectiveTemplate(
                    label = "In DIFFICULTY Endless Mode, Complete FRAGMENTLOW Fragments with a(n) RANK Rank or Higher",
                    data = {
                        "DIFFICULTY": (self.difficulty, 1),
                        "FRAGMENTLOW": (self.fragments_low, 1),
                        "RANK": (self.ranks, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 6,
                ),
            ])

        if self.include_challenge_completions:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Complete CHALLENGES Challenges",
                    data = {
                        "CHALLENGES": (self.challenge_count, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 6,
                ),
                GameObjectiveTemplate(
                    label = "Complete CHALLENGES_HARD Challenge(s)",
                    data = {
                        "CHALLENGES_HARD": (self.challenge_count_hard, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Fail CHALLENGE_COUNT Challenge(s)",
                    data = {
                        "CHALLENGE_COUNT": (self.challenge_count_fail_single, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 1,
                ),
                GameObjectiveTemplate(
                    label = "Complete CHALLENGE_COUNT Challenge(s) in one Shard",
                    data = {
                        "CHALLENGE_COUNT": (self.challenge_count_fail_single, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Complete a 'CHALLENGE' Challenge",
                    data = {
                        "CHALLENGE": (self.challenges, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 4,
                ),
                GameObjectiveTemplate(
                    label = "Complete one of the following Challenges: CHALLENGE",
                    data = {
                        "CHALLENGE": (self.challenges, 3)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 8,
                ),
            ])

        if self.include_scavenger_hunt:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Collect ITEM_COUNT items of RARITY rarity",
                    data = {
                        "ITEM_COUNT": (self.item_count, 1),
                        "RARITY": (self.rarities, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 7,
                ),
                GameObjectiveTemplate(
                    label = "Collect ITEM_COUNT_LEGENDARY item(s) of Legendary rarity",
                    data = {
                        "ITEM_COUNT_LEGENDARY": (self.item_count_legendary, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Collect three of the following Common (Green) Items: COMMON_ITEM",
                    data = {
                        "COMMON_ITEM": (self.common_items, 5)
                    },
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Collect two of the following Rare (Blue) Items: RARE_ITEM",
                    data = {
                        "RARE_ITEM": (self.rare_items, 4)
                    },
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Collect two of the following Epic (Purple) Items: EPIC_ITEM",
                    data = {
                        "EPIC_ITEM": (self.epic_items, 3)
                    },
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Collect one of the following Legendary (White/Rainbow) Item: LEGENDARY_ITEM",
                    data = {
                        "LEGENDARY_ITEM": (self.legendary_items, 2)
                    },
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 5,
                ),
            ])
            
        if self.include_disaster_mode:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete the Final Shard on Disaster Level DISASTER",
                    data = {
                        "DISASTER": (self.disaster, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = True,
                    weight = 5,
                )
            )
        
        return game_objective_templates

    @property
    def modes(self) -> List[str]:
        return sorted(self.archipelago_options.haste_trial_modes.value)
    
    @property
    def include_shard_completions(self) -> bool:
        return "Shard Completion" in self.modes
    
    @property
    def include_endless_statistics(self) -> bool:
        return "Endless Statistics" in self.modes
    
    @property
    def include_challenge_completions(self) -> bool:
        return "Challenge Completion" in self.modes
    
    @property
    def include_scavenger_hunt(self) -> bool:
        return "Scavenger Hunt" in self.modes

    @property
    def include_disaster_mode(self) -> bool:
        return "Disaster Mode" in self.modes

    def abilities(self) -> List[str]:
        abilities: List[str] = list(self.archipelago_options.haste_ability_options.value)
        return sorted(abilities)
    
    def difficulty(self) -> List[str]:
        difficulties: List[str] = ["Peaceful","Easy","Medium","Hard","Very Hard"]
        difficulties = difficulties[:(self.archipelago_options.haste_maximum_difficulty_endless.value + 1)]
        return difficulties
    
    @staticmethod
    def shards() -> List[int]:
        return list(range(1,9))
    
    @staticmethod
    def shards_hard() -> List[int]:
        return list(range(1,11))
    
    @staticmethod
    def fragments_high() -> List[int]:
        return list(range(15, 31, 5))
    
    @staticmethod
    def fragments_low() -> List[int]:
        return list(range(7, 13))
    
    @staticmethod
    def speeds() -> List[int]:
        return list(range(180, 241, 10))
    
    @staticmethod
    def landings() -> List[int]:
        return list(range(300, 601, 25))
    
    @staticmethod
    def ranks() -> List[str]:
        return ["B","A","S",]
    
    @staticmethod
    def challenge_count() -> List[int]:
        return list(range(2,6))
    
    @staticmethod
    def challenge_count_hard() -> List[int]:
        return list(range(2,6))
    
    @staticmethod
    def challenge_count_fail_single() -> List[int]:
        return list(range(1,3))
    
    @staticmethod
    def challenges() -> List[str]:
        return [
            "Find the Portal (Any)",
            "Restore the World",
            "Capture Weebohs / Save as many Weebohs as you can!",
            "Survive (Any)",
            "Collect Sparks",
            "Collect Stars (Any)",
            "Catch the Captain/ Niada",
        ]
    
    @staticmethod
    def item_count() -> List[int]:
        return list(range(3, 6))
    
    @staticmethod
    def item_count() -> List[int]:
        return list(range(2, 4))
    
    @staticmethod
    def item_count_legendary() -> List[int]:
        return list(range(1, 3))
    
    @staticmethod
    def rarities() -> List[str]:
        return [
            "Common",
            "Rare",
            "Epic",
        ]
    
    @staticmethod
    def common_items() -> List[str]:
        return [
            "Rocket Boots",
            "Distance-Based Health Insurance",
            "Perpetual Motion Machine",
            "Shimmering Condenser",
            "Transition Slingshot",
            "Void Charger",
            "Pocket Snack",
            "Void Compressor",
            "Spark Furnace",
            "Restorative Maneuver",
            "Adrenaline",
            "Mortar and Pestle",
            "Dynamo Treadmill",
            "Shortcut",
            "Golden Necklace",
            "Replenishing Vial",
            "Big Pumpkin",
            "Aromatic Herbs",
        ]
    
    @staticmethod
    def rare_items() -> List[str]:
        return [
            "Clown Shoes",
            "Growth Potential",
            "Reheated Soup",
            "Intangibility",
            "Greed Machine",
            "Fragile Taco",
            "Speedy Recovery",
            "Big Squash",
            "Heart Shaped Mirror",
            "400-leaf Clover",
            "Spark Powered Propeller",
            "Interest",
            "Steady Investment",
            "High Risk Investment",
            "Jackpot",
            "Momentum Recalibrator",
            "Bitter Herbs",
            "Secret Technique Instructions",
            "Overclocked Medical Drone",
            "Big Spark Magnet",
            "Recyclable Rocket",
            "Emergency Shoes",
            "Plutonium Coin",
            "Shiny Anchor Pin",
            "Mysterious Spring",
            "Vitamins",
            "Heir's Determination",
            "Well Earned Confidence",
            "N-Dimensional-leaf Clover",
            "Performance Based Health Insurance",
            "Delayed Emergency Device",
            "Impulse Activated Stabilizer",
            "Protective Medallion",
            "Grunt's Helmet",
            "Standard Redirector",
            "Velocity Powered Syringe",
            "Personal Matter Stabilizer",
        ]
    
    @staticmethod
    def epic_items() -> List[str]:
        return [
            "Painful Coil",
            "Extreme Herbs",
            "BOOSTR POG",
            "Pungent Herbs",
            "Tight Schedule",
            "Steel Hat Lining",
            "Quick Taco",
            "Low Grade Timeline Swapper",
            "Friendly Looking Star",
            "Atomic Timepiece",
            "Time Dilation Thing",
            "Instant Compensation Machine",
            "Personal Gravity Enhancer",
            "Timeline Shifter",
            "Brittle Breastplate",
            "Energy Lash",
            "Fragile Confidence",
            "Planar Reconfiguration",
            "Karma",
            "Impact Activated Healing Drone",
            "Timeline Recalibrator",
            "Ring Materializer",
            "Timeline Refactor",
            "Overwound Pocketwatch",
            "General Relativity",
            "Leadership Pipe",
            "Spark Dasher",
        ]
    
    @staticmethod
    def legendary_items() -> List[str]:
        return [
            "Portable Harvester",
            "Blood Engine",
            "Experimental Autopilot",
            "Overcomplicated Coin",
            "Flashback",
            "Experiemtal Thrusters",
            "Otherworldly Contact",
            "Dangerous Investment Scheme",
            "Wingspan",
        ]
    
    @staticmethod
    def disaster() -> List[int]:
        return list(range(1,5))


class HasteTrialModes(OptionSet):
    """
    Defines what objective types can generate in keeps.

    Shard Completion: Complete Shards, may require you to do so with specific abilities.
    Endless Statistics: Complete objectives related to the final stat screen in Endless Mode (Perfect Landings, Completed Fragments, Max Speed, etc.).
    Challenge Completion: Complete challenges within any shard, or complete a specific challenge.
    Scavenger Hunt: Search for items, either an amount from certain tiers, or specific items.
    Disaster Mode: Complete specified Disaster level on the Final Shard.
    """
    display_name = "Haste Trial Modes"

    valid_keys = [
        "Shard Completion",
        "Endless Statistics",
        "Challenge Completion",
        "Scavenger Hunt",
        "Disaster Mode",
    ]

    default = valid_keys

class HasteAbilityOptions(OptionSet):
    """
    Determines which abilities can be rolled for objectives with a strict ability selection.
    """
    display_name = "Haste Ability Options"

    valid_keys = [
        "Courier's Board",
        "Wraith's Hourglass",
        "Heir's Javelin",
        "Sage's Cowl",
    ]

    default = valid_keys

class HasteMaximumDifficultyEndless(Choice):
    """
    Determines the highest difficulty Endless Statistics objectives will require.
    """

    display_name = "Haste Maximum Difficulty Endless"

    option_peaceful = 0
    option_easy = 1
    option_medium = 2
    option_hard = 3
    option_very_hard = 4

    default = 2