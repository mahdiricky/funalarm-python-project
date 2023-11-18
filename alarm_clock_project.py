# randomly alarm clock project
import datetime,time,winsound

def alarm_input():
    '''
    with this function we will know the users
    input and the alarm hour 
    '''
    #we make the variables global because we need to use in other functions
    global invalid,userinput,alarmTime
    invalid=True

    while(invalid):
        print('Please Set The Valid Time (Ex. 06:30):')
        userinput=input('>> ')
        #this will be seperate the hour from the minute
        alarmTime = [int(n) for n in userinput.split(":")]
        if(alarmTime[0]>=24 or alarmTime[0]<0):
            #we should validate the hour and the minute
            invalid=True
        elif(alarmTime[1]<0 or alarmTime[1]>=60):
            invalid=True
        else:
            False
            # if it will be false the we need to break out of the loop
            break
alarm_input()

def alarm_seconds():
    '''
    after alarm input we need to have seconds because we 
    need to use it as a countdown
    '''
    global alarmTime,userinput,invalid,seconds,alarmSeconds,time_now,current_seconds,seconds_until_alarm
    # the firstone for the hour (1hour=3600seconds) the second one for minute (1minute=60seconds)
    # the next one is for second (1secnod=1second)
    seconds=[3600,60,1]
    #we need to conert alarm time to seconds
    alarmSeconds = sum([a*b for a,b in zip(seconds[:len(alarmTime)], alarmTime)])
    time_now=datetime.datetime.now()
    #convert current time to the seconds
    current_seconds= sum([a*b for a,b in zip(seconds, [time_now.hour, time_now.minute, time_now.second])])
    seconds_until_alarm=alarmSeconds-current_seconds
    if(seconds_until_alarm<0):
        seconds_until_alarm+=86400 #set the new alarm if the seconds is under 0
    print('\nThe Alarm Set Seccessfuly')
    print(f'The Alarm Will Ring At {datetime.timedelta(seconds=seconds_until_alarm)}')
alarm_seconds()

def alarm_ring():
    '''
    this will the ring of the alarm as you know
    '''
    print('\n Waky Waky....')
    winsound.Beep(1000,100)
    winsound.Beep(1100,100)
    winsound.Beep(1200,100)
    audio_address='D:\\Programming_Projects\\Python Projects\\alarm_clock_project\\audio\\ringtone.wav' #copy your custom audio here
    winsound.PlaySound(audio_address,winsound.SND_FILENAME)
    print(f'\nYour Alaram Ring At:{datetime.datetime.now()}')
    file_path='D:\\Programming_Projects\\Python Projects\\alarm_clock_project\\time folder\\time_file.txt' #copy your txt file here please
    with open(file_path,'w+') as file:
        file.write(f'The Time You Tried:{datetime.datetime.now()}')

def alarm_countdown():
    '''
    as you know this will be the alarm count down 
    '''
    global alarmTime,userinput,invalid,seconds,alarmSeconds,time_now,current_seconds,seconds_until_alarm
    for count in range(0,seconds_until_alarm):
        time.sleep(1)
        print(f'\nTime:{seconds_until_alarm}')
        seconds_until_alarm-=1
        if(seconds_until_alarm==1):
            alarm_ring()
            break
alarm_countdown()


    
# Thanks For Using This Is Just A Fun Project Hope You Enjoy 