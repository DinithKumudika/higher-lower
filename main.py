import random
from art import logo,vs
from data import game_data
from os import system,name

#clearing console
def clear_console():
     if(name == 'nt' or name == 'dos'):
          system('cls')
     else:
          system('clear')

#get random item from the game_data        
def generate_question():
     random_data = random.choice(game_data)
     return random_data

#print two options and return their follower_counts
def display_options(option):
     follower_count = option['follower_count']
     celeb_name = option['name']
     desc = option['description']
     country = option['country']
     print(f"{celeb_name}, a {desc} from {country}")
       
     return follower_count
     
#compare follower counts of 2 options
def compare_follower_counts(count_a,count_b):
     if count_a > count_b:
          return "a"
     else:
          return "b"

# check answer and max follower count return true if they match, otherwise return false    
def check_answer(guess,result):
     if result == guess:
          return True
     else:
          return False

def main_game():
     is_over = False
     score = 0
     
     option_a = generate_question()
     option_b = generate_question()
      
     while not is_over:
          clear_console() 
          print(logo)
          
          if option_a == option_b:
               option_b = generate_question()
          
          print(f"Current score:{score}")
          print("\n")
          
          print("Option A : ", end = '')
          follower_count_a  = display_options(option_a)
          
          print(vs)
          
          print("Option B : ", end = '')
          follower_count_b = display_options(option_b)
          print("\n")

          user_choice = input("Who has more folowers? type 'a' for option A and type 'b' for option B: ").lower()
          result = compare_follower_counts(follower_count_a,follower_count_b)

          if check_answer(user_choice,result) == True:
               print("Correct answer!")
               if user_choice == "a":
                    option_a = option_b       
               score += 1     
               option_b = generate_question()   
          else:
               print(f"Oops! Wrong answer. Your final score: {score}")
               is_over = True

main_game()
