const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Middleware to parse USSD requests
app.use(bodyParser.urlencoded({ extended: false }));

// Define initial menu options
const mainMenu = {
  text: 'Welcome to Famaso.\nAre you a Buyer or a Farmer?',
  options: [
    { code: '1', label: 'Buyer' },
    { code: '2', label: 'Farmer' },
  ],
};

const buyerMenu = {
  text: 'Buyer Profile',
  options: [
    { code: '1', label: 'View Orders' },
    { code: '2', label: 'Place an Order' },
    { code: '3', label: 'Contact Support' },
    { code: '00', label: 'Home' },
  ],
};

const farmerMenu = {
  text: 'Farmer Section',
  options: [
    { code: '1', label: 'View Farm Stats' },
    { code: '2', label: 'Update Farm Info' },
    { code: '3', label: 'Contact Support' },
    { code: '00', label: 'Home' },
  ],
};

// USSD menu handling function
function handleUSSD(text, menu) {
  let response = '';
  for (const option of menu.options) {
    response += `${option.code}: ${option.label}\n`;
  }
  return `${menu.text}\n${response}`;
}

// USSD entry point
app.post('/ussd', (req, res) => {
  const { text } = req.body;
  const sessionData = req.body.sessionData || {};

  let menu;

  if (!sessionData.menu) {
    menu = mainMenu;
  } else if (sessionData.menu === 'buyer') {
    menu = buyerMenu;
  } else if (sessionData.menu === 'farmer') {
    menu = farmerMenu;
  }

  if (text === '00') {
    sessionData.menu = undefined; // Return to the main menu
    res.send(handleUSSD('', mainMenu));
  } else if (menu) {
    // Handle menu selection
    const selectedOption = menu.options.find((option) => option.code === text);
    if (selectedOption) {
      res.send(handleUSSD(selectedOption.label, menu));
    } else {
      res.send('Invalid option. Please try again.');
    }
  } else {
    res.send('Invalid option. Please try again.');
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
