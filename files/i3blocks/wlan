#!/usr/bin/env bash
#
# i3blocks blocklet script to display wifi signal in dBm and IP address, if WIFI is available

# try to detect interface name

if [[ -z "$IFACE" ]] ; then
    if  ( ip a s dev wlp3s0 ) > /dev/null 2>& 1 ; then
        IFACE="wlp3s0"
    elif ( ip a s dev wlan0 ) > /dev/null 2>& 1 ; then
        IFACE="wlan0"
    else
        # No wlan interface found
        exit 0
    fi
fi

USE_PERCENT=${USE_PERCENT:-0}

IW=$(which iw || echo "/sbin/iw")

if [[ ! -x $IW ]]; then
	echo "No iw binary was found on the system." 1>2
	exit 1
fi

while getopts p opt; do
    case "$opt" in
        p) USE_PERCENT=1 ;;
    esac
done

if ( ip a s dev $IFACE | grep "state DOWN" ) > /dev/null 2>& 1 ; then
    echo "📶 DOWN"
fi

dbm=$($IW dev "$IFACE" link | grep 'dBm$' | grep -Eoe '-[0-9]{2}')
ssid=$($IW dev "$IFACE" link | grep 'SSID' | cut -d ':' -f2 | sed "s/\ //g")
ipv4=$(ip -o -4 addr list "$IFACE" | awk '{print $4}')
ipv6=$(ip -o -6 addr list "$IFACE" | awk '{print $4}')

[[ -n "$dbm" ]] || exit 1
[[ -n "$ssid" ]] || exit 1

if [[ $USE_PERCENT -eq 0 ]]; then
    echo "📶($ssid) $dbm"dBm
    echo "📶($ssid) $dbm"dBm
else
    if [[ "$dbm" -le -100 ]]; then
        quality=0
    elif [[ $dbm -ge -50 ]]; then
        quality=100
    else
        quality=$((2 * (dbm + 100)))
    fi
    echo "📶($ssid) $quality%"
    echo "📶($ssid) $quality%"
fi

if [[ $dbm -ge -55 ]]; then
	echo "#00FF00"
elif [[ $dbm -ge -60 ]]; then
	echo "#CCFF00"
elif [[ $dbm -ge -70 ]]; then
	echo "#FFFF00"
elif [[ $dbm -ge -80 ]]; then
	echo "#FFAA00"
else
	echo "#FF0000"
fi
