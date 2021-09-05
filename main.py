def Establecer():
    global t1, t2, t3, promedio
    t1 = input.temperature()
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    basic.pause(5000)
    t2 = input.temperature()
    music.play_tone(880, music.beat(BeatFraction.SIXTEENTH))
    basic.pause(5000)
    t3 = input.temperature()
    music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
    promedio = (t1 + t2 + t3) / 3

def on_button_pressed_a():
    Establecer()
    if promedio > 30:
        music.play_tone(523, music.beat(BeatFraction.DOUBLE))
        music.play_tone(131, music.beat(BeatFraction.DOUBLE))
    else:
        music.play_tone(523, music.beat(BeatFraction.QUARTER))
        basic.pause(200)
        music.play_tone(523, music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Establecer()
    if promedio > 30:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
    basic.pause(5000)
input.on_button_pressed(Button.B, on_button_pressed_b)

t3 = 0
t2 = 0
t1 = 0
promedio = 0
promedio = 0
t1 = 0
t2 = 0
t3 = 0

def on_forever():
    pass
basic.forever(on_forever)
