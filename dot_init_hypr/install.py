from utils import *
import config



# ---------------------------------------------------------------------------- #
#                                   SECTIONS                                   #
# ---------------------------------------------------------------------------- #

# ---------------------------------- UPDATE ---------------------------------- #

def update_func() -> int:
    return_code = run_command('yay -Syu')
    return return_code
update = Section(
    "Updates",
    "Run system upgrade ?",
    update_func
)


# ----------------------------------- FONTS ---------------------------------- #

def font_install_func() -> int:
    fonts = config.fonts

    return_code = pacman_install(fonts)
    return return_code
font_install = Section(
    "Font installation",
    "Install fonts ?",
    font_install_func
)


# ------------------------------ MINIMAL INSTALL ----------------------------- #

def minimal_install_func() -> int:
    packages = config.minimal_packages

    return_code = pacman_install(packages)
    return return_code
minimal_install = Section(
    "Minimal installation",
    "Install minimal software config ?",
    minimal_install_func
)


# ------------------------------- SHELL CONFIG ------------------------------- #

def shell_config_func() -> int:
    return_code = run_command('sudo chsh -s /usr/bin/fish')
    print("\
Veillez configurer les variables suivantes dans l'éditeur qui va apparaitre :\
BROWSER=zen-browser\
EDITOR=micro\
SHELL=/usr/bin/fish\
")
    input("Press any key to continue...")

    return_code |= run_command('micro /etc/environment')
    return_code |= run_command('~/.init_hypr/fish_functions')

    return return_code
shell_config = Section(
    "SHELL configuration",
    "Configure default shell to fish ?",
    shell_config_func
)


# ------------------------------- COMPATIBILITY ------------------------------ #

def compatibilty_layers_func() -> int:
    packages = config.compatibility_packages

    return pacman_install(packages)
compatibilty_layers = Section(
    "Compatibilty layers",
    "Install compatibility layers ?",
    compatibilty_layers_func
)


# --------------------------- SYSTEMD CONFIGURATION -------------------------- #

def systemd_config_func() -> int:
    # Enable services
    return_code = run_command('sudo systemctl enable sddm.service')                 # Login service
    return_code |= run_command('sudo systemctl enable bluetooth.service')           # Bluetooth service
    return_code |= run_command('systemctl --user enable hyprpolkitagent.service')   # GUI sudo prompt

    # Enable numlock in sddm
    return_code |= run_command('sudo touch /etc/sddm.conf')
    return_code |= run_command('sudo bash -c \'echo "[General]\
Numlock=on\
[Autologin]\
User=nyde\
Session=hyprland-uwsm.desktop" > /etc/sddm.conf\'')

    return return_code
systemd_config = Section(
    "Systemd configuration",
    "Configure systemd ?",
    systemd_config_func
)


# def fix_g502_func() -> int:
#     return 0
#     return_code = run_command('sudo bash -c \'echo "[DisableThatShitHighResolution]\
# MatchName=*\
# AttrEventCode=-REL_WHEEL_HI_RES;-REL_HWHEEL_HI_RES;" > /etc/libinput/local-overrides.quirks\'')
#     return_code |= run_command('sudo bash -c \'echo "blacklist hid_logitech_hidpp" > /etc/modprobe.d/blacklist.conf\'')

#     return return_code
# fix_g502 = Section(
#     "G502 scrolling fix",
#     "Fix Logitech G502 mouse scrolling issues ?",
#     fix_g502_func
# )


# ----------------------- GENERAL PACKAGE INSTALLATION ----------------------- #

def general_packages_install_func() -> int:
    pacman_packages = config.general_pacman_packages
    yay_packages = config.general_yay_packages
    flatpak_packages = config.general_flatpak_packages

    print("\
Les package installés avec yay peuvent être long à installer (notamment ags-hyprpanel qui prend un temps fou).\
Avant de partir du principe que l'installation est bloquée ou boucle dans le vide, attendez au moins 15 minutes.")
    input("Press any key to continue...")

    return_code = pacman_install(pacman_packages)
    return_code |= yay_install(yay_packages)
    return_code |= flatpak_install(flatpak_packages)
    return_code |= run_command('sudo cp org.gnome.Calculator.desktop /usr/share/applications/')   # Put desktop entry in correct directory
    return return_code
general_packages_install = Section(
    "General packages installation",
    "Install all useful softwares ?",
    general_packages_install_func
)


