from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

from Options import OptionSet

@dataclass
class ShinyPokemonHuntScarletVioletArchipelagoOptions:
    shiny_pokemon_hunt_scarlet_violet_dlc: ShinyPokemonHuntScarletVioletDLC
    shiny_pokemon_hunt_scarlet_violet_included_methods: ShinyPokemonHuntScarletVioletIncludedMethods

class ShinyPokemonHuntScarletVioletGame(Game):
    name = "Shiny Pokemon Hunt Scarlet/Violet"
    platform = KeymastersKeepGamePlatforms.SW
    is_adult_only_or_unrated = False
    options_cls = ShinyPokemonHuntScarletVioletArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Capture at least one TYPE type shiny Pokemon",
                data = {
                    "TYPE": (self.types, 1)
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label = "Capture a Shiny Pokemon in AREA",
                data = {
                    "AREA": (self.all_locations, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 8
            ),
            GameObjectiveTemplate(
                label = "Capture a Shiny Pokemon in BROAD_AREA",
                data = {
                    "BROAD_AREA": (self.all_locations_broad, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            ),
        ])

        if self.include_outbreaks:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Capture a Shiny Pokemon in a Mass Outbreak in BROAD_AREA",
                    data = {
                        "BROAD_AREA": (self.all_locations_broad, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 3
                )
            )
        
        if self.include_eggs:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Hatch a Shiny Pokemon from an egg",
                    data = dict(),
                    is_time_consuming = True,
                    is_difficult = True,
                    weight = 2
                )
            )

        return game_objective_templates

    @property
    def dlc_enabled(self) -> List[str]:
        return sorted(self.archipelago_options.shiny_pokemon_hunt_scarlet_violet_dlc.value)
    
    @property
    def include_teal_mask(self) -> bool:
        return "The Teal Mask" in self.dlc_enabled
    
    @property
    def include_indigo_disk(self) -> bool:
        return "The Indigo Disk" in self.dlc_enabled
    
    @property
    def methods_included(self) -> List[str]:
        return sorted(self.archipelago_options.shiny_pokemon_hunt_scarlet_violet_included_methods.value)
    
    @property
    def include_outbreaks(self) -> bool:
        return "Mass Outbreak" in self.methods_included
    
    @property
    def include_eggs(self) -> bool:
        return "Masuda Hatching" in self.methods_included

    @staticmethod
    def locations_paldea() -> List[str]:
        return [
            "Poco Path",
            "Cabo Poco",
            "South Province (Area One)",
            "South Province (Area Two)",
            "South Province (Area Three)",
            "South Province (Area Four)",
            "South Province (Area Five)",
            "South Province (Area Six)",
            "East Province (Area One)",
            "East Province (Area Two)",
            "East Province (Area Three)",
            "Tagtree Thicket",
            "North Province (Area One)",
            "North Province (Area Two)",
            "North Province (Area Three)",
            "Glaseado Mountain",
            "Dalizapa Passage"
            "West Province (Area One)",
            "West Province (Area Two)",
            "West Province (Area Three)",
            "Asado Desert",
            "Casseroya Lake",
            "Any Paldean Sea",
            "Fury Falls",
            "Soccarat Trail",
            "The Great Crater of Paldea - Area Zero"
        ]
    
    @staticmethod
    def locations_kitakami() -> List[str]:
        return [
            "Kitakami - Mossfell Confluence",
            "Kitakami - Kitakami Road",
            "Kitakami - Reveler's Road",
            "Kitakami - Fellhorn Gorge",
            "Kitakami - Timeless Woods",
            "Kitakami - Kitakami Wilds",
            "Kitakami - Paradise Barrens",
            "Kitakami - Wistful Fields",
            "Kitakami - Loyalty Plaza/Apple Hills",
            "Kitakami - Infernal Pass",
            "Kitakami - Oni Mountain/Oni's Maw",
            "Kitakami - Crystal Pool"
        ]
    
    @staticmethod
    def locations_blueberry() -> List[str]:
        return [
            "Blueberry Terrarium's Canyon Biome",
            "Blueberry Terrarium's Polar Biome",
            "Blueberry Terrarium's Coastal Biome",
            "Blueberry Terrarium's Savannah Biome",
            "Blueberry Terrarium's Chargestone Cavern"
        ]
    
    def all_locations(self) -> List[str]:
        all_locations: List[str] = self.locations_paldea()

        if self.include_teal_mask:
            all_locations.extend(self.locations_kitakami())

        if self.include_indigo_disk:
            all_locations.extend(self.locations_blueberry())

        return all_locations

    def all_locations_broad(self) -> List[str]:
        all_locations: List[str] = [
            "Paldea's North Province",
            "Paldea's South Province",
            "Paldea's East Province",
            "Paldea's West Province"
        ]

        if self.include_teal_mask:
            all_locations.append("Kitakami")

        if self.include_indigo_disk:
            all_locations.append("Blueberry Terrarium")

        return all_locations

    @staticmethod
    def types() -> List[str]:
        return [
            "Normal",
            "Fire",
            "Fighting",
            "Water",
            "Flying",
            "Grass",
            "Poison",
            "Electric",
            "Ground",
            "Psychic",
            "Rock",
            "Ice",
            "Bug",
            "Dragon",
            "Ghost",
            "Dark",
            "Steel",
            "Fairy"
        ]

class ShinyPokemonHuntScarletVioletDLC(OptionSet):
    """
    Defines what DLC objectives can generate with.
    """
    display_name = "Shiny Pokemon Hunt Scalet/Violet DLC"

    valid_keys = [
        "The Teal Mask",
        "The Indigo Disk"
    ]

    default = valid_keys

class ShinyPokemonHuntScarletVioletIncludedMethods(OptionSet):
    """
    Defines whether or not to include hatching Eggs as objectives.

    By default, there will be broad "Catch a shiny" objectives with no method attatched.
    Adding methods below adds a new objective type 
    """
    display_name = "Shiny Pokemon Hunt Scarlet/Violet Included Methods"

    valid_keys = [
        "Mass Outbreak",
        "Masuda Hatching"
    ]

    default = valid_keys