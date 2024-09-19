import os

from ... import Command
from ... import controllersConfig
from ...utils.logger import get_logger
from ..Generator import Generator

eslog = get_logger(__name__)

class CdogsGenerator(Generator):

    def generate(self, system, rom, playersControllers, metadata, guns, wheels, gameResolution):

        romdir = "/userdata/roms/cdogs"
        assetdirs = [
            "music/briefing",
            "music/end",
            "music/game",
            "music/victory",
            "music/lose",
            "music/menu",
            "missions/antares3consp.cdogscpn",
            "missions/spacepirates.cdogscpn/graphics",
            "missions/graveintent.cdogscpn",
            "missions/harmful_crysalis.cdogscpn/sounds",
            "missions/harmful_crysalis.cdogscpn/graphics",
            "missions/bem.cdogscpn",
            "missions/ai_insurgency.cdogscpn/graphics",
            "missions/doom.cdogscpn/sounds",
            "missions/doom.cdogscpn/graphics/chars/bodies/demon",
            "missions/custom/Wuzzy/gungame.cdogscpn/sounds",
            "missions/custom/Wuzzy/gungame.cdogscpn/graphics",
            "missions/custom/techdemo/spawnertest.cdogscpn",
            "missions/custom/techdemo/soundtest.cdogscpn/sounds",
            "missions/custom/techdemo/soundtest.cdogscpn/graphics",
            "missions/custom/techdemo/funwithguns.cdogscpn/sounds",
            "missions/custom/techdemo/funwithguns.cdogscpn/graphics",
            "missions/custom/techdemo/spritetest.cdogscpn",
            "missions/custom/techdemo/tiletest.cdogscpn",
            "missions/custom/techdemo/rescue.cdogscpn",
            "missions/custom/techdemo/minimal.cdogscpn",
            "missions/custom/techdemo/cyberdogs.cdogscpn/graphics/chars",
            "missions/custom/techdemo/cyberdogs.cdogscpn/graphics/chars/guns",
            "missions/custom/techdemo/static.cdogscpn",
            "missions/WOLF3D",
            "missions/zombie.cdogscpn",
            "missions/Sand.cdogscpn/sounds",
            "missions/Sand.cdogscpn/graphics",
            "missions/devhell.cdogscpn",
            "missions/distress.cdogscpn",
            "missions/ai_insurgency_2.cdogscpn/graphics",
            "missions/ogre.cdogscpn",
            "missions/most_classified_enemy.cdogscpn",
            "missions/terror.cdogscpn",
            "sounds/boom",
            "sounds/footsteps/wood",
            "sounds/footsteps/tile",
            "sounds/footsteps/mech",
            "sounds/footsteps/bones",
            "sounds/footsteps/gravel",
            "sounds/footsteps/grass",
            "sounds/footsteps/dog",
            "sounds/footsteps/water",
            "sounds/footsteps/metal",
            "sounds/footsteps/boots",
            "sounds/hits/dog_growl",
            "sounds/hits/knife_flesh",
            "sounds/hits/petrify",
            "sounds/hits/flesh",
            "sounds/hits/fist_flesh",
            "sounds/hits/fire",
            "sounds/hits/hard",
            "sounds/hits/knife_hard",
            "sounds/hits/gas",
            "sounds/slide",
            "sounds/chars/die/ogre",
            "sounds/chars/die/mech",
            "sounds/chars/die/man",
            "sounds/chars/die/zombie",
            "sounds/chars/die/alien",
            "sounds/chars/die/dog",
            "sounds/chars/die/woman",
            "sounds/chars/alert/ogre",
            "sounds/chars/alert/mech",
            "sounds/chars/alert/man",
            "sounds/chars/alert/zombie",
            "sounds/chars/alert/alien",
            "sounds/chars/alert/dog",
            "sounds/chars/alert/woman",
            "sounds/bang",
            "sounds/ricochet",
            "sounds/explosion",
            "graphics/hud",
            "graphics/tile/wood",
            "graphics/tile/grid",
            "graphics/tile/recessed2",
            "graphics/tile/grate",
            "graphics/tile/tile",
            "graphics/tile/hex",
            "graphics/tile/biggrid",
            "graphics/tile/checker",
            "graphics/tile/wood2",
            "graphics/tile/biggrid2",
            "graphics/tile/slab",
            "graphics/tile/recessed",
            "graphics/tile/dirt",
            "graphics/tile/cobble",
            "graphics/tile/striped",
            "graphics/tile/smallsquare2",
            "graphics/tile/flat",
            "graphics/tile/water",
            "graphics/tile/stone",
            "graphics/tile/smallsquare",
            "graphics/tile/metal",
            "graphics/door/office2/base/key",
            "graphics/door/office/base/key",
            "graphics/door/dungeon/base/key",
            "graphics/door/alien2/base/key",
            "graphics/door/dungeon2/base/key",
            "graphics/door/doom/base/key",
            "graphics/door/prison/base/key",
            "graphics/door/tech/base/key",
            "graphics/door/alien/base/key",
            "graphics/door/blast/base/key",
            "graphics/wall/techwall",
            "graphics/wall/colony",
            "graphics/wall/greenstain",
            "graphics/wall/plasteel",
            "graphics/wall/stone2",
            "graphics/wall/plasteel2",
            "graphics/wall/brick",
            "graphics/wall/station",
            "graphics/wall/rock",
            "graphics/wall/bunker",
            "graphics/wall/steel",
            "graphics/wall/panel",
            "graphics/wall/cobble",
            "graphics/wall/granite",
            "graphics/wall/hightech",
            "graphics/wall/stone",
            "graphics/wall/carbon2",
            "graphics/wall/carbon",
            "graphics/wall/steelwood",
            "graphics/wall/brick2",
            "graphics/wall/support",
            "graphics/editor/cursors",
            "graphics/keys/cube",
            "graphics/keys/office",
            "graphics/keys/dungeon",
            "graphics/keys/card",
            "graphics/keys/chip",
            "graphics/keys/plain2",
            "graphics/keys/plain",
            "graphics/keys/cube2",
            "graphics/chars/glasses",
            "graphics/chars/bodies/soldier",
            "graphics/chars/bodies/big_soldier",
            "graphics/chars/bodies/skinny",
            "graphics/chars/bodies/big_skinny",
            "graphics/chars/bodies/mech",
            "graphics/chars/bodies/none",
            "graphics/chars/bodies/base",
            "graphics/chars/bodies/dog",
            "graphics/chars/bodies/big",
            "graphics/chars/hats",
            "graphics/chars/heads",
            "graphics/chars/facehairs",
            "graphics/chars/hairs",
            "graphics/chars/guns",
            "graphics/exits/plate",
            "graphics/exits/hazard",
            "graphics/exits/hazard2",
            "graphics/exits/plate2",
            "graphics/particles",
            "dogfights/doom_e1m1.cdogscpn/graphics",
            "dogfights/cubicle.cdogscpn",
            "dogfights/temple_of_carnage.cdogscpn/graphics",
            "dogfights/de_dust.cdogscpn",
            "dogfights/map07.cdogscpn/sounds",
            "dogfights/map07.cdogscpn/graphics",
            "dogfights/dungeon.cdogscpn",
            "dogfights/dwango5_map01.cdogscpn/sounds",
            "dogfights/dwango5_map01.cdogscpn/graphics",
            "dogfights/spells_n_spikes.cdogscpn/graphics",
            "doc",
            "data/.wolf3d/WL6.cdogscpn",
            "data/.wolf3d/SD2.cdogscpn",
            "data/.wolf3d/SD2data.cdogscpn/graphics/wall/landscape",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/bodies/angel",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/bodies/bat",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/bodies/big_mutant",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/bodies/wizard",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/hairs",
            "data/.wolf3d/SD2data.cdogscpn/graphics/chars/guns",
            "data/.wolf3d/SD3.cdogscpn",
            "data/.wolf3d/WL1.cdogscpn",
            "data/.wolf3d/common.cdogscpn/graphics/wall/landscape",
            "data/.wolf3d/common.cdogscpn/graphics/chars/bodies/mutant",
            "data/.wolf3d/common.cdogscpn/graphics/chars/bodies/angel",
            "data/.wolf3d/common.cdogscpn/graphics/chars/bodies/big_mutant",
            "data/.wolf3d/common.cdogscpn/graphics/chars/bodies/wizard",
            "data/.wolf3d/common.cdogscpn/graphics/chars/hairs",
            "data/.wolf3d/common.cdogscpn/graphics/chars/guns",
            "data/.wolf3d/SOD.cdogscpn",
            "data/.wolf3d/SD3data.cdogscpn/graphics/wall/landscape",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/bodies/angel",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/bodies/bat",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/bodies/big_mutant",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/bodies/wizard",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/hairs",
            "data/.wolf3d/SD3data.cdogscpn/graphics/chars/guns",
        ]

        try:
            for assetdir in assetdirs:
                os.chdir(f"{romdir}/{assetdir}")
            os.chdir(romdir)
        except FileNotFoundError:
            eslog.error("ERROR: Game assets not installed. You can get them from the Batocera Content Downloader.")
            raise

        commandArray = ["cdogs"]

        return Command.Command(
            array=commandArray,
            env={
                'SDL_GAMECONTROLLERCONFIG': controllersConfig.generateSdlGameControllerConfig(playersControllers)
            })
