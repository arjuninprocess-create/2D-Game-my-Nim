#
import brain
import time



def find_best_move(tokens):
    best_score = float('-inf')
    best_move = 1
    
    for move in [1, 2, 3]:
        if tokens - move >= 0:
            # Look ahead up to 10 moves
            score = brain.minimax(tokens - move, 10, False) 
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def play_game():
    tokens = 15
    print("Welcome to Nim! Take 1, 2, or 3 tokens. The player forced to take the last one loses.")
    
    while tokens > 0:
        # --- HUMAN TURN ---
        print(f"\nRemaining tokens: {'O ' * tokens} ({tokens})")
        human_move = 0
        while human_move not in [1, 2, 3] or tokens - human_move < 0:
            try:
                human_move = int(input("Your turn! How many tokens do you want to take? (1-3): "))
            except ValueError:
                print("Please enter a valid number.")
        
        tokens -= human_move
        if brain.is_game_over(tokens):
            print("\nYou took the last token! You lose! 🤖 Wins.")
            break
            
        # --- AI TURN ---
        print(f"\nRemaining tokens: {'O ' * tokens} ({tokens})")
        print("AI is thinking...")
        time.sleep(1) # Dramatic pause
        
        ai_move = find_best_move(tokens)
        print(f"AI takes {ai_move} token(s).")
        tokens -= ai_move
        
        if brain.is_game_over(tokens):
            print("\nAI took the last token! You win! 🎉")
            break

if __name__ == "__main__":
    play_game()