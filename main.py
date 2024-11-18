import random

def admin_input():
    """Admin enters the numbers of the lottery tokens."""
    while True:
        try:
            tokens = input("Admin: Enter lottery tokens separated by spaces: ").strip().split()
            if not tokens:
                print("Please enter at least one token.")
                continue
            return tokens
        except ValueError:
            print("Invalid input. Please try again.")

def user_participation(tokens):
    """Users buy lottery tokens."""
    user_data = {}
    print("\nUsers can now buy lottery tokens!")

    while True:
        user_name = input("Enter your name (or 'done' to finish buying): ").strip()
        if user_name.lower() == 'done':
            break

        print(f"Available tokens: {tokens}")
        token_choices = input(f"{user_name}, choose tokens from the available list (separated by spaces): ").strip().split()

        # Validate each token
        invalid_tokens = [t for t in token_choices if t not in tokens]
        if invalid_tokens:
            print(f"Invalid or unavailable tokens: {', '.join(invalid_tokens)}. Try again!")
            continue

        # Assign valid tokens to the user
        for token in token_choices:
            if user_name in user_data:
                user_data[user_name].append(token)
            else:
                user_data[user_name] = [token]
            tokens.remove(token)  # Remove the token from available list

        print(f"{user_name} has successfully purchased tokens: {', '.join(token_choices)}.\n")

        if not tokens:
            print("All tokens have been sold!")
            break

    return user_data

def pick_winner(user_data):
    """Randomly pick a winning token and determine the winner."""
    if not user_data:
        print("No participants in the lottery. No winner can be selected.")
        return

    all_tokens = [(user, token) for user, tokens in user_data.items() for token in tokens]
    winner = random.choice(all_tokens)
    print("\n🎉 Lottery Winner Announcement 🎉")
    print(f"Winning Token: {winner[1]}")
    print(f"Winner: {winner[0]}")

def lottery_system():
    """Main function to manage the lottery system."""
    print("Welcome to the Lottery System!\n")

    tokens = admin_input()
    user_data = user_participation(tokens)
    pick_winner(user_data)

# Start the Lottery System
lottery_system()
