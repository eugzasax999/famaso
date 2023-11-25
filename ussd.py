# Define a dictionary to store user sessions
user_sessions = {}

# Main Menu
def main_menu(user_id):
    return (
        f"Welcome to Famaso.\n"
        f"Are you a Buyer or a Farmer?\n"
        f"1. Buyer\n"
        f"2. Farmer"
    )

# Buyer Profile Menu
def buyer_menu(user_id):
    return (
        f"Buyer Profile\n"
        f"1. View Orders\n"
        f"2. Place an Order\n"
        f"3. Contact Support\n"
        f"00. Home"
    )

# Farmer Section Menu
# ... (previous code) ...

# Farmer Section Menu
def farmer_menu(user_id):
    return (
        f"Farmer Section\n"
        f"1. View Farm Stats\n"
        f"2. Update Farm Info\n"
        f"3. Contact Support\n"
        f"4. View Farm Items\n"  # Add an option to view farm items
        f"00. Home"
    )

# Function to handle user input and navigate menus
# ... (existing code)
def order_items_menu(user_id):
    return (
        f"Farm Items\n"
        f"1. Vegetables\n"
        f"2. Livestock\n"
        f"3. Fruits\n"
        f"4. Farm Inputs\n"
        f"00. Back"
    )
 
# ... (existing code)

# ... (existing code)

def handle_input(user_id, user_input):
    if user_input == "1":
        user_sessions[user_id] = buyer_menu
        return buyer_menu(user_id)
    elif user_input == "2":
        user_sessions[user_id] = farmer_menu
        return farmer_menu(user_id)
    elif user_input == "00":
        user_sessions[user_id] = main_menu
        return main_menu(user_id)
    elif user_input == "3" and user_sessions.get(user_id) == farmer_menu:
        return "Please contact our support team at 0726993619."
    elif user_input in ["1", "2", "3", "4"] and user_sessions.get(user_id) == farmer_menu:
        return order_items_menu(user_id)
    elif user_sessions.get(user_id):
        return user_sessions[user_id](user_id)
    else:
        return main_menu(user_id)

# ... (existing code)

# ... (existing code)


# ... (existing code)



# ... (rest of the code remains the same) ...


# Simulate the USSD session
def simulate_ussd_session():
    user_id = input("Enter your user ID: ")
    user_sessions[user_id] = main_menu
    response = main_menu(user_id)

    while True:
        print(response)
        user_input = input("Enter your choice: ")
        response = handle_input(user_id, user_input)

if __name__ == "__main__":
    simulate_ussd_session()
