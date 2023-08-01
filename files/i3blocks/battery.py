#!/usr/bin/env python3
"""
battery for i3blocks
"""

import subprocess
import sys

def get_battery_info():
    status = subprocess.check_output(['acpi'], universal_newlines=True)

    if not status:
        # -> keine Batterie gefunden
        text_output = "<span color='red'><span font='FontAwesome'>\uf00d \uf240</span></span>"
        battery_percent = 100
    else:
        # -> auswertung der batteriedaten
        batteries = status.strip().split("\n")
        state_batteries = []
        battery_percent_batteries = []

        for battery in batteries:
            if battery:
                state_batteries.append(battery.split(": ")[1].split(", ")[0])
                commasplitstatus = battery.split(", ")
                battery_percent_batteries.append(int(commasplitstatus[1].rstrip("%\n")))

        state = state_batteries[0]
        battery_percent = int(sum(battery_percent_batteries) / len(battery_percent_batteries))

        # stands for charging
        fa_lightning = "<span color='yellow'><span font='FontAwesome'>\uf0e7</span></span>"

        # stands for plugged in
        fa_plug = "<span font='FontAwesome'>\uf1e6</span>"

        text_output = ""
        battery_remaining_time = ""

        if state == "Discharging":
            battery_time = batteries[0].split()[-2]
            battery_remaining_time = f" ({battery_time})"
        elif state == "Full":
            text_output = fa_plug + " "
        elif state == "Unknown":
            text_output = "<span font='FontAwesome'>\uf128</span> "
        else:
            text_output = fa_lightning + " " + fa_plug + " "

        def get_color(percent):
            """
            -> color based on battery state
            """
            color_mapping = {
                16: "#FFFFFF",
                24: "#FF3300",
                32: "#FF6600",
                40: "#FF9900",
                50: "#FFCC00",
                60: "#FFFF00",
                70: "#FFFF33",
                80: "#FFFF66"
            }

            for threshold, color_code in color_mapping.items():
                if percent < threshold:
                    return color_code

            return "#FFFFFF"

        battery_form_string = '<span color="{}">{}%</span>'
        text_output += battery_form_string.format(get_color(battery_percent), battery_percent)
        text_output += battery_remaining_time

    return text_output

if __name__ == "__main__":
    text_output = get_battery_info()
    print(text_output)
    print(text_output)

    if "battery_percent" in locals() and battery_percent < 16:
        sys.exit(33)

