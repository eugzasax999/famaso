# Get the user's input from the USSD gateway (e.g., *123*1*1#)
user_input = '*123#'

# Define the menu options and their corresponding USSD codes
main_menu = {
    '1': 'Buyer',
    '2': 'Farmer',
    '3': 'About FAMASO',
}

buyer_menu = {
    '1': 'View Orders',
    '2': 'Place an Order',
    '3': 'Contact Support',
    '00': 'Home',
}

farmer_menu = {
    '1': 'View Farm Stats',
    '2': 'Update Farm Info',
    '3': 'Contact Support',
    '00': 'Home',
}

about_menu = {
    '1': 'About Us',
    '00': 'Home',
}

# Function to display a menu and its options
def display_menu(menu):
    response = "Welcome to Famaso.\n"
    for key, option in menu.items():
        response += f"{key}. {option}\n"
    print(response)

# Function to handle buyer-specific logic
def handle_buyer_menu(option):
    switcher = {
        '1': "You selected View Orders. Here are your orders:\n",
        '2': "You selected Place an Order. Please follow the instructions to place an order.\n",
        '3': "You selected Contact Support. Please contact our support team at support@example.com.\n",
        '00': "Returning to the Home/Main Menu.\n",
    }
    print(switcher.get(option, "Invalid option. Please try again.\n"))

# Function to handle farmer-specific logic
def handle_farmer_menu(option):
    switcher = {
        '1': "You selected View Farm Stats. Here are your farm statistics:\n"
             "Farm Name: ABC Dairy Farm\n"
             "Total Cows: 50\n"
             "Milk Production (today): 500 liters\n"
             "Milk Production (this month): 15000 liters\n",
        '2': "You selected Update Farm Info. Please update your farm information:\n"
             "Farm Name: ABC Dairy Farm\n"
             "Owner: John Doe\n"
             "Total Cows: 50\n"
             "Location: Farmington, USA\n"
             "Daily Milk Production: 500 liters/day\n"
             "Farm Size: 100 acres\n",
        '3': f"You selected Contact Support. Please contact our support team at 0726993619.\n",
        '00': "Returning to the Home/Main Menu.\n",
    }
    print(switcher.get(option, "Invalid option. Please try again.\n"))

# Function to handle about menu
def handle_about_menu(option):
    switcher = {
        '1': "In this online platform buyers will be able to interact with farmers in easy way. They will be able to get their required products from a variety of farmers they prefer\n",
        '00': "Returning to the Home/Main Menu.\n",
    }
    print(switcher.get(option, "Invalid option. Please try again.\n"))

# Parse the user's input
input_parts = user_input.split('*')

# Determine the menu level
menu_level = len(input_parts) - 1

# Check the menu level and execute the appropriate logic
if menu_level == 1:
    # Main Menu
    if input_parts[1] in main_menu:
        display_menu(main_menu)
    else:
        print("Invalid option. Please try again.\n")
elif menu_level == 2:
    # Buyer or Farmer Menu
    selected_option = input_parts[2]
    if input_parts[1] == '1' and selected_option in buyer_menu:
        handle_buyer_menu(selected_option)
    elif input_parts[1] == '2' and selected_option in farmer_menu:
        handle_farmer_menu(selected_option)
    else:
        print("Invalid option. Please try again.\n")
else:
    print("Invalid USSD code. Please try again.\n")
