-------------------
---- AUTOSTART ----
-------------------

hl.on("hyprland.start", function () 
  hl.exec_cmd("nm-applet")
  hl.exec_cmd("waybar & hyprpaper & awww-daemon & swaync")
  hl.exec_once("hyprctl setcursor Bibata-Modern-Classic 20")
end)
