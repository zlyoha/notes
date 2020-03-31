# превичная настройка ОС

# history
cat >> ~/.bashrc << 'EOF'
#add datetime to commands
export HISTTIMEFORMAT='%Y-%m-%d %H:%M:%S '
#add more commands to history
export HISTFILESIZE=100000
export HISTSIZE=100000
# Avoid duplicates
HISTCONTROL=ignoredups:erasedups
# When the shell exits, append to the history file instead of overwriting it
shopt -s histappend

# After each command, append to the history file and reread it
PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"
EOF

systemctl disable --now apt-daily{,-upgrade}.{timer,service}

sudo apt install -y vlc terminator google-chrome 

#ubuntu
gsettings set com.ubuntu.update-notifier no-show-notifications true
