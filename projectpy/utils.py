from __future__ import print_function

import sys
from colorama import init, Fore, Back, Style
init(autoreset=True)


def cprint(something, somethingelse, somethingelsesomething, heading = False, normal = False):
    if normal:
        print()
        print(Fore.YELLOW+"%s%s%s" %(something, somethingelse, somethingelsesomething))
        print()
        return
    
    if heading:
        print()
        print(Fore.BLUE+"%s"% ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED+"%18s"% (somethingelse), end="")
        print(Fore.BLUE+"%18s"% ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED+"%18s"% (somethingelsesomething), end="")
        print(Fore.BLUE+"%18s"% ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return
        
    else:
        print(Fore.BLUE+"%s"% ("||"), end="")

        print("%18s"% (somethingelse), end="")
        print(Fore.BLUE+"%18s"% ("||"), end="")

        print("%18s"% (somethingelsesomething), end="")
        print(Fore.BLUE+"%18s"% ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return
    
def copy_files(frem, to):
    import os
    return os.system("cp -rf %s %s"%(frem, to))