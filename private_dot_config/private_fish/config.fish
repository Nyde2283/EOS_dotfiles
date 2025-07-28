if status is-interactive
    # Commands to run in interactive sessions can go here
    # echo "Prosternez vous devant le grand poulpy, mascotte de la MP2I" | cowsay -f ~/.config/.assets/octopus.cow | lolcat
    # alias all-update "sudo apt update && sudo apt upgrade -y && sudo apt autopurge && sudo snap refresh && flatpak update"
    alias pipes "pipes.sh -p 4 -r 10000 -R"
    alias ls "eza --color always --long --no-permissions --no-filesize --no-user --no-time --icons always --group-directories-first --sort extension --grid"
    alias la "eza --color always --long --no-permissions --no-filesize --no-user --no-time --icons always --group-directories-first --sort extension --grid --all"
    alias lt "eza --color always --icons always --tree --level 2 --only-dirs --all"
    alias cz chezmoi
    alias lg "git log --oneline"
    bind \er 'echo; echo; commandline -f repaint'
    bind \cl 'reset ; commandline -f repaint'
    bind \cd 'exit'
    bind ctrl-alt-q 'reset ; source ~/.config/fish/config.fish ; commandline -f repaint ; echo "Prosternez vous devant le grand poulpy, mascotte de la MP2I" | cowsay -f ~/.config/.assets/octopus.cow | lolcat'
    bind \cq 'reset ; source ~/.config/fish/config.fish ; commandline -f repaint'
    bind \ea 'fish_list_all_current_token'
    bind \et 'fish_list_tree_current_token'
    bind \cf "fish_search; reload"
    bind \ef "fish_search_all; reload"
    bind \ec "fish_search_home; reload"
    bind ctrl-alt-c "fish_search_all_home; reload"
    bind \ei "fish_insert"
    source ~/.config/.assets/scripts/git_fzf.fish
    git_fzf_key_bindings
    oh-my-posh init fish --config "~/.config/.assets/unicorn.omp.json" | source
end

# opam configuration
source /home/nyde/.opam/opam-init/init.fish >/dev/null 2>/dev/null; or true
