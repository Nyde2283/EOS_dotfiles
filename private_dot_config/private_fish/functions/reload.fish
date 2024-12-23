function reload
    if status is-interactive
        # Commands to run in interactive sessions can go here
        oh-my-posh init fish --config "~/.config/assets/unicorn.omp.json" | source
    end
end
