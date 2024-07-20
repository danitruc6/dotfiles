# dotfiles
These is my basic info to get started with any Arch distribution

## Nvim
Use and install [Lazyvim](http://www.lazyvim.org/)

In order to disable the autocomment behaviour of LazyNvim, run this line inside neovim
`:set formatoptions-=cro`

## Baisc packages
sudo pacman -S git python-pip nvim neofetch firefox alacritty exa 
 
## Nerd fonts
 
## Trackpad Natural Scrolling
 
use xinput

1. xinput list : to list the devices

```
   ~ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Synaptics TM3381-002                    	id=12	[slave  pointer  (2)]
⎜   ↳ TPPS/2 Elan TrackPoint                  	id=13	[slave  pointer  (2)]
⎜   ↳ Corne Keyboard                          	id=14	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Video Bus                               	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ Integrated Camera: Integrated C         	id=9	[slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard            	id=10	[slave  keyboard (3)]
    ↳ ThinkPad Extra Buttons                  	id=11	[slave  keyboard (3)]
    ↳ Corne Keyboard                          	id=15	[slave  keyboard (3)]
```

2. Then copy the ID of mouse(or touchpad if on laptop)

3. Use the following command: xinput list-props {ID}, to get the list of properties

```
   ~ xinput list-props 12
Device 'Synaptics TM3381-002':
	Device Enabled (185):	1
	Coordinate Transformation Matrix (187):	1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
	libinput Tapping Enabled (444):	1
	libinput Tapping Enabled Default (445):	0
...
	libinput Natural Scrolling Enabled (452):	1
	libinput Natural Scrolling Enabled Default (453):	0
	libinput Disable While Typing Enabled (454):	1
	libinput Disable While Typing Enabled Default (455):	1
...
```
4. Look for the Natural Scrolling prop ID.

5.Then use xinput set-prop {ID} {Property-ID} 1 ('1' means enable)
```
input set-prop 12 452 1
```

## ZSH config
Uselful plugings taken from [here](https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df):
## Install plugins.
 - autosuggesions plugin
 
	`git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions`
	
 - zsh-syntax-highlighting plugin
 
	`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting`
	
 - zsh-fast-syntax-highlighting plugin
 
	`git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting`
	
 - zsh-autocomplete plugin
	
	`git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete`
	
## Enable plugins by adding them to .zshrc.
 - Open .zshrc
	
	`nvim ~/.zshrc`
	
 -  Find the line which says `plugins=(git)`.
	
 -  Replace that line with
	`plugins=(git zsh-autosuggestions zsh-syntax-highlighting fast-syntax-highlighting zsh-autocomplete)`
- You can omit the zsh-autocomplete, since it's kind of weird how it works

## Keyboard backlight settings
Check max brightness
`cat /sys/class/leds/tpacpi::kbd_backlight/max_brightness`

Change level of bightness
`echo 1 > /sys/class/leds/tpacpi::kbd_backlight/brightness`

install ` sudo pacman -S brightnessctl` for a tool to control it:

info of available controls `brightnessctl --device='tpacpi::kbd_backlight' info`

how to change it: `brightnessctl --device='tpacpi::kbd_backlight' set 1`	


## Change keyboard layout using setxkbmap
You can change the layout using Alt+Shift with the following terminal command:

```
setxkbmap -layout "us,latam" -option "grp:alt_shift_toggle" &
```
However this is not permanent.

In Openbox, add the command to this file and logout and re-login to work.
```
~/.config/openbox/autostart
```
For BSPWM just add the line to the bspwmrc file.

Or an easiest way using the same windows hotkey Super(Windows) + Space, is to add it to the bspwm/sxhkdrc like this:
```
# Change keyboard language
super + space
  {setxkbmap se, setxkbmap us}
```
### Showing keyboard layout in polybar
Use the polybar [Module: xkeyboard](https://github.com/polybar/polybar/wiki/Module:-xkeyboard), add the module to the modules.ini, and then add the module to the config.init, like this:
```
modules-left = ... xkeyboard ...
```
## Loging to github using ssh
Follow this [guide](https://www.geeksforgeeks.org/using-github-with-ssh-secure-shell/)

## How to change shell to Fish (for Macos)

As per this (guide)[https://stackoverflow.com/questions/66724016/my-fish-is-blind-fish-does-not-recognise-any-commands-after-setting-it-as-defa]

```
$ brew install fish ​
$ fish
$ fish_add_path /opt/homebrew/bin
$ echo "/opt/homebrew/bin/fish" | sudo tee -a /etc/shells
$ chsh -s /opt/homebrew/bin/fish
```
