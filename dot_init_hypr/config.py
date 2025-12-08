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

minimal_packages = [
    "hyprland",   # Window manager
    "sddm",       # Login manager
    "uwsm",       # Universal Wayland Session Manager
    "kitty",      # Terminal emulator
    "fish",       # Fancy SHELL
    "micro"       # Fancy Nano
]

compatibility_packages = [
    "xdg-desktop-portal-hyprland",
    "xdg-desktop-portal-gtk",
    "hyprpolkitagent",
    "qt5-wayland",
    "qt6-wayland"
]

general_pacman_packages = [
    "nautilus",                   # File manager
    "nautilus-image-converter",
    "cliphist",                   # Clipboard
    "cowsay",                     # Funny greating in terminal
    "lolcat",                     # Colorfull greating in terminal
    "btop",                       # Task manager
    "mission-center",             # GUI Task manager
    "zathura",                    # PDF viewer
    "zathura-pdf-poppler",        # Add PDF support to zathura
    "pdfarranger",                # PDF split/merge utility
    "evince",                     # PDF thumbnailer
    "eza",                        # Fancy ls
    "bluetui",                    # Bluetooth manager TUI
    "hyprpicker",                 # Color picker
    "hyprlock",                   # Screen locker
    "bat",                        # Fancy cat
    "fd",                         # Fancy find
    "imv",                        # Image viewer
    "loupe",                      # GNOME image viewer
    "vlc",                        # Video player
    "vlc-plugin-ffmpeg",          # Ffmpeg support for vlc
    "wev",                        # Debug input for Hyprland
    "udiskie",                    # Auto mount disks
    "playerctl",                  # Allow media keys to work
    "baobab",                     # Disk usage analyzer
    "flatpak",                    # Forbiden package manager
    "ydotool",                    # Input emulator
    "brightnessctl",              # Brightness manager
    "partitionmanager",           # Partition manager
    "cups",                       # Printer system
    "system-config-printer",      # Printer configurator
    "foot",                       # Fast terminal emulator used by Alt+Tab
    "chafa",                      # Image to Unicode converter used by Alt+Tab
    "network-manager-applet",     # Network manager GUI
    "thunderbird",                # Mail Client
    "yazi",                       # TUI File manager
    "chromium",                   # A better browser (only for CSS coding)
    "hyprpaper",                  # Hyprland's wallpaper manager
    "typst",                      # Typst > Latex
    "libreoffice-fresh",          # Just Libre Office
    "signal-desktop"              # WhatsApp but private
]

general_yay_packages = [
    "nautilus-admin-gtk4",
    "nautilus-open-any-terminal",
    "zen-browser-bin",              # Browser
    "ags-hyprpanel-git",            # Status bar
    "tofi",                         # App/Emoji/Clipboard launcher
    "rofimoji-git",                 # Emoji feeder for Tofi
    "hypridle",                     # Hidle manager
    "wlogout",                      # Logout options menu
    "grim-hyprland-git",            # Screenshot utility
    "grimblast-git",                # Screenshot manager
    "hyprls-git",                   # Language server for Hyprland config
    "grub-customizer",              # GUI to customize GRUB
    "xorg-xhost",                   # Missing dependency for grub-customizer
    "ookla-speedtest-bin",          # Ookla's speedtest CLI
    "ente-auth-bin",                # 2FA codes manager
    "samsung-unified-driver",       # Drivers for Samsung's printers
    "freedownloadmanager",          # Download manager, need browser extension to work
    "pyprland",                     # Plugin manager, used for scratchpads
    "anki-bin",                     # Learning with cards
    "informant",                    # Prevent update if fresh Arch news post
    "github-desktop-plus-bin",      # For GUI lovers
    "visual-studio-code-bin",       # Sry VIM, I take showers
    "vesktop-bin",                  # Fancy Discord
    "spotify",                      # Spotify, that's it
    "systemd-numlockontty"          # Enable numlock on tty
]

general_flatpak_packages = [
    "org.gnome.Calculator",   # Basic calculator
    "org.kiwix.desktop"       # Offline reader for Wikipedia
]

rice_pacman_packages = [
    "arc-gtk-theme-eos",   # EndeavourOS theme
    "fastfetch"            # Fancy system info
]

rice_yay_packages = [
    "pipes.sh",        # PIPES EVERYWHERE
    "oh-my-posh-bin"   # Fancy SHELL prompt
]
