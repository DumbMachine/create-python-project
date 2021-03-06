from __future__ import print_function

import json
import os
import readline
import sys

import yaml
from colorama import Back, Fore, Style, init
from loguru import logger

from .config import *

init(autoreset=True)

logger.add(sys.stderr, format="{time} {level} {message}",
           filter="my_module", level="INFO")


def cprint(
        something,
        somethingelse,
        somethingelsesomething,
        heading=False,
        normal=False):
    if normal:
        print()
        print(Fore.YELLOW + "%s%s%s" %
              (something, somethingelse, somethingelsesomething))
        print()
        return

    if heading:
        print()
        print(Fore.BLUE + "%s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED + "%18s" % (somethingelse), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED + "%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return

    else:
        print(Fore.BLUE + "%s" % ("||"), end="")

        print("%18s" % (somethingelse), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="")

        print("%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return


def progressBar(value, endvalue, message, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print(Fore.CYAN +
          "\rPercent: [{0}] {1}: {2} %".format(arrow +
                                               spaces, int(round(percent *
                                                                 100)), message), file=sys.stdout, end=" ")
    sys.stdout.flush()


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


def custom_reader(location):
    '''
    '''
    # thing = yaml.load(custom, Loader=yaml.Loader)
    thing = yaml.load(open(location), Loader=yaml.Loader)

    files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    shields = [
        "build",
        "codecov",
        "analysis",
        "chat",
        "dependencies",
        "size",
        "downloads",
        "funding",
        "issues",
        "license",
        "rating",
        "social",
        "version",
        "platform",
        "monitoring",
        "activity",
        "other",
        "custom_shield",
    ]

    conf = Config()
    conf.options['config_location'] = location
    for item in thing.keys():
        if item in files:
            conf.options['files'][item] = thing[item]
        elif item == 'shields':
            for small_item in thing[item].keys():
                conf.options['shields'].append(
                    thing[item][small_item])
        else:
            # try:
            conf.options[item] = thing[item]
    return conf


def writer_writer(conf):
    '''
    Used to write shyat
    '''
    for writes in conf.options['files'].keys():
        if writes == 'license' and conf.options['files'][writes]:
            conf.actions[writes](
                location=f"./{conf.options['project_name']}",
                license_type=conf.options['files']['license'])

        elif writes == 'setup_py':
            conf.actions[writes](
                f"./{conf.options['project_name']}", conf.options)

        elif writes == 'main':
            conf.actions[writes](
                f"./{conf.options['project_name']}", conf.options['project_name'])

        elif writes == 'manifest' or writes == 'dockerfile':
            conf.actions[writes](
                f"./{conf.options['project_name']}", name=conf.options['project_name']
            )

        elif writes == 'color' or writes == 'interactive':
            continue

        elif writes == 'git':
            conf.actions[writes](f"./{conf.options['project_name']}")

        else:
            try:
                conf.actions[writes](
                    f"./{conf.options['project_name']}")
            except Exception as e:
                print(
                    f"The following exception occured while doing something\n{e}")
                pass
    try:
        from .generator import generate_README
        generate_README(os.path.join(
            '.', f"./{conf.options['project_name']}"), shields=conf.options['shields'])

    except Exception as e:
        print(e)
        raise RuntimeError('There was a problem generating the README.md')
