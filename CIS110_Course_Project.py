print(f"Hi, there! This is a story about an amazing adventurer who is looking for the lost golden city and it's treasures.")
print(f"Whether the adventurer finds the treasures or not will be base on your input decisions.")
print(f"Before the story begins, you will have to answer a few quesitons.")
print(f"After typing your answer, make sure to press the Enter Key.")
input(f"\nPress the Enter Key to start the journey...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    gender = input(f"\nWhat is your gender: ")
    while (len(gender) == 0):
        gender = input(f"Please enter a gender: ")
     
    name = input(f"What is your name: ")
    while (len(name) == 0):
        name = input(f"Name is required for the story to continue. Please enter a name: ")
        
    country = input(f"What is a country you want to visit the most: ")
    while (len(country) == 0):
        country = input(f"Please enter a country: ")
        
    typeOfCommute = input(f"What is your favorite way of commuting? Bike, Car, Train, Plane, Bus, etc..: ")
    while (len(typeOfCommute) == 0): 
        typeOfCommute = input(f"Enter a type of commute: ") 
        
    item = input(f"What is one item you can't live without: ")
    while (len(item) == 0):
        item = input(f"Enter one item you want to take everywhere: ") 
        
    print(f"Story begins, Let's Go!") 
    print(f"There is a famous {gender} adventurer name {name}, who is looking for the lost golden city and it's treasures.")
    print(f"{name} wants to go to {country} because the lost golden city is located there") 
    print(f"{name} is thinking of ways to get to {country} fastest to be the first person to discover the treasures.") 
    print(f"{name} realized using {typeOfCommute} will get there the fastest.") 
    print(f"{name} is finally on the way to {country} taking {item} to help in the journey.") 
    print(f"{name} is dropped off in the remote jungle of {country}. there are a lot of trees and jungle is deep")
    print(f"Even though the journey is tough, {name} doesn't give up. After many hours of exploring the jungle, {name} finds an old looking paper on the ground which looks like a map.")
    
    takeTheMap = input(f"Should {name} picks up the map? Type yes or no: ")
    while takeTheMap.lower() != "yes" and takeTheMap.lower() != "no":
        takeTheMap = input("Please type yes or no: ") 
        
    if takeTheMap == "yes": 
        print(f"{name} picks up the map and reads it. To {name} surprise, it looks like its map showing how to get to the lost golden city and treasures.")
        print(f"The map looks like it's made by somewhere who been to the lost golden city. It has history of {country} lost treasures, what {name} should be expecting in this journey going forward.")   
        print(f"The map shows obstacles {name} will face and there will be a big door a long this journey. Map further explain that going through this door is dangerous but it should be worth it on the other side")
        print(f"{name} takes the map and remembers it's details and moves forwad with the journey.") 
    else:
        print(f"{name} thinks it's a waste of time to picks up this old looking paper.")
        print(f"{name} thinks a lot of time has been wasted already, and picking this paper up it's not going to help in this journey") 
        print(f"{name} uses {item} to clear the jungle and moves along in the journey without picking up or reading the paper.")
        
    print(f"Many hours has passed, {name} continues moving a long the jungle. It has tough journey {name} is not giving up.")
    print(f"After awhile {name} sees a huge door that is blocking the way")
    print("There is a narrow way to go through the door but it looks really dangrous. The door looks like it's thousands of years old and it could collapse anytime")
    
    goThroughDoor = input(f"Should {name} go through this door? Type yes or no: ")
    while goThroughDoor.lower() != "yes" and goThroughDoor.lower() != "no":
        goThroughDoor = input("Please type yes or no: ")
        
    if goThroughDoor == "yes": 
        print(f"{name} squeezes through the narrow passage in the door. The passage is very tight but {name} keeps pushing through it")
        print(f"The door collapsed right after {name} passed through it.") 
        print(f"{name} feels very lucky to be made it through the door and keeps continuing on the path.") 
        print(f"The path led {name} to the lost golden city and it's treasures. {name} is so exicted and happy to finally discover the treasures.")
    else:
        print(f"{name} thinks it's too dangerous to go through this door because it looks like it can fall anytime.")
        print(f"{name} doesn't want to risk it all to find this treasures. So, {name} decided not to go through this door")
        print(f"{name} goes opposites side of the door, using {item} as a tool to to go forward in this journey") 
        
    if takeTheMap == "yes" and goThroughDoor == "yes":
        print(f"{name} feels really grateful to whoever left this map.")
        print(f"{name} became the first person in the world to discover the last golden city and it's treasues") 
        print(f"{name} is also glad to take risks and never giving up on this journey.")
        print(f"{name} became famous throughout the world as the first person to achieve the almost impossible journey")
    elif takeTheMap == "no" and goThroughDoor == "no":
        print(f"{name} keeps moving on the journey without finding anything. {name} feels something is missing and something thats overlooked")
        print(f"After many hours of not finding anything, {name} feels exhausted and thinks taking more risks should have been better")
        print(f"{name} keeps wondering the jungle and doesn't know what to do next") 
    else:
        print(f"After many days, in this {country} jungle, {name} starting to feels more familiar with the place")
        print(f"{name} tries many different ways to get to the golden city")
        print(f"After very heavy storm, there was a path thats opened leading {name} somewhere.")
        print(f"This path fianlly led {name} to the lost golden city and it's treasures")
        print(f"Somethime all it takes is luck and never giving up to acheive your goals {name} thinks.") 
    print("The End")
    keepPlaying = input("Do you want to play again? Enter yes or no: ") 
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no": 
        keepPlaying = input("Please type yes or no: ")
        

    

          
    
        

        
    


     
        
    
        

        
