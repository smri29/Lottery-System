import random

# Global lists to store lottery tickets and user purchases
lottery_tickets = []
user_tickets = {}


# Function to add lottery tickets
def add_lottery_tickets():
    global lottery_tickets
    tickets = input("Admin: Enter the lottery ticket numbers separated by spaces: ").split()
    lottery_tickets = [int(ticket) for ticket in tickets]
    print(f"Lottery tickets added: {lottery_tickets}")


# Function for users to buy tickets
def buy_tickets():
    global user_tickets
    name = input("Enter your name: ")
    print(f"Available tickets: {lottery_tickets}")
    chosen_tickets = input(f"{name}, enter the ticket numbers you want to buy (separated by spaces): ").split()
    chosen_tickets = [int(ticket) for ticket in chosen_tickets]

    for ticket in chosen_tickets:
        if ticket not in lottery_tickets:
            print(f"Ticket {ticket} is not available or already purchased.")
            continue
        # Add tickets to the user's list
        user_tickets.setdefault(name, []).append(ticket)
        # Remove the ticket from the available tickets
        lottery_tickets.remove(ticket)

    print(f"{name} purchased tickets: {user_tickets[name]}")
    print(f"Remaining tickets: {lottery_tickets}")


# Function to pick a random winner
def pick_winner():
    if not user_tickets:
        print("No users have purchased tickets. No winner can be chosen.")
        return

    # Create a combined list of all purchased tickets
    all_purchased_tickets = [(user, ticket) for user, tickets in user_tickets.items() for ticket in tickets]
    winner = random.choice(all_purchased_tickets)
    print(f"The winning ticket is {winner[1]}, and the winner is {winner[0]}!")


# Main function to run the lottery system
def lottery_system():
    while True:
        print("\n--- Lottery System ---")
        print("1. Add lottery tickets (Admin)")
        print("2. Buy lottery tickets (User)")
        print("3. Pick a winner")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_lottery_tickets()
        elif choice == '2':
            buy_tickets()
        elif choice == '3':
            pick_winner()
        elif choice == '4':
            print("Exiting the lottery system.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the lottery system
lottery_system()
