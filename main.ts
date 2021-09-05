function Establecer () {
    t1 = input.temperature()
    music.playTone(784, music.beat(BeatFraction.Sixteenth))
    basic.pause(5000)
    t2 = input.temperature()
    music.playTone(880, music.beat(BeatFraction.Sixteenth))
    basic.pause(5000)
    t3 = input.temperature()
    music.playTone(988, music.beat(BeatFraction.Sixteenth))
    promedio = (t1 + t2 + t3) / 3
}
input.onButtonPressed(Button.A, function () {
    Establecer()
    if (promedio > 30) {
        music.playTone(523, music.beat(BeatFraction.Double))
        music.playTone(131, music.beat(BeatFraction.Double))
    } else {
        music.playTone(523, music.beat(BeatFraction.Quarter))
        basic.pause(200)
        music.playTone(523, music.beat(BeatFraction.Quarter))
    }
})
input.onButtonPressed(Button.B, function () {
    Establecer()
    if (promedio > 30) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(5000)
})
let t3 = 0
let t2 = 0
let t1 = 0
let promedio = 0
basic.showString("Profejavierc")
promedio = 0
t1 = 0
t2 = 0
t3 = 0
basic.forever(function () {
	
})
