
# IMPORTS
import os
import re
import subprocess
from typing import List  # noqa: F401
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.battery import Battery, BatteryState
from libqtile.widget.volume import Volume

#Dracula color theme
theme = {"background": "#282a36",
        "current": "#44475a",
        "selection": "#44475a",
        "foreground": "#f8f8f2",
        "comment": "#6272a4",
        "cyan": "#8be9fd",
        "green": "#50fa7b",
        "orange": "#ffb86c",
        "pink": "#ff79c6",
        "purple": "#bd93f9",
        "red": "#ff5555",
        "yellow": "#f1fa8c"}


theme2 = {
    "dark": [
        "#0f101a",
        "#0f101a"
    ],
    "grey": [
        "#353c4a",
        "#353c4a"
    ],
    "light": [
        "#f1ffff",
        "#f1ffff"
    ],
    "text": [
        "#0f101a",
        "#0f101a"
    ],
    "focus": [
        "#a151d3",
        "#a151d3"
    ],
    "active": [
        "#f1ffff",
        "#f1ffff"
    ],
    "inactive": [
        "#4c566a",
        "#4c566a"
    ],
    "urgent": [
        "#F07178",
        "#F07178"
    ],
    "color1": [
        "#a151d3",
        "#a151d3"
    ],
    "color2": [
        "#F07178",
        "#F07178"
    ],
    "color3": [
        "#fb9f7f",
        "#fb9f7f"
    ],
    "color4": [
        "#ffd47e",
        "#ffd47e"
    ]
}


#Variables/Programs
mod = "mod1"                        # Sets mod key to SUPER
home = os.path.expanduser('~')      # Allow using 'home +' to expand ~
myTerm = "alacritty"                # Default Terminal application
myBrowser = "google-chrome-stable"                  # Web browser
myFilemgr = "thunar"               # File Manager
myEditor = "code"                  # Text editor
myAppLauncher = "rofi -show drun -theme '~/.config/rofi/config.rasi'"

# Keybindings
keys = [
	### Essentials/launching apps
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc="Launches My Terminal"
        ),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc="Launches My Web Browser"
        ),
    Key([mod], "e",
        lazy.spawn(myFilemgr),
        desc="Launches My File Manager"
        ),
    Key([mod], "a",
        lazy.spawn(myEditor),
        desc="Launches Text Editor"
        ),
    Key([mod], "Escape",
        lazy.spawn([home + '/.config/rofi/scripts/powermenu.sh'])
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    Key([mod], "d",
        lazy.spawn(myAppLauncher),
        desc="Application Launcher"
        ),
    Key([mod], "r",
    	lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
        ),
    # Qtile/layout commands
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
        ),
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
    # Moving windows.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    Key([mod, "shift"], "k",
    	lazy.layout.shuffle_down(),
    	desc="Move window down"
    	),
    # Window changing commands
    Key([mod, "control"], "h",
    	lazy.layout.shrink(),
        desc="Shrink window"
        ),
    Key([mod, "control"], "l",
    	lazy.layout.grow(),
        desc="Grow window"
        ),
    Key([mod], "n",
    	lazy.layout.normalize(),
    	desc="Reset all window sizes"
    	),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    ## Function keys
    # Screen Brightness
    Key([], 'XF86MonBrightnessUp',
    	#lazy.spawn('xbacklight -inc 10')
    	lazy.spawn("brightnessctl set +10%")
    	),
    Key([], 'XF86MonBrightnessDown',
    	#lazy.spawn('xbacklight -dec 10')
    	lazy.spawn("brightnessctl set 10%-")
    	),
    # Audio/Volume
    Key([], 'XF86AudioMute',
    	#lazy.spawn('amixer -q set Master toggle')
    	lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    	),
    Key([], 'XF86AudioRaiseVolume',
    	lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    	),
    Key([], 'XF86AudioLowerVolume',
    	lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    	),
    #Screenshots
   # Key(["mod4"], 'space',
   # 	lazy.spawn("setxkbmap -layout us,es")
   # 	),
    Key(["mod4", "shift"], 's',
        lazy.spawn("scrot -s -e 'mv $f ~/Pictures/Screenshot 2>/dev/null'"))
]



# Remove portions of windows name
def parse_func(text):
	for string in [" - google-chrome-stable", " - gedit", " - Visual Studio Code"]:
		text = text.replace(string, "")
	return text


# Groups using Names istead of numbers
# See https://docs.qtile.org/en/stable/manual/config/groups.html
groups = [Group(""),
          Group("爵"),
          Group(""),
          Group(""),
          Group(""),
          Group("碌", layout='treetab'),
          Group("", layout='floating')]
# allow [S]mod4+1 through [S]mod4+0 to bind to groups; if you bind your groups by hand in your config, you don't need to do this.
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")


#Used layouts
layouts = [
    layout.MonadTall(
        border_width = 2,
        border_focus = theme["purple"],
        border_normal = theme["background"],
        margin = 4,
        ),
    layout.Max(),
	layout.Floating(
        border_width = 2,
        border_focus = theme["purple"],
        border_normal = theme["background"],
        ),
	layout.TreeTab(
		font = "Hack",
		fontsize = 20,
		border_width = 2,
		sections = [''],
		bg_color = theme["background"],
		active_bg = theme["current"],
		active_fg = theme["purple"],
		inactive_bg = theme["background"],
		inactive_fg = theme["foreground"],
		urgent_bg = theme["background"],
		urgent_fg = theme["red"],
		panel_width = 185,
		),
]

