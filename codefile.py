print ("Welcome to Concert Coordinator!")
service = input ("Are you entering data for a musician (enter 'm') or concert date?(enter 'c')\nMusician or concert date? : ")
if service == "m":
    print ("Please enter the artist you are seeing so we can log it!")
    musician = input ("Artist:")
    print ("Perfect! What date are you seeing the musician?")
    input ("Enter date")
    print ("Musician and date is now logged for you, thank you!")
