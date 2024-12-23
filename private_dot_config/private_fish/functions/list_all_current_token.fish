function list_all_current_token
    set -l val (commandline -t | string replace -r '^~' "$HOME")
    printf "\n"
    if test -d $val
        la $val
    else
        set -l dir (dirname -- $val)
        if test $dir != . -a -d $dir
            la $dir
        else
            la
        end
    end

    string repeat -N \n --count=(math (count (fish_prompt)) - 1)

    commandline -f repaint
end
