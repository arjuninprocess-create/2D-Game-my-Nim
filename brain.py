#1
# 
def minimax(tokens, depth, is_maximizing):
    # Base cases: game over or reached depth limit
    if is_game_over(tokens) or depth == 0:
        return evaluate_board(tokens, is_maximizing)
    
    if is_maximizing:
        best_score = float('-inf')
        # AI can try taking 1, 2, or 3 tokens
        for move in [1, 2, 3]:
            if tokens - move >= 0:
                score = minimax(tokens - move, depth - 1, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        # Human opponent's simulated turns
        for move in [1, 2, 3]:

            if tokens - move >= 0:
                score = minimax(tokens - move, depth - 1, True)
                best_score = min(best_score, score)
        return best_score

#2   
def is_game_over(tokens):
    return tokens <= 0

#3
def evaluate_board(tokens, is_ai_turn):
    # If no tokens are left, the player whose turn it JUST WAS lost.
    if tokens <= 0:
        return 10 if not is_ai_turn else -10
    return 0