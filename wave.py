from puppet import Puppet

def play(p, recording):
    for move in recording:
        print(move)
        p.move(move, 0.025)

p = Puppet()
recording = [[150, 85, 85, 10], [145, 85, 85, 10], [140, 85, 85, 10], [135, 85, 85, 10], [130, 85, 85, 10], [125, 85, 85, 10], [120, 85, 85, 10], [115, 85, 85, 10], [110, 85, 85, 10], [105, 85, 85, 10], [100, 85, 85, 10], [95, 85, 85, 10], [90, 85, 85, 10], [85, 85, 85, 10], [80, 85, 85, 10], [75, 85, 85, 10], [70, 85, 85, 10], [70, 85, 85, 10], [75, 85, 85, 10], [80, 85, 85, 10], [85, 85, 85, 10], [90, 85, 85, 10], [85, 85, 85, 10], [80, 85, 85, 10], [75, 85, 85, 10], [70, 85, 85, 10], [75, 85, 85, 10], [80, 85, 85, 10], [85, 85, 85, 10], [90, 85, 85, 10], [95, 85, 85, 10], [100, 85, 85, 10], [105, 85, 85, 10], [110, 85, 85, 10], [115, 85, 85, 10], [120, 85, 85, 10], [125, 85, 85, 10]]

print("Start Wave...")
try:
    for i in range(3):
        play(p, recording)
finally:
    p.close()
    print("...Goodbye")
