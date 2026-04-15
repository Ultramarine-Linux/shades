# SPDX-FileCopyrightText: 2025 Its-J
#
# SPDX-License-Identifier: GPL-3.0-or-later

#!/usr/bin/env bash

choice=$(printf " Logout\n Shutdown\n Reboot\n Suspend\n Cancel" | rofi -dmenu -l 5)
elif [[ $choice == " Logout" ]];then
    swaymsg exit
elif [[ $choice == " Shutdown" ]];then
    systemctl poweroff
elif [[ $choice == " Reboot" ]];then
    systemctl reboot --now
elif [[ $choice == " Suspend" ]];then
    systemctl suspend
elif [[ $choice == " Cancel" ]];then
    exit
fi
