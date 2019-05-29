 I3 Window Manager - ansible role
=========================================

*Install and deploy a basic configuration of [I3 Window Manager](https://i3wm.org/) via ansible.*

[![Build Status](https://travis-ci.org/DO1JLR/ansible-role-i3wm.svg?branch=master)](https://travis-ci.org/DO1JLR/ansible-role-i3wm) 

<a href="https://galaxy.ansible.com/do1jlr/ansible_role_i3wm"><img width="80px" src="https://galaxy.ansible.com/assets/galaxy-logo-02.svg"/></a>

### Get it directly from Ansible Galaxy 
```bash
$ ansible-galaxy install do1jlr.ansible_role_i3wm
```

 Requirements
------------

No requirements.

 Role Variables
--------------

For a good overview about possible variables, please have a look into ``defaults/main.yml``.

 Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```bash
    - hosts: all
      vars_files:
        - vars/main.yml    
      roles:
        - { role: i3 }
```
*`vars/main.yml`*

```bash
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

```