# ---------------------------------- RICING ---------------------------------- #

def rice_system_func() -> int:
    pacman_packages = config.rice_pacman_packages
    yay_packages = config.rice_yay_packages

    return_code = pacman_install(pacman_packages)
    return_code |= yay_install(yay_packages)
    return_code |= run_command('gsettings set org.gnome.desktop.interface gtk-theme "Arc-Dark"')
    return_code |= run_command('gsettings set org.gnome.desktop.interface color-scheme \'prefer-dark\'')
    return return_code
rice_system = Section(
    "Ricing configuration",
    "Rice the system ?",
    rice_system_func
)


# --------------------------- GROUPS CONFIGURATION --------------------------- #

def groups_config_func() -> int:
    return_code = run_command('sudo usermod -aG lp $USER')   # Add user to printing group
    return return_code
groups_config = Section(
    "Groups configuration",
    "Configure groups (relevant to use printers) ?",
    groups_config_func
)


# ----------------------- SYSTEMD GENERAL CONFIGURATION ---------------------- #

def systemd_general_config_func() -> int:
    return_code |= run_command('sudo systemctl enable numLockOnTty.service')        # Turn on numlock on tty
    return_code |= run_command('sudo systemctl enable cups')                        # Enable printer system
    return_code |= run_command('systemctl --user enable hypridle.service')          # Hidle service
    return_code |= run_command('systemctl --user enable --now hyprpaper.service')   # Wallpaper service

    return return_code
systemd_general_config = Section(
    "Systemd configuration for general softwares",
    "Configure systemd ?",
    systemd_config_func
)


# ----------------------------- XDG CONFIGURATION ---------------------------- #

def xdg_configuration_func() -> int:
    return_code = run_command('sudo ln -s /usr/bin/kitty /usr/bin/xdg-terminal-exec')           # Open TUI apps (Btop, Micro, ...) inside Kitty instead of Xterm
    return_code |= run_command('sudo ln -s /usr/bin/kitty /usr/bin/gnome-terminal')             # Nautilus 'Open terminal here' option open Kitty instead of Xterm
    return_code |= run_command('xdg-mime default org.gnome.Nautilus.desktop inode/directory')   # Set Nautilus as default file manager

    return return_code
xdg_configuration = Section(
    "XDG configuration",
    "Configure XDG settings ?",
    xdg_configuration_func
)


# --------------------------- YDOTOOL CONFIGURATION -------------------------- #

def ydotool_config_func() -> int:
    return_code = run_command('sudo chmod +s /usr/bin/ydotoold')
    return_code |= run_command('sudo chmod +s /usr/bin/ydotool')

    return return_code
ydotool_config = Section(
    "Ydotool configuration",
    "Allow to run ydotool in sudo mode by default ?",
    ydotool_config_func
)


# ---------------------------- WORKING DIRECTORIES --------------------------- #

def work_dirs_func() -> int:
    print("Creating directories...")
    return_code = run_command('mkdir ~/Documents/dev')
work_dirs = Section(
    "Working dirs",
    "Create working directories ?",
    work_dirs_func
)


# ----------------------- NVIDIA DRIVERS CONFIGURATION ----------------------- #

def nvidia_drivers_conf_func() -> int:
    return_code = run_command('sudo pacman -Rns nvidia')   # Remove Proprietary Drivers because I'm with a RTX 20xx
    return_code |= pacman_install(['nvidia-open'])         # Install Open Drivers
nvidia_drivers_conf = Section(
    "NVIDIA drivers configuration",
    "Configure NVIDIA drivers (Only if you know what you are doing) ?",
    nvidia_drivers_conf_func
)



if __name__ == "__main__":
    Section.ask_ignore_sections()

    try:
        for section in Section.sections:
            section.run()

        print("\
Pensez à changer le thème de GRUB avec grub-customizer.\
Pour ajouter un dual boot, exécutez sudo os-prober avant.\
Si vous avez un dual boot Windows, exécutez timedatectl set-local-rtc 1 --adjust-system-clock pour régler le problème du différentiel d'heure entre Windows et Linux\
Sur Zen Browser, pour enlever la bordure un peu chiante il faut set la variable zen.theme.content-element-separation à 0.")
    except:
        pass

    print(f"\nPackages which ended with non-zero code : {flatten(error_packages)}")
