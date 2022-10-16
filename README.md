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
 
## Trackpad Natura Scrolling
 
use xinput

1. xinput list : to list the devices

Then copy the ID of mouse(or touchpad if on laptop)

2. xinput list-props {ID}
For examp;e:

Then use xinput set-prop
```
input set-prop 10 320 1
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
