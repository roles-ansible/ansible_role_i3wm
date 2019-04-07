I3 WM
=====

Install and a basic configuration of I3 Window Manager
See: https://i3wm.org/

[![Build Status](https://travis-ci.org/DO1JLR/ansible-role-i3wm.svg?branch=master)](https://travis-ci.org/DO1JLR/ansible-role-i3wm)

Requirements
------------

No requirements.

Role Variables
--------------

*additional i3 packages*

    i3_packages_extra:

*background image*

    i3_desktop_env:

*i3 workspaces*

`__i3_workspaces` could be overwritte with `i3_workspaces`

*i3 keybindings*

`__i3_keybindings` coud be overwritten with `i3_keybindings`

*additional i3 keybindings*

    i3_keybindings_extra: []

*monitor settings and bindings to i3 workspaces*

    i3_monitors: []

*applications bindings to i3 workspaces*

    i3_applications: []

*ansible user*
i3wm_user: "{{ user }}"

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      vars_files:
        - vars/main.yml    
      roles:
        - { role: i3 }

*`vars/main.yml`*

    i3_desktop_env:
      background: "~/wallpaper.jpg"

    i3_packages_extra:
      - ranger

    i3_keybindings_extra:
      - keybinding:
        name: Volume (mute/unmute)
        key: $mod+F12
        exec: --no-startup-id amixer sset Master toggle
      - keybinding:
        name: Volue (default)
        key: $mod+Shift+F12
        exec: --no-startup-id amixer sset Master 40%

    i3_monitors:
      - monitor:
        id: 1
        output: "VGA-1"
        mode: "1920x1080"
        pos: "0x0"
        rotate: "normal"
        workspaces: [1,2,3,4,5,6]
      - monitor:
        id: 2
        output: "HDMI-1"
        mode: "1920x1080"
        pos: "1920x0"
        rotate: "normal"
        workspaces: [7,8,9,0]

    i3_applications:
      - application:
        class: "Firefox"
        name: "firefox"
        workspace: 1
        on_startup: false
      - application:
        class: "Code"
        name: "code"
        workspace: 7
        on_startup: true

License
-------

Apache
