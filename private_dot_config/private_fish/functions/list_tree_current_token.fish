function list_tree_current_token
    set -l val (commandline -t | string replace -r '^~' "$HOME")
    printf "\n"
    if test -d $val
        lt $val
    else
        set -l dir (dirname -- $val)
        if test $dir != . -a -d $dir
            lt $dir
        else
            lt
        end
    end

    string repeat -N \n --count=(math (count (fish_prompt)) - 1)

    commandline -f repaint
end
