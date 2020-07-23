import pygame
from time import sleep
from puppet import Puppet

#import librosa

#y, sr = librosa.load("clown_song.wav")
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print(beat_times)

beat_times = [ 0.37151927,  0.85913832,  1.32353741,  1.81115646,  2.29877551,  2.80961451,
  3.27401361,  3.76163265,  4.22603175,  4.71365079,  5.20126984,  5.68888889,
  6.15328798,  6.64090703,  7.12852608,  7.61614512,  8.12698413,  8.61460317,
  9.07900227,  9.56662132, 10.03102041, 10.51863946, 10.98303855, 11.4706576,
 11.93505669, 12.42267574, 12.93351474, 13.39791383, 13.88553288, 14.37315193,
 14.86077098, 15.34839002, 15.85922902, 16.34684807, 16.81124717, 17.29886621,
 17.78648526, 18.27410431, 18.7385034,  19.22612245, 19.7137415,  20.2245805,
 20.68897959, 21.17659864, 21.64099773, 22.12861678, 22.61623583, 23.08063492,
 23.54503401, 24.03265306, 24.52027211, 25.00789116, 25.47229025, 25.98312925,
 26.44752834, 26.91192744, 27.37632653, 27.88716553, 28.37478458, 28.86240363,
 29.32680272, 29.79120181, 30.27882086, 30.78965986, 31.27727891, 31.76489796,
 32.25251701, 32.74013605, 33.2277551,  33.71537415, 34.71537415, 35.71537415]

# initialize puppet
p = Puppet()


# Play wav file
pygame.mixer.init()
pygame.mixer.music.load("clown_song.wav")
pygame.mixer.music.play()


def move_to_the_beat(start_t, end_t, min, max):
    total_time = end_t - start_t
    move_time = total_time / 2
    move_num = int(move_time / 0.05) - 1
    
    d = [
            int((max[0]-min[0]) / move_num),
            int((max[1]-min[1]) / move_num),
            int((max[2]-min[2]) / move_num),
            int((max[3]-min[3]) / move_num)
        ]
    
    c = min
    p.move(c)
    
    # move to the max angle in intervals
    for i in range(move_num):
        c[0] = c[0] + d[0]
        c[1] = c[1] + d[1]
        c[2] = c[2] + d[2]
        c[3] = c[3] + d[3]
        print(c)
        p.move(c)
    sleep(move_time - int(move_time /0.05) * 0.05)
    
    # move back to the min in intervals
    for i in range(move_num):
        c[0] = c[0] - d[0]
        c[1] = c[1] - d[1]
        c[2] = c[2] - d[2]
        c[3] = c[3] - d[3]
        print(c)
        p.move(c)
    sleep(move_time - int(move_time / 0.05) * 0.05)


# dance to the beat of the music
for i in range(len(beat_times)):
    if i == 0:
        sleep(1 + beat_times[i])
    else:
        move = i % 3
        if move == 0:
            max_angle = [180, 0, 100, 0]
        elif move == 1:
            max_angle = [0, 100, 0, 180]
        else:
            max_angle = [50, 180, 180, 50]
        move_to_the_beat(beat_times[i-1], beat_times[i], [0,0,0,0], max_angle)
