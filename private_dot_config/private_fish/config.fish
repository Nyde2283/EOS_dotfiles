if status is-interactive
    # Commands to run in interactive sessions can go here
    echo "Prosternez vous devant le grand poulpy, mascotte de la MP2I" | cowsay -f octopus | lolcat
    # alias speedtest ~/.apps/Speedtest/speedtest
    # alias all-update "sudo apt update && sudo apt upgrade -y && sudo apt autopurge && sudo snap refresh && flatpak update"
    alias pipe "pipes.sh -p 4 -r 10000 -R"
    alias ls "eza --color always --long --no-permissions --no-filesize --no-user --no-time --icons always --group-directories-first --sort extension --grid"
    alias la "eza --color always --long --no-permissions --no-filesize --no-user --no-time --icons always --group-directories-first --sort extension --grid --all"
    alias lt "eza --color always --icons always --tree --level 2 --only-dirs --all"
    alias cz chezmoi
    alias i "cd ~/Documents/MPI/Info"
    alias m "cd ~/Documents/MPI/Maths"
    alias p "cd ~/Documents/MPI/Physique"
    alias t "cd ~/Documents/TIPE"
    alias mpi "cd ~/Documents/MPI"
    alias tipe "cd ~/Documents/TIPE"
    bind \er 'echo; echo; commandline -f repaint'
    bind \cl 'clear ; commandline -f repaint'
    bind \cq 'clear ; source ~/.config/fish/config.fish ; commandline -f repaint'
    bind \ea list_all_current_token
    bind \et list_tree_current_token
    bind \cf "fcd; reload"
    bind \ef "fcd_all; reload"
    bind \ec "fcd_home; reload"
    bind \ei fcd_insert
    set -gx PATH $PATH /home/nyde/.local/bin
    oh-my-posh init fish --config "~/.config/assets/unicorn.omp.json" | source
end

# opam configuration
source /home/nyde/.opam/opam-init/init.fish >/dev/null 2>/dev/null; or true
