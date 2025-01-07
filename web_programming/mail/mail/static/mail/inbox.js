document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM fully loaded and parsed");

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Send email
  const composeForm = document.querySelector('#compose-form');
  if (composeForm) {
    console.log("Attaching submit event listener to compose form");
    composeForm.addEventListener('submit', send_email);
  } else {
    console.log("Compose form not found");
  }

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  console.log("Compose email view");

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  console.log(`Loading mailbox: ${mailbox}`);

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    console.log(emails);

    // Display emails
    emails.forEach(email => {
      const newEmail = document.createElement('div');
      newEmail.innerHTML = `<strong>${email.sender}</strong> ${email.subject} ${email.timestamp}`;
      newEmail.addEventListener('click', function() {
          console.log('This element has been clicked!')
      });
      document.querySelector('#emails-view').append(newEmail);})
  })
};

function send_email(event) {
  event.preventDefault();
  console.log("Sending email");

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
    })
  })
  .then(response => response.json())
  .then(result => {
    // Print result
    console.log(result);
    load_mailbox('sent');
  });
};
