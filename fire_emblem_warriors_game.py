from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class FireEmblemWarriorsArchipelagoOptions:
    fire_emblem_warriors_trial_modes: FireEmblemWarriorsTrialModes
    fire_emblem_warriors_dlc_enabled: FireEmblemWarriorsDLCEnabled
    fire_emblem_warriors_enable_space_time_missions: FireEmblemWarriorsEnableSpaceTimeMissions

class FireEmblemWarriorsGame(Game):
    name = "Fire Emblem Warriors"
    platform = KeymastersKeepGamePlatforms.SW
    is_adult_only_or_unrated = False
    options_cls = FireEmblemWarriorsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.include_story:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Complete STORY on DIFFICULTY Difficulty",
                    data = {
                        "STORY": (self.story_chapter_max_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 10,
                ),
                GameObjectiveTemplate(
                    label = "Complete STORY on DIFFICULTY Difficulty",
                    data = {
                        "STORY": (self.story_chapter_low_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 3,
                ),
                GameObjectiveTemplate(
                    label = "Capture every Keep before completing STORY on DIFFICULTY Difficulty",
                    data = {
                        "STORY": (self.story_chapter_max_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 7,
                ),
            ])

        if self.include_story_character:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label = "Complete STORY on DIFFICULTY Difficulty with the following characters: CHARACTER",
                    data = {
                        "STORY": (self.story_chapter_max_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1),
                        "CHARACTER": (self.playable_characters, 4)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 5,
                ),
                GameObjectiveTemplate(
                    label = "Complete STORY on DIFFICULTY Difficulty with CHARACTER",
                    data = {
                        "STORY": (self.story_chapter_low_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1),
                        "CHARACTER": (self.playable_characters, 1)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 2,
                ),
                GameObjectiveTemplate(
                    label = "Capture every Keep before completing STORY on DIFFICULTY Difficulty with the following characters: CHARACTER",
                    data = {
                        "STORY": (self.story_chapter_max_deploy, 1),
                        "DIFFICULTY": (self.story_chapter_difficulties, 1),
                        "CHARACTER": (self.playable_characters, 4)
                    },
                    is_time_consuming = False,
                    is_difficult = False,
                    weight = 4,
                ),
            ])

        if self.include_history:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete MISSION_COUNT missions on the HISTORY map",
                    data = {
                        "MISSION_COUNT": (self.history_mission_count, 1),
                        "HISTORY": (self.history_mode_maps, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 12,
                )
            )

            if self.include_space_time:
                game_objective_templates.append(
                    GameObjectiveTemplate(
                        label = "Complete a Space-Time Distortion Mission on the HISTORY map",
                        data = {
                            "HISTORY": (self.history_mode_maps, 1)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 6,
                )
            )

        if self.include_history_characters:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Complete MISSION_COUNT missions on the HISTORY map using the following characters at least once: CHARACTER",
                    data = {
                        "MISSION_COUNT": (self.history_mission_count, 1),
                        "HISTORY": (self.history_mode_maps, 1),
                        "CHARACTER": (self.playable_characters, 6)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 4,
                )
            )

            if self.include_space_time:
                game_objective_templates.append(
                    GameObjectiveTemplate(
                        label = "Complete a Space-Time Distortion Mission on the HISTORY map with the following characters: CHARACTER",
                        data = {
                            "HISTORY": (self.history_mode_maps, 1),
                            "CHARACTER": (self.playable_characters,4)
                        },
                        is_time_consuming = False,
                        is_difficult = True,
                        weight = 2,
                )
            )

        if self.include_materials:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label = "Collect COUNT RARITY Materials",
                    data = {
                        "COUNT": (self.material_count, 1),
                        "RARITY": (self.rarities, 1)
                    },
                    is_time_consuming = True,
                    is_difficult = False,
                    weight = 10,
                )
            )

        return game_objective_templates

    @property
    def modes(self) -> List[str]:
        return sorted(self.archipelago_options.fire_emblem_warriors_trial_modes.value)
    
    @property
    def include_story(self) -> bool:
        return "Story Mode" in self.modes
    
    @property
    def include_story_character(self) -> bool:
        return "Story Mode with Characters" in self.modes
    
    @property
    def include_history(self) -> bool:
        return "History Mode" in self.modes
    
    @property
    def include_history_characters(self) -> bool:
        return "History Mode with Characters" in self.modes
    
    @property
    def include_materials(self) -> bool:
        return "Material Hunt" in self.modes

    @property
    def dlc_enabled(self) -> List[str]:
        return sorted(self.archipelago_options.fire_emblem_warriors_dlc_enabled.value)
    
    @property
    def include_awakening_dlc(self) -> bool:
        return "Awakening" in self.dlc_enabled
    
    @property
    def include_fates_dlc(self) -> bool:
        return "Fates" in self.dlc_enabled
    
    @property
    def include_shadow_dragon_dlc(self) -> bool:
        return "Shadow Dragon" in self.dlc_enabled
    
    def history_mode_maps(self) -> List[str]:
        history_mode_maps: List[str] = ["Invisible Ties","The Path is Yours","The Dark Pontifex","Noble Lady of Caelin","Together to the End","Hero Challenge"]

        if self.include_awakening_dlc:
            history_mode_maps.extend(["Scion of Legend","Emmeryn","Caravan Dancer"])

        if self.include_fates_dlc:
            history_mode_maps.extend(["Grief","Land of Gods","Cold Reception"])

        if self.include_shadow_dragon_dlc:
            history_mode_maps.extend(["A Brush in the Teeth","Princess Minerva","Knorda Market"])
        
        return history_mode_maps
    
    def playable_characters(self) -> List[str]:
        playable_characters: List[str] = [
            "Rowan",
            "Lianna",
            "Corrin",
            "Ryoma",
            "Hinoka",
            "Takumi",
            "Sakura",
            "Xander",
            "Camilla",
            "Leo",
            "Elise",
            "Chrom",
            "Lucina",
            "Robin",
            "Lissa",
            "Frederick",
            "Cordelia",
            "Anna",
            "Marth",
            "Caeda",
            "Tiki",
            "Celica",
            "Lyn"
        ]

        if self.include_awakening_dlc:
            playable_characters.extend(["Owain","Tharja","Olivia"])

        if self.include_fates_dlc:
            playable_characters.extend(["Azura","Oboro","Niles"])

        if self.include_shadow_dragon_dlc:
            playable_characters.extend(["Navarre","Minerva","Linde"])

        return playable_characters
    
    @property
    def include_space_time(self) -> bool:
        return self.archipelago_options.fire_emblem_warriors_enable_space_time_missions.value

    @staticmethod
    def story_chapter_max_deploy() -> List[str]:
        return [
            "Chapter 3 - Dragon Valley Temple",
            "Chapter 4 - Hero-King of the Desert",
            "Chapter 5 - The Dragon's Table",
            "Chapter 6 - Hoshidan Princess",
            "Chapter 7 - Hoshidan Prince",
            "Chapter 8 - High Prince Ryoma",
            "Chapter 9 - Nohrian Princess",
            "Chapter 10 - Nohrian Prince",
            "Chapter 11 - Crown Prince Xander",
            "Chapter 12 - An Orchestrated Battle",
            "Chapter 13 - What Happened to Corrin",
            "Chapter 14 - Seiging the Citadel",
            "Chapter 15 - Taking the World Tree",
            "Chapter 16 - The Imprisoned Prince",
            "Chapter 17 - Royal Blood",
            "Chapter 18 - Chaos Dragon's Might",
            "Chapter 19 - Reclaiming Home",
            "Chapter 20 - Clash at the World Tree",
            "Endgame - Chaos Dragon Velezark"
        ]
    
    @staticmethod
    def story_chapter_low_deploy() -> List[str]:
        return ["Prologue - Crumbling Peace","Chapter 1 - Home in Ruins","Chapter 2 - Woodlands Encounter"]
    
    @staticmethod
    def story_chapter_difficulties() -> List[str]:
        return [
            "Easy",
            "Normal",
            "Hard",
            "Lunatic"
        ]
    
    @staticmethod
    def history_mission_count() -> List[int]:
        return list(range(2,6))
    
    @staticmethod
    def rarities() -> List[str]:
        return ["Gold","Silver Character"]

    @staticmethod
    def material_count() -> List[int]:
        return list(range(3,9))
    
