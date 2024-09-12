def Volume_of_Cuboid(L: number, B: number, H: number):
    global Volume
    Volume = L * (B * H)
    game.splash("Volume of cuboid =", Volume)
    return Volume
Volume = 0
Volume = 0
Volume_of_Cuboid(4, 2, 4)