

def draw_stairs(n):
    str = ""
    for i in range(n):
        space = " " * i
        str += space + "I\n"
    return str.strip()

print(draw_stairs(3), '''I\n I\n  I''')
print(draw_stairs(5), '''I\n I\n  I\n   I\n    I''')