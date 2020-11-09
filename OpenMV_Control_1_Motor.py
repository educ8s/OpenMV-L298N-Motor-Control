import pyb

def stopMotor():
    in1.value(0)
    in2.value(0)

timer = pyb.Timer(4, freq=1000)
ena = timer.channel(1, pyb.Timer.PWM, pin=pyb.Pin('P7'))
in1 = pyb.Pin('P1', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
in2 = pyb.Pin('P2', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)

in1.value(1)
in2.value(0)
ena.pulse_width_percent(100)
pyb.delay(2000)

stopMotor()
pyb.delay(2000)

in1.value(0)
in2.value(1)
pyb.delay(2000)

stopMotor()
pyb.delay(2000)

in1.value(1)
in2.value(0)
ena.pulse_width_percent(50)
pyb.delay(2000)

stopMotor()
pyb.delay(2000)

in1.value(0)
in2.value(1)
ena.pulse_width_percent(50)
pyb.delay(2000)

stopMotor()
