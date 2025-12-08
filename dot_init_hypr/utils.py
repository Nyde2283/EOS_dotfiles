import functools
import subprocess
from typing import Self



error_packages: list[list[str]] = []



# ---------------------------------------------------------------------------- #
#                               INSTALL COMMANDS                               #
# ---------------------------------------------------------------------------- #

def install_packages(command: list[str], packages: list[str]) -> int:
    def get_process(package: str):
        return subprocess.Popen([*command, package])
    return_code = 0

    for package in packages:
        print(f"\n🔁 Running '{' '.join(command)} {package}'...")
        install_process = get_process(package)
        curr_return_code = install_process.wait()
        if curr_return_code != 0:
            error_packages[-1].append(package)
        return_code |= curr_return_code
    return return_code


def pacman_install(packages: list[str]) -> int:
    error_packages.append([])
    return_code = install_packages(['sudo', 'pacman', '-Si', '--noconfirm', '--needed'], packages)

    if return_code != 0:
        print(f"\n❌ Packages which ended with non-zero code : {error_packages[-1]}")
    else:
        print(f"\n✅ Pacman installation succeeded")

    return return_code


def yay_install(packages: list[str]) -> int:
    error_packages.append([])
    return_code = install_packages(['yay', '-Si', '--noconfirm', '--needed'], packages)

    if return_code != 0:
        print(f"\n❌ Packages which ended with non-zero code : {error_packages[-1]}")
    else:
        print(f"\n✅ Yay installation succeeded")

    return return_code


def flatpak_install(packages: list[str]) -> int:
    error_packages.append([])
    return_code = install_packages(['flatpak', 'info'], packages)

    if return_code != 0:
        print(f"\n❌ Packages which ended with non-zero code : {error_packages[-1]}")
    else:
        print(f"\n✅ Flatpak installation succeeded")

    return return_code


# ---------------------------------------------------------------------------- #
#                               GENERAL COMMANDS                               #
# ---------------------------------------------------------------------------- #

def run_command(command: str) -> int:
    split_command = command.split(' ')
    print(f"\n🔁 Running '{command}'...")
    process = subprocess.Popen(split_command)
    return_code = process.wait()
    if return_code != 0:
        print(f"\n❌ Failed to run '{command}'")
    else:
        print(f"\n✅ Successfully run '{command}'")

    return return_code


# ---------------------------------------------------------------------------- #
#                              SECTIONS MANAGEMENT                             #
# ---------------------------------------------------------------------------- #

def headerize(header: str) -> str:
    return f"\n{"-"*76}\n{header:^76}\n{"-"*76}"


def flatten(l: list[list[str] | None]) -> list[str]:
    res = []
    for sub_l in l:
        if sub_l != None:
            res.extend(sub_l)

    return res


class Options:
    def __init__(self, yes_opt: list[str], no_opt: list[str]):
        self.yes_opt = yes_opt
        self.no_opt = no_opt
        self.all_opt = yes_opt + no_opt
        for opt in self.all_opt:
            if opt.isupper():
                self.main = opt

    def __str__(self):
        result = "["
        for opt in self.all_opt[:-1]:
            result += f'{opt},'
        result += f'{self.all_opt[-1]}]'

        return result


class Section:

    sections: list[Self] = []

    @classmethod
    def ask_ignore_sections(clc):
        for i, section in enumerate(clc.sections):
            print(f"[{i}] {section.header}")
        print(f"Ignore confirmation for sections ? [0-{len(clc.sections)-1}]")
        ans = input("Format your input as 0 3 4 for (0, 3, 4) : ")
        if ans == "":
            confirmed_sections_index = []
        else:
            confirmed_sections_index = [int(a) for a in ans.split(" ")]

        for i in confirmed_sections_index:
            clc.sections[i].answer_default = True

    def __init__(self, header: str, input_msg: str, run_func, options: Options = None):
        self.header = header
        if options == None:
            self.options = Options(['Y'], ['n'])
        else:
            self.options = options
        self.input_msg = input_msg + f' {self.options} '
        self.run_func = run_func
        self.answer_default = False
        Section.sections.append(self)

    def run(self) -> int:
        print(headerize(self.header))
        if self.answer_default:
            ans = self.options.main
            print(self.input_msg)
        else:
            ans = input(self.input_msg)

        if ans == '':
            ans = self.options.main

        if ans in self.options.no_opt:
            print(f"Skipping {self.header.lower()}")
            return 0
        elif ans in self.options.yes_opt:
            return self.run_func()
        else:
            self.run()
