
def bugCollector():
    
    print('Welcome to Bug Masters bug collection system.')
    
    counter = 1
    totalBugs = 0
    
    while counter <= 5:
        
        question = 'How many bugs did you collect on day ' + str(counter) + '? '
        
        bugInput = int(input(question))
        
        if bugInput > 0:
            
            totalBugs += bugInput
            
            counter += 1
        
        else:
            
            print('Please enter a non-negative integer.')
        
    print('Great job, you collected', totalBugs, "bugs this week. You're the bug master!")
    


def distanceTraveled():
    
    speed = int(input('Enter the speed of the vehicle in mph: '))
    
    while speed < 0:
        
        print('Please enter a valid integer.')
        speed = int(input('Enter the speed of the vehicle in mph: '))
        
    hours = int(input('Enter how many hours the vehicle traveled: '))
    
    while hours < 0:
        
        print('Please enter a valid integer.')
        hours = int(input('Enter how many hours the vehicle traveled: '))
    
    print('Hour\t\tDistance Traveled')
    print('---------------------------------')
    
    counter = 1
    
    while counter <= hours:
        
        print(counter, '\t\t\t', str(speed * counter))
        
        counter += 1;
    

def pennies():
    
    days = int(input('How many days do you want to accure pennies? '))
    
    while days < 0:
        
        print('Please enter a valid integer.')
        days = int(input('How many days do you want to accure pennies? '))
    
    print('Day\t\t\tSalary')  
    print('------------------------------')
    
    print('1\t\t\t', '$', '{:,.2f}'.format(0.01))
    
    counter = 2
    prev = 0.01
    
    while counter <= days:
        
        prev = prev * 2
        
        print(counter, '\t\t\t', '$', '{:,.2f}'.format(prev))
        
        counter += 0
        
        
def hogwartsTuition():
    
    print('Year\t\t\tTuition Cost')  
    print('------------------------------------')
    
    counter = 2
    prev = 16000.00 * 1.03
    
    print('1\t\t\t', '$', '{:,.2f}'.format(prev))
    
    while counter <= 5:
        
        prev *= 1.03
        
        print(counter, '\t\t\t', '$', '{:,.2f}'.format(prev))
        
        counter += 1
    
    
pennies()