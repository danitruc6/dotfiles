# dotfiles
These is my basic info to get started with any Arch distribution

## Nvim
Install all of these dependencies taken from [here](https://github.com/antoniosarosi/dotfiles/tree/master/.config/nvim)
  
```bash
# Vim-plug
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# Some runtimes are needed, install only those you don't have
sudo pacman -S nodejs npm python python-pip ruby rubygems

# Download neovim packages
pip install neovim
gem install neovim
sudo npm i -g neovim

# Some other dependencies
sudo pacman -S xsel fzf ripgrep fd the_silver_searcher prettier
yay -S universal-ctags-git
```

Then execute ```:PlugInstall``` inside neovim and it should be ready.

## Vscode

Copy ```settings.json``` and ```keybindings.json``` from my
[gist](https://gist.github.com/antoniosarosi/eb8d73a580eaa3e7dc32b0b803b4654d).
and then install the 
[Which Key](https://marketplace.visualstudio.com/items?itemName=VSpaceCode.whichkey)
and
[Neovim](https://marketplace.visualstudio.com/items?itemName=asvetliakov.vscode-neovim)
extensions.

This are some keybingins besides default ones:

| Key                    | Action                                 |
| ---------------------- | -------------------------------------- |
| **jk** or **kj**       | Go to normal mode (from insert)        |
| **alt + [hjkl]**       | Resize split                           |
| **control + [hjkl]**   | Navigate splits                        |
| **control + s**        | Save                                   |
| **control + q**        | Save and quit                          |
| **tab**                | Next buffer                            |
| **shift + tab**        | Previous buffer                        |
| **control + b**        | Close buffer                           |
| **shift + <** or **>** | Indent one level or remove it (visual) |
| **shift + k** or **j** | Move selected line down or up (visual) |

***Plugin keybindings***:

| Key           | Action                                        |
| ------------- | --------------------------------------------- |
| **space + f** | Fuzzy search                                  |
| **space + /** | Comment selected line or block                |
| **space + n** | Toggle NerdTree                               |
| **space + p** | Format document with prettier                 |
| **shift + k** | Function or class documentation and arg types |

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


