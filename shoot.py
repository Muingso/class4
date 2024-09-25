import pgzrun

TITLE= "Good Shot"

WIDTH =500
HEIGHT =500

alien= Actor('alien')

def draw():
    screen.fill(coloer=(77,77,0))
    alien.draw()

pgzrun.go()