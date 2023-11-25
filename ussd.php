<?php

// Get the user's input from the USSD gateway (e.g., *123*1*1#)
$userInput = $_GET['input'];

// Define the menu options and their corresponding USSD codes
$mainMenu = [
    '1' => 'Buyer',
    '2' => 'Farmer',
    '3' => 'About FAMASO',
];

$buyerMenu = [
    '1' => 'View Orders',
    '2' => 'Place an Order',
    '3' => 'Contact Support',
    
    '00' => 'Home',
];

$farmerMenu = [
    '1' => 'View Farm Stats',
    '2' => 'Update Farm Info',
    '3' => 'Contact Support',
    '00' => 'Home',
];

$aboutMenu = [
    '1' => 'About Us',
    '00' => 'Home'
];

// Function to display a menu and its options
function displayMenu($menu)
{
    $response = "Welcome to Famaso.\n";
    foreach ($menu as $key => $option) {
        $response .= "$key. $option\n";
    }
    echo $response;
}

// Function to handle buyer-specific logic
function handleBuyerMenu($option)
{
    switch ($option) {
        case '1':
            echo "You selected View Orders. Here are your orders:\n";
            // Implement logic to display orders
            break;
        case '2':
            echo "You selected Place an Order. Please follow the instructions to place an order.\n";
            // Implement logic to place an order
            break;
        case '3':
            echo "You selected Contact Support. Please contact our support team at support@example.com.\n";
            // Implement logic to contact support
            break;
        case '00':
            echo "Returning to the Home/Main Menu.\n";
            break;
        default:
            echo "Invalid option. Please try again.\n";
            break;
    }
}

// Function to handle farmer-specific logic
function handleFarmerMenu($option)
{
    switch ($option) {
        case '1':
            echo "You selected View Farm Stats. Here are your farm statistics:\n";
            // Logic to display farm stats
            function displayFarmStats()
{
    
           $farmName = "ABC Dairy Farm";
           $totalCows = 50;
           $todayMilkProduction = "500 liters";
           $thisMonthMilkProduction = "15000 liters";

           echo "Farm Name: $farmName\n";
           echo "Total Cows: $totalCows\n";
           echo "Milk Production (today): $todayMilkProduction\n";
           echo "Milk Production (this month): $thisMonthMilkProduction\n";
    // Add more farm statistics as needed
}
            break;
        case '2':
            echo "You selected Update Farm Info. Please update your farm information:\n";
            // Logic to update farm info
            function displayFarmInfo()
{
    
            $farmName = "ABC Dairy Farm";
            $ownerName = "John Doe";
            $totalCows = 50;
            $location = "Farmington, USA";
            $milkProduction = "500 liters/day";
            $farmSize = "100 acres";

            echo "Farm Name: $farmName\n";
            echo "Owner: $ownerName\n";
            echo "Total Cows: $totalCows\n";
            echo "Location: $location\n";
            echo "Daily Milk Production: $milkProduction\n";
            echo "Farm Size: $farmSize\n";
    
    
}
            break;

        case '3':
            echo "You selected Contact Support. Please contact our support team at .\n";
            // Logic for contact support
            $supportMobileNumber = '0726993619';
           echo "You selected Contact Support. Please contact our support team at $supportMobileNumber.\n";
   
     break;
            
     case '00':
            echo "Returning to the Home/Main Menu.\n";
            break;
        default:
            echo "Invalid option. Please try again.\n";
            break;
    }
}

function handleAboutMenu($option)

{    switch ($option) {
    case '1':
        echo "In this online platform buyers will be able to interact with farmers in easy way. They will be able to get their required products from a variety of farmers they prefer\n";

        break;
        case '00':
            echo "Returning to the Home/Main Menu.\n";
            break;
        default:
            echo "Invalid option. Please try again.\n";
            break;
    }



}


// Parse the user's input
$inputParts = explode('*', $userInput);

// Determine the menu level
$menuLevel = count($inputParts) - 1;

// Check the menu level and execute the appropriate logic
if ($menuLevel == 1) {
    // Main Menu
    if (isset($mainMenu[$inputParts[1]])) {
        displayMenu($menuLevel == 1 ? $mainMenu : []);
    } else {
        echo "Invalid option. Please try again.\n";
    }
} elseif ($menuLevel == 2) {
    // Buyer or Farmer Menu
    $selectedOption = $inputParts[2];
    if ($inputParts[1] == '1' && isset($buyerMenu[$selectedOption])) {
        handleBuyerMenu($selectedOption);
    } elseif ($inputParts[1] == '2' && isset($farmerMenu[$selectedOption])) {
        handleFarmerMenu($selectedOption);
    } else {
        echo "Invalid option. Please try again.\n";
    }
} else {
    echo "Invalid USSD code. Please try again.\n";
}

?>
