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
        
    


     
        
    
        

        
