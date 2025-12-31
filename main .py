import random  

def game():
   
    choice_mapping = {"s": 1, "w": 0, "g": -1}       
    reverse_mapping = {1: "snake", 0: "water", -1: "gun"}  

    
    player = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

    
    if player not in choice_mapping:
        return "Invalid choice! Please enter s, w, or g."

    
    player_val = choice_mapping[player]

    
    comp = random.choice([1, 0, -1])
    print("Computer chose:", reverse_mapping[comp])

    
    if player_val == comp:
        return "It's a Draw! Both chose the same."
    elif player_val == 1 and comp == 0:
        return "Snake drinks water → Player wins!"
    elif player_val == 0 and comp == -1:
        return "Water douses gun → Player wins!"
    elif player_val == -1 and comp == 1:
        return "Gun shoots snake → Player wins!"
    elif comp == 1 and player_val == 0:
        return "Snake drinks water → Computer wins!"
    elif comp == 0 and player_val == -1:
        return "Water douses gun → Computer wins!"
    elif comp == -1 and player_val == 1:
        return "Gun shoots snake → Computer wins!"
    else:
        return "Unexpected outcome!"

print(game())