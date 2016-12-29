"""
This is main where i call all the different functions
in order for the whole system to work.

Below you can either just check motion and send email to yourself
or you could comment it and only use the command function so if
you send it a command to take a picture then it will take a picture for
you and send it to you.
or you could use both if you want.
"""

import emailing2
import readEmail
import picture
import P3picam

while True:
    motionState = P3picam.motion()        ## This calls the motion() from P3picam
    print('Motion detected',motionState)  ## motion() checks if motion is detected
    if motionState == True:               ## if motion is detected then it calls takepic()
        picture.takepic()                 ## from picture which takes a picture
        emailing2.send()                  ## then it sends that picture to my email
                                          ## using send() from emailing2.




    cmd = readEmail.command()                    ## this line calls the cmmand() from
    print('Listening...')                        ## readEmail and stores it in cmd
   
    if cmd[0] == 'tp' or cmd[1] == 'tp':         ## this if statement checks if the cmd
        print('Command received: take picture')  ## is equal to tp(take picture)
        emailing2.send()                         ## then send the last taken picture
        picture.takepic()                        ## then take a new picture 
        emailing2.send()                         ## and send it to my email
	
        




