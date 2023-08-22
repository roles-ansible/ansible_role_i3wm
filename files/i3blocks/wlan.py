#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import subprocess
import sys
import argparse

def find_interface(interfaces):
    for iface in interfaces:
        if os.path.exists(f"/sys/class/net/{iface}"):
            return iface
    return None

def get_signal_quality(interface):
    try:
        iw_output = subprocess.check_output(["/sbin/iw", "dev", interface, "link"], text=True)
        signal_match = re.search(r'(\-\d{2}) dBm', iw_output)
        return int(signal_match.group(1)) if signal_match else None
    except subprocess.CalledProcessError:
        return None

def get_ssid(interface):
    try:
        iw_output = subprocess.check_output(["/sbin/iw", "dev", interface, "link"], text=True)
        ssid_match = re.search(r'SSID: (.+)', iw_output)
        return ssid_match.group(1).encode("utf-8").decode("unicode-escape") if ssid_match else None
    except subprocess.CalledProcessError:
        return None

def print_color(quality):
    if quality >= 70:
        print("#00FF00")
    elif quality >= 50:
        print("#CCFF00")
    elif quality >= 30:
        print("#FFFF00")
    elif quality >= 10:
        print("#FFAA00")
    else:
        print("#FF0000")

def main():
    interfaces = ["wlp3s0", "wlan0"]
    parser = argparse.ArgumentParser(description="Display WiFi signal strength and SSID")
    parser.add_argument("--interface", help="Specify the wireless interface")
    args = parser.parse_args()

    if args.interface:
        interface = args.interface
    else:
        interface = find_interface(interfaces)

    if not interface:
        sys.exit(0)

    signal_quality = get_signal_quality(interface)
    ssid = get_ssid(interface)

    if signal_quality is None:
        sys.exit(1)

    # quality = int((signal_quality / 70) * 100)  # Adjust the calculation as needed
    quality = int(signal_quality)  # Adjust the calculation as needed

    emoji_signal = "📶"

    if ssid:
        print(f"{emoji_signal} {ssid} {quality}dBm")
    else:
        print(f"{emoji_signal} {quality}dBm")

    print_color(quality)

if __name__ == "__main__":
    main()

