const nodemailer = require('nodemailer');

// Create a transporter using your SMTP settings
const transporter = nodemailer.createTransport({
  host: 'smtp-relay.brevo.com', // e.g., 'smtp.gmail.com'
  port: 587, // Port for most SMTP servers
  secure: false, // true for 465, false for other ports
  auth: {
    user: 'eugeenasande999@gmail.com',
    pass: '6vL3HAYSgqKmxEw7'
  }
});

// Define the email options
const mailOptions = {
  from: 'eugeenasande999@gmail.com',
  to: 'famso.fmks@gmail.com',
  subject: 'Test Email',
  text: 'Welcome to FAMASO, feel free to test our products.'
};

// Send the email
transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.error(error);
  }
  console.log('Email sent:', info.response);
});