class FireEmblemWarriorsTrialModes(OptionSet):
    """
    Defines what objective types can generate in keeps.

    Story Mode - Complete a specific story chapter
    Story Mode with Character - Complete a specific story chapter with a specified set of characters
    History Mode - Includes objectives based around missions from available History Mode maps
    Material Hunt - Collect a certain amount of either gold or silver character materials
    """
    display_name = "Fire Emblem Warriors Trial Modes"

    valid_keys = [
        "Story Mode",
        "Story Mode with Characters",
        "History Mode",
        "History Mode with Characters",
        "Material Hunt"
    ]

    default = valid_keys

class FireEmblemWarriorsDLCEnabled(OptionSet):
    """
     Defines which DLC packs should be included in objectives.

    Awakening: includes Owain, Tharja, and Olivia as characters, and Caravan Dancer, Emmeryn, and Scion of Legend as additional History Mode maps
    Fates: includes Azura, Oboro, Niles as characters, and Grief, Land of Gods, and Cold Reception as additional History Mode Maps
    Shadow Dragon: includes Navarre, Minerva, and Linde as characters, and A Brush in the Teeth, Princess Minerva, and Knorda Market as additional History Mode maps
    """
    display_name = "Fire Emblem Warriors DLC Enabled"
        
    valid_keys = [
        "Awakening",
        "Fates",
        "Shadow Dragon"
    ]

    default = valid_keys

class FireEmblemWarriorsEnableSpaceTimeMissions(Toggle):
    """
    Defines whether objectives can generate to complete 'Space-Time' Missions from completing every mission in a History Mode map
    These missions tend to be difficult, and on average are 20-30 levels higher than the boss of the History Mode map
    """
    display_name = "Fire Emblem Warriors Enable Space-Time Missions"