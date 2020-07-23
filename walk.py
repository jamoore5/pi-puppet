from puppet import Puppet

def play(p, recording):
    for move in recording:
        print(move)
        p.move(move)

p = Puppet()
recording = [[155, 85, 80, 30], [155, 90, 80, 40], [155, 95, 80, 55], [155, 100, 80, 65], [155, 105, 80, 75], [155, 100, 80, 65], [155, 95, 80, 50], [155, 90, 80, 40], [155, 85, 80, 30], [145, 85, 75, 30], [135, 85, 70, 30], [120, 85, 65, 30], [110, 85, 60, 30], [100, 85, 55, 30], [110, 85, 60, 30], [125, 85, 65, 30], [135, 85, 70, 30], [145, 85, 75, 30], [155, 85, 80, 30]]

print("Start Walking...")
try:
    while True:
        play(p, recording)
finally:
    p.close()
    print("...Goodbye")

