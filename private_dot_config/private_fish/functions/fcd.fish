function fcd
    set -l val (fd | fzf -e  --preview 'bat --color always {}')
    if test -d $val
        if test "$val" != ""
            cd $val
        else
            cd .
        end
    else
        set -l dir (dirname -- $val)
        cd $dir
    end
    commandline -f repaint
end
