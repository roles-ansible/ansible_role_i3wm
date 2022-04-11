 I3 Window Manager - ansible role
=========================================

Install and deploy a basic configuration of [I3 Window Manager](https://i3wm.org/) via ansible.<br/>
Optionally configure your resolution, which applications will be bound to which screen and what will be included in the autostart.<br/>
If you want to use wayland instead of xorg, think about using [sway](https://swaywm.org/) as window manager. The corresponding ansible is located on [github.com/roles-ansible/role-sway](https://github.com/roles-ansible/role-sway.git).

[![MIT License](https://raw.githubusercontent.com/chaos-bodensee/role-i3wm/master/.github/license.svg?sanitize=true)](https://github.com/chaos-bodensee/role-i3wm/blob/master/LICENSE)
[![MIT License](https://raw.githubusercontent.com/chaos-bodensee/role-i3wm/master/.github/galaxy.svg?sanitize=true)](https://galaxy.ansible.com/do1jlr/i3wm)

### Get it directly from Ansible Galaxy
```bash
$ ansible-galaxy install do1jlr.i3wm
```

 Role Variables
--------------

For a good overview about possible variables, please have a look into ``defaults/main.yml``.

 Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - name: install i3wm on localhost
      hosts: localhost
      vars_files:
        - vars/main.yml
      roles:
        - {role: do1jlr.i3wm, tags[i3,i3wm]}
```
*`vars/main.yml`*

```yaml
    # background image
    i3_desktop_background: "~/Bilder/wallpaper.jpg"

    # you want additional keybindings?
    i3_keybindings_extra:
      - keybinding:
        name: Volume (mute/unmute)
        key: $mod+F12
        exec: --no-startup-id amixer sset Master toggle
      - keybinding:
        name: Volue (default)
        key: $mod+Shift+F12
        exec: --no-startup-id amixer sset Master 40%

    # how your monitors are configured
    i3_monitors:
      - monitor:
        id: 1
        output: "HDMI-A-0"
        mode: "1920x1080"
        pos: "0x0"
        rotate: "normal"
        workspaces: [0,1,2,3,4,5,6]
      - monitor:
        id: 2
        output: "DisplayPort-0"
        mode: "1920x1080"
        pos: "1920x0"
        rotate: "normal"
        workspaces: [7,8,9]

    # startup applications
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

    # lock your screen after 3 hours
    enable_lock_after_time: true
```
