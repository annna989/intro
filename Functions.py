def function():
    print("Hallo, this is code from the function")

print("This is code from our main program")

#To call function just type its name

function()

def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(70, 200))


def minutes_to_hours(seconds, minutes=70): #If you type one aruguments then you need to add const value
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(200))  


def minutes_to_hours(seconds, minutes=70): #If you type both aruguments then python reed only arguments, not const value
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(300, 200))