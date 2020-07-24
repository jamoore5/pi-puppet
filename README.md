# Pi Puppet

I bought the Puppet Kit for Raspberry Pi from Monk Makes to try a more hands on project with the raspberry pi. 

The kit started off on the wrong foot with the software in the tutorial no longer being supported and would not install on my pi. Thankfully I am more confident in the software side than the electronic side. The out-of-date software pointed me to GPIO Zero’s AngularServo. After looking over the documentation, I tried to implement something to test the puppet, and realized two of the servos are backwards. I tried writing code the handled the angles, so that 90 was up for all the servos. Then I looked at the documentation again and found they already had the logic to handle this situation. 

Trying to test some scripts from the original tutorial, I found their logic used 0 and 180 not -90 and 90, so I wrote a Servo class to adapt AngularServo to accept these angles. 

I wrote a Puppet class to make it easier to repeat current actions with the puppet in multiple scripts for playing with the puppet. 

After I implemented walk and wave, I wanted to do something a little more challenging. Someone suggested if I could make the puppet dance to music, it would impress them. I accepted the challenge and started trying to figure out how to do it. Here is my result.

