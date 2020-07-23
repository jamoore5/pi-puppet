from puppet import Puppet

def play(p, recording):
    for move in recording:
        print(move)
        p.move(move)

p = Puppet()
recording = []

while True:
    play(p, recording)

