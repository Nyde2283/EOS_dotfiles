import functools
import subprocess



# yes_answers = ("", "Y", "y", "yes")

# default_yes = False

# sections = []

error_packages: list[list[str]] = []

def get_install_command(pacakge_manager: str):
    def get_process(package: str):
        return subprocess.Popen([pacakge_manager, '-Si', '--noconfirm', '--needed', package])
    return get_process

def install_packages(package_manager: str, packages: list[str]) -> int:
    get_process = get_install_command(package_manager)
    return_code = 0

    for package in packages:
        install_process = get_process(package)
        curr_return_code = install_process.wait()
        if curr_return_code != 0:
            error_packages[-1].append(package)
        return_code |= curr_return_code
    return return_code

def pacman_install(packages: list[str]) -> int:
    error_packages.append([])
    return_code = install_packages('pacman', packages)
    if return_code != 0:
        print(f"\nPackages which ended with non-zero code : {error_packages[-1]}")

    return return_code

def yay_install(packages: list[str]) -> int:
    error_packages.append([])
    return_code = install_packages('yay', packages)
    if return_code != 0:
        print(f"\nPackages which ended with non-zero code : {error_packages[-1]}")

    return return_code

def flatpak_install(packages: list[str]) -> int:
    def get_process(package: str):
        return subprocess.Popen(["flatpak", "info", package])
    error_packages.append([])
    return_code = 0

    for package in packages:
        install_process = get_process(package)
        curr_return_code = install_process.wait()
        if curr_return_code != 0:
            error_packages[-1].append(package)
        return_code |= curr_return_code

    if return_code != 0:
        print(f"\nPackages which ended with non-zero code : {error_packages[-1]}")

    return return_code

def headerize(header: str) -> str:
    return f"\n{"-"*76}\n{header:^76}\n{"-"*76}"

def flatten(l: list[list[str] | None]) -> list[str]:
    res = []
    for sub_l in l:
        if sub_l != None:
            res.extend(sub_l)

    return res

class Section:

    yes_answers = ("", "Y", "y", "yes")
    sections = []
    error_packages: list[list[str]] = []

    def __init__(self, header: str, input_msg: str, run_func):
        self.header = header
        self.input_msg = input_msg
        self.run_func = run_func
        self.default_to_yes = False
        Section.sections.append(self)

    def run(self) -> int:
        print(headerize(self.header))
        if self.default_to_yes:
            ans = ""
            print(self.input_msg)
        else:
            ans = input(self.input_msg)

        if ans not in Section.yes_answers:
            print(f"Skipping {self.header.lower()}")
            return 0

        return self.run_func()


# def build_section(header: str, input_msg: str):
#     def build_section(func):
#         @functools.wraps(func)
#         def section(*args, **kwargs) -> int:
#             print(headerize(header))
#             if default_yes:
#                 ans = ""
#                 print(input_msg)
#             else:
#                 ans = input(input_msg)

#             if ans not in yes_answers:
#                 print(f"Skipping {header}")
#                 return 0
#             return func(*args, **kwargs)

#         sections.append(section)
#         return section
#     return build_section

def ignore_sections(sections: list[Section]) -> list[int]:
    for i, section in enumerate(sections):
        print(f"[{i}] {section.header}")
    print("Ignore confirmation for sections ?")
    ans = input("Format your input as 1-3 for (1, 2, 3) or 0 3 4 for (0, 3, 4) or 1-3 5 for (1, 2, 3, 5) : ")
    sep_ans = ans.split(" ")
    confirmed_sections = []

    for sub_ans in sep_ans:
        try:
            dash_index = sub_ans.index('-')
            a = int(sub_ans[:dash_index])
            b = int(sub_ans[dash_index+1:])
            confirmed_sections.extend(range(a, b+1))
        except ValueError:
            confirmed_sections.append(int(sub_ans))

    for i in confirmed_sections:
        sections[i].default_to_yes = True