# Widget default settings
widget_defaults = dict(
    font = 'mononoki Nerd Font Mono',
    fontsize = 20,
    padding = 2,
    background = theme["background"],
)
extension_defaults = widget_defaults.copy()
#adding powerline
def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=55 ,
        padding=-10
    )
def base(fg, bg): 
    return {
        'foreground': fg,
        'background': bg
    }


#Setup bar
screens = [
    Screen(
        top=bar.Bar(
            [
				widget.CurrentLayoutIcon(
					custom_icon_paths = [(home + "/.config/qtile/icons")],
					foreground = theme["foreground"],
					scale = 0.8,
					),
				widget.GroupBox(
                    active = theme["green"],
                    background = theme["background"],
                    block_highlight_text_color = theme["purple"],
                    disable_drag = True,
                    foreground = theme["foreground"],
                    fontsize = 32,
                    highlight_color = theme["selection"],
                    highlight_method = "line",
                    inactive = theme["foreground"],
                    urgent_border = theme["red"],
                    ),
                widget.Prompt(
                	prompt = 'Run: ',
                	padding = 5,
                	foreground = theme["purple"],
                    bell_style = 'visual',
                    visual_bell_color = theme["red"],
                    ignore_dups_history = True,
                	),
                widget.WindowName(
                	format = '{name}',
                    empty_group_string = "Truc's Qtile Arch BTW",
                	foreground = theme["foreground"],
                	parse_text = parse_func,
                	),
                powerline(theme2["color4"],theme["background"]),
				widget.CheckUpdates(
                    update_interval = 300,
                    distro = "Arch_checkupdates",
                    display_format = " {updates} ",
                    no_update_string = "0",
                    mouse_callbacks = {'Button1': lazy.spawn(myTerm + ' -e yay -Syu')},
                    foreground = theme2["dark"],
                    colour_no_updates = theme2["dark"],
                    colour_have_updates = theme2["dark"],
                    background = theme2["color4"],
                    ),


                widget.NetGraph(
                	#format = '{total}',
                    interface = "eno1",
                    #format = '{down} ↓↑ {up}',
                    foreground = theme2["dark"],
                    background = theme2["color4"],
                	#mouse_callbacks = {'Button1': lazy.spawn('nm-connection-editor')},
                	),
                powerline(theme2["color3"],theme2["color4"]),
                widget.CPU(
                	background = theme2["color3"],
                    foreground = theme2["dark"],
                	fmt = '{}',
                    format = '💻{load_percent} ',
                	),
              	widget.ThermalSensor(
                    threshold = 70,
                    tag_sensor = "Core 0",
                    foreground_alert = theme["red"],
                    foreground = theme2["dark"],
                    background = theme2["color3"],
                    fmt = '{}',
                    ),
                powerline(theme2["color2"],theme2["color3"]),
                widget.TextBox(                    foreground = theme2["dark"],
                    background = theme2["color2"],
                    text = '',
                ),
                widget.Memory(
                    mouse_callbacks = {'Button1': lazy.spawn(myTerm + ' -e btop')},
                    background = theme2["color2"],
                    foreground = theme2["dark"],
                    fmt = '{}',
                    measure_mem = 'G',
                    format = '{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}',
                    #update_interval = '1',
                    ),
                widget.DF(
                	background = theme2["color2"],
                    foreground = theme2["dark"],
                	warn_color = theme["red"],
                	format = '  {r:.0f}',
                	partition = '/',
                	visible_on_warn = False,
                	),
                powerline(theme2["color1"],theme2["color2"]),
                widget.TextBox(                    foreground = theme2["dark"],
                    background = theme2["color1"],
                    text = '🔈',
                ),
                widget.PulseVolume(
                    foreground = theme2["dark"],
                    background = theme2["color1"],
                    #volume_app = 'pulseaudio',
                    limit_max_volume = True,
                ),
                #powerline(theme2["color1"],theme2["color2"]),
                widget.KeyboardLayout(
                    foreground = theme2["dark"],
                	background = theme2["color1"],
                    configured_keyboards = ['us','es'],
                ),
                widget.Clock(
                	format = ' %b %d %I:%M%p',
                	background = theme2["color1"],
                    foreground = theme2["dark"],
                	mouse_callbacks = {'Button1': lazy.spawn(myBrowser + ' https://calendar.google.com')},
                	),
                powerline(theme2["dark"],theme2["color1"]),
                widget.Systray(
                	icon_size = 22,
                	background = theme["background"],
                    foreground = theme["background"],
                	),
            ],
            24,
        ),
    ),
]

# Allows dragging floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

# Set floating for certain apps
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
	Match(wm_class='confirm'),
	Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='nm-connection-editor'),
    Match(wm_class='xfce4-power-manager-settings'),
    Match(wm_class='bitwarden'),
    Match(wm_class='blueman-manager'),
    Match(wm_class='Conky'),
    Match(wm_class='kdeconnect-app'),
    Match(wm_class='VirtualBox Machine'),
    Match(wm_class='lxappearance'),
    Match(wm_class='qt5ct'),
    Match(wm_class='xarchiver'),
    Match(wm_class='Clamtk'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Allows auto-minimize when losing focus for apps that need it
auto_minimize = True

# Functions for changing groups
def window_to_prev_group(qtile):
	if qtile.currentWindow is not None:
		i = qtile.groups.index(qtile.currentGroup)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

# Hooks
#Runs startup applications
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# java UI toolkits/whitelist
wmname = "LG3D"
