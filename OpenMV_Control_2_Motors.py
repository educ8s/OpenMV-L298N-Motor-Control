import pyb

def stopMotors():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

timer = pyb.Timer(4, freq=1000)
ena = timer.channel(1, pyb.Timer.PWM, pin=pyb.Pin('P7'))
enb = timer.channel(2, pyb.Timer.PWM, pin=pyb.Pin('P8'))

in1 = pyb.Pin('P1', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
in2 = pyb.Pin('P2', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
in3 = pyb.Pin('P3', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
in4 = pyb.Pin('P4', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)

#ROTATE CLOCKWISE AT FULL SPEED
in1.value(1)
in2.value(0)
in3.value(1)
in4.value(0)
ena.pulse_width_percent(100)
enb.pulse_width_percent(100)

pyb.delay(2000)

stopMotors()
pyb.delay(2000)

#ROTATE COUNTERCLOCKWISE AT FULL SPEED
in1.value(0)
in2.value(1)
in3.value(0)
in4.value(1)
pyb.delay(2000)

stopMotors()
pyb.delay(2000)

#ROTATE CLOCKWISE AT HALF SPEED
in1.value(1)
in2.value(0)
in3.value(1)
in4.value(0)
ena.pulse_width_percent(50)
enb.pulse_width_percent(50)
pyb.delay(2000)

stopMotors()
pyb.delay(2000)

#ROTATE COUNTERCLOCKWISE AT HALF SPEED
in1.value(0)
in2.value(1)
in3.value(0)
in4.value(1)
ena.pulse_width_percent(50)
enb.pulse_width_percent(50)
pyb.delay(2000)

stopMotors()
