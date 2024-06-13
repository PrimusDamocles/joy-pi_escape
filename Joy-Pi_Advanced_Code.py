# -*- coding: iso-8859-1 -*-
# Required modules are imported and set up
import RPi.GPIO as GPIO
import time

# set up GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup pin for the buzzer
buzzer_pin = 4
GPIO.setup(buzzer_pin, GPIO.OUT)

# dictionary to convert notes to frequencies
read_notes = {
  '' : 0,
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}

def buzz(freq, tempo, speed):
    """
    method to play a note
    freq - frequency to modulate the note
    tempo - timings of the note
    speed - time of the song
    """
    # do a pause
    if freq == 0: time.sleep(tempo / speed)
    else:
        # set up modulation of note
        modulation = 1 / (freq * 2 )
        iterations = int(tempo * freq)
        # playing the note
        for i in range(iterations):
           GPIO.output(buzzer_pin, True)
           time.sleep(modulation)
           GPIO.output(buzzer_pin, False)
           time.sleep(modulation)

def play(notes, timings, music_time, speed = 1, rep = 1):
    """
    method to play song
    notes - array of the notes of the song
    timings - timings of every note of the song
    music_time - time of the song
    speed (default 1) - to slow the song down (0-1) or to speed up (> 1)
    rep (default 1) - how many repetitions will be played
    """
    # for loop for repetitions
    for i in range(rep):
        # for loop for each note of the song
        for i in range(len(notes)):
            # use the method buzz to play note
            buzz(read_notes[notes[i]], (timings[i] / music_time) * 1/speed, music_time)
            # stop to accentuate a single note
            time.sleep(0.05)

# Play Cantina Band
print("Cantina Band - John Williams")
# define notes into array
cantina_band_notes = [
    'B4', 'B4', 'B4', 'B4', 'F4', 'B4', 'B4', 'B4', 'B4', 'F4', 'B4', 'B4', 'B4', 'B4', 'F4',
    'A4', 'A4', 'A4', 'A4', 'F4', 'A4', 'A4', 'A4', 'A4', 'F4', 'A4', 'A4', 'A4', 'A4', 'F4',
    'G4', 'G4', 'G4', 'G4', 'F4', 'G4', 'G4', 'G4', 'G4', 'F4', 'G4', 'G4', 'G4', 'G4', 'F4',
    'A4', 'A4', 'A4', 'A4', 'F4', 'A4', 'A4', 'A4', 'A4', 'F4', 'A4', 'A4', 'A4', 'A4', 'F4'
]
# define timings for the notes into an array
cantina_band_timings = [
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4
]
# define time of the song
cantina_band_time = 4
# run the method play with defined variables
play(cantina_band_notes, cantina_band_timings, cantina_band_time, speed = 1, rep = 1)

# cleans up after program is finished
GPIO.cleanup()
