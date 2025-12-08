import subprocess
from utils import *



# ---------------------------------------------------------------------------- #
#                                   SECTIONS                                   #
# ---------------------------------------------------------------------------- #

def update_func() -> int:
    print("Running update...")
    return 0
update = Section(
    "Updates",
    "Run system upgrade ? [Y,n] ",
    update_func
)

# @build_section(
#     "Font installation",
#     "Install fonts ? [Y,n] "
# )
def font_install_func() -> int:
    fonts = [
        "ttf-cascadia-code-nerd",
        "ttf-cascadia-mono-nerd",
        "ttf-fira-code",
        "ttf-fira-mono",
        "ttf-fira-sans",
        "ttf-firacode-nerd",
        "ttf-iosevka-nerd",
        "ttf-iosevkaterm-nerd",
        "ttf-jetbrains-mono-nerd",
        "ttf-jetbrains-mono",
        "ttf-nerd-fonts-symbols",
        "ttf-nerd-fonts-symbols",
        "ttf-nerd-fonts-symbols-mono"
    ]

    return pacman_install(fonts)
font_install = Section(
    "Font installation",
    "Install fonts ? [Y,n] ",
    font_install_func
)

@build_section(
    "Minimal installation",
    "Install minimal software config ? [Y,n] "
)
def minimal_install_func() -> int:
    packages = [
        "hyprland",
        "sddm",
        "uwsm",
        "kitty",
        "fish",
        "micro"
    ]

    return pacman_install(packages)
minimal_install = Section(

)

@build_section(
    "SHELL configuration",
    "Configure default shell to fish ? [Y,n] "
)
def shell_config() -> int:
    print("Configuring...")
    return 0

@build_section(
    "Compatibilty layers",
    "Install compatibility layers ? [Y,n] "
)
def compatibilty_layers() -> int:
    packages = [
        "xdg-desktop-portal-hyprland",
        "xdg-desktop-portal-gtk",
        "hyprpolkitagent",
        "qt5-wayland",
        "qt6-wayland"
    ]

    return pacman_install(packages)

@build_section(
    "Systemd configuration",
    "Configure systemd ? [Y,n] "
)
def systemd_config() -> int:
    print("Configuring...")
    return 0

@build_section(
    "G502 scrolling fix",
    "Fix Logitech G502 mouse scrolling issues ? [Y,n] "

)
def fix_g502() -> int:
    print("Fixing...")
    return 0

@build_section(
    "General packages installation",
    "Install all useful softwares ? [Y,n] "
)
def general_packages_install() -> int:
    pacman_packages = [
        "nautilus",
        "nautilus-image-converter",
        "cliphist",
        "cowsay",
        "lolcat",
        "btop",
        "mission-center",
        "zathura",
        "zathura-pdf-poppler",
        "pdfarranger",
        "evince",
        "eza",
        "bluetui",
        "hyprpicker",
        "hyprlock",
        "bat",
        "fd",
        "imv",
        "loupe",
        "vlc",
        "vlc-plugin-ffmpeg",
        "wev",
        "udiskie",
        "playerctl",
        "baobab",
        "flatpak",
        "ydotool",
        "brightnessctl",
        "partitionmanager",
        "cups",
        "system-config-printer",
        "foot",
        "chafa",
        "network-manager-applet",
        "thunderbird",
        "yazi",
        "chromium",
        "hyprpaper",
        "typst",
        "libreoffice-fresh",
        "signal-desktop"
    ]
    yay_packages = [
        "nautilus-admin-gtk4",
        "nautilus-open-any-terminal",
        "zen-browser-bin",
        "ags-hyprpanel-git",
        "tofi",
        "rofimoji-git",
        "hypridle",
        "wlogout",
        "grim-hyprland-git",
        "grimblast-git",
        "hyprls-git",
        "grub-customizer",
        "xorg-xhost",
        "ookla-speedtest-bin",
        "ente-auth-bin",
        "samsung-unified-driver",
        "freedownloadmanager",
        "pyprland",
        "anki-bin",
        "informant",
        "github-desktop-plus-bin",
        "visual-studio-code-bin",
        "vesktop-bin",
        "spotify",
        "systemd-numlockontty"
    ]
    flatpak_packages = [
        "org.gnome.Calculator",
        "org.kiwix.desktop"
    ]

    pacman_return_code = pacman_install(pacman_packages)
    yay_return_code = yay_install(yay_packages)
    flatpak_return_code = flatpak_install(flatpak_packages)
    return pacman_return_code | yay_return_code | flatpak_return_code

@build_section(
    "Ricing configuration",
    "Rice the system ? [Y,n] "
)
def rice_system() -> int:
    pacman_packages = [
        "arc-gtk-theme-eos",
        "fastfetch"
    ]
    yay_packages = [
        "pipes.sh",
        "oh-my-posh-bin"
    ]

    pacman_return_code = pacman_install(pacman_packages)
    yay_return_code = yay_install(yay_packages)
    return pacman_return_code | yay_return_code

@build_section(
    "Groups configuration",
    "Configure groups (relevant to use printers) ? [Y,n] "
)
def groups_config() -> int:
    print("Configuring...")
    return 0

@build_section(
    "Systemd configuration for general softwares",
    "Configure systemd ? [Y,n] "
)
def systemd_general_config() -> int:
    print("Configuring general systemd...")
    return 0

@build_section(
    "XDG configuration",
    "Configure XDG settings ? [Y,n] "
)
def xdg_configuration() -> int:
    print("Configuring XDG...")
    return 0

@build_section(
    "Ydotool configuration",
    "Allow to run ydotool in sudo mode by default ? [Y,n] "
)
def ydotool_config() -> int:
    print("Autorizing")
    return 0

@build_section(
    "Working dirs",
    "Create working directories ? [Y,n] "
)
def work_dirs() -> int:
    print("Creating directories...")
    return 0



if __name__ == "__main__":
    ans = input("Do you want to skip confirmations ? [Y,n] ")
    if ans in yes_answers:
        set_default_to_yes()

    try:
        for section in sections:
            print(section())
    except:
        pass

    print(f"\nPackages which ended with non-zero code : {flatten(error_packages)}")






"""
from time import sleep
# process = subprocess.Popen(['sleep', '0.2'])
process = subprocess.Popen(['echo', 'exit(2)'], stdout=subprocess.PIPE)
process.wait()
# sleep(1)
proc = subprocess.Popen(['python'], stdin=process.stdout)
sleep(0.5)
print(proc.wait())
"""
