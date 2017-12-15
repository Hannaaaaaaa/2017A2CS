#Hanna Gao Option1 State Transition Table


def pressstart(inactive,active):
    if inactive==True:
        inactive=False
        active=True
    return inactive,active

def enterPIN(inactive,active,alert,alarm):
    if active==True:
        inactive=True
        active=False
    if alert==True:
        inactive=True
        alert=False
    if alarm==True:
        inactive=True
        alarm=False
    return inactive,active,alert,alarm

def activatesensor(active,alert):
    if active==True:
        alert=True
        print('Diiiiiiiiiiiiiiiiiiiii...')
    return active,alert

def twomin(alert,alarm):
    if alert==True:
        print('2min gone...')
        alarm=True
        print('Warning...')
        alert=False
    return alert,alarm

print('1=Press Start Button')
print('2=Enter PIN')
print('3=Activate Sensor')
print('4=Two Minutes Pass')
print('5=Finish')

inactive=True
active=False
alert=False
alarm=False

action=int(input('Input Action: '))
while action!=5:
    if action==1:
        inactive,active=pressstart(inactive,active)
    if action==2:
        PIN=input('Enter PIN')
        inactive,active,alert,alarm=enterPIN(inactive,active,alert,alarm)
    if action==3:
        active,alert=activatesensor(active,alert)
    if action==4:
        alert,alarm=twomin(alert,alarm)
    print('Inactive',inactive)
    print('Active',active)
    print('Alert',alert)
    print('Alarm',alarm)
    action=int(input('Input Action: '))
   
    
    

















        
