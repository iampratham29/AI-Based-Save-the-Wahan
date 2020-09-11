import game.ek as g
g.commence()
if g.mode == 1:
    bgimage = g.bgImg
    vehicleimg = g.car2Img

if g.mode == 2:
    bgimage = g.bgbtImg
    vehicleimg = g.boat2Img

if g.mode == 3:
    bgimage = g.bgspImg
    vehicleimg = g.sp2Img
g.gameloop(bgimage=bgimage, vehicleimg=vehicleimg)
