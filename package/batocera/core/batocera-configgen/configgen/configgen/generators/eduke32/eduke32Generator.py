from configparser import ConfigParser
import os

from ... import batoceraFiles
from ... import Command
from ... import controllersConfig
from ...utils.buildargs import parse_args
from ..Generator import Generator


class EDuke32Generator(Generator):
    def generate(self, system, rom, playersControllers, metadata, guns, wheels, gameResolution):
        # Core is either eduke32 or fury
        core = system.config["core"]
        config_dir = f"{batoceraFiles.CONF}/{core}"
        saves_dir = f"{batoceraFiles.SAVES}/{core}"
        config_file = f"{config_dir}/{core}.cfg"
        # A script file with console commands that are always ran when the game starts
        script_file = f"{config_dir}/autoexec.cfg"
        for path in [config_dir, saves_dir]:
            if not os.path.exists(path):
                os.mkdir(path)
        if not os.path.exists(config_file):
            with open(config_file, "x"):
                pass
        parser = ConfigParser(interpolation=None)
        # Override optionxform to stop implicit case conversions
        parser.optionxform = str
        # Configuration options found here: https://wiki.eduke32.com/wiki/Configuration_file_options
        # NB: Not all configuration options listed actually work e.g. showFPS, etc.
        # NB: In eduke32 configs, booleans must be integers
        with open(config_file, "r") as config:
            parser.read_file(config)
        if not parser.has_section("Screen Setup"):
            parser.add_section("Screen Setup")
        parser.set("Screen Setup", "ScreenWidth", str(gameResolution["width"]))
        parser.set("Screen Setup", "ScreenHeight", str(gameResolution["height"]))
        # The game should always be fullscreen
        parser.set("Screen Setup", "ScreenMode", "1")
        with open(config_file, "w") as config:
            parser.write(config)
        with open(script_file, "w") as script:
            script.write(
                f'// This file is automatically generated by eduke32Generator.py\n'
                f'bind "F12" "screenshot"\n'
                f'screenshot_dir "{batoceraFiles.SCREENSHOTS}"\n'
                f'r_showfps "{1 if system.getOptBoolean("showFPS") else 0}"\n'
                f'echo BATOCERA\n'  # Easy check when debugging
            )
        launch_args = [
            core,
            "-cfg", config_file,
            "-nologo" if system.getOptBoolean("nologo") else ""
        ]
        if core == "fury":
            launch_args += [
                "-gamegrp", os.path.basename(rom),
                "-j", os.path.dirname(rom)
            ]
        else:
            result = parse_args(launch_args, rom)
            if not result.okay:
                raise Exception(result.message)
        return Command.Command(
            array=launch_args,
            env={
                'SDL_GAMECONTROLLERCONFIG': controllersConfig.generateSdlGameControllerConfig(playersControllers)
            }
        )
