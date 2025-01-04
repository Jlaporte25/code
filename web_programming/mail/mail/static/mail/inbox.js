document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#sent-view').style.display = 'none';
  document.querySelector('#archive-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Send email
  document.querySelector('#compose-form').addEventListener('submit', send_email);

}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#sent-view').style.display = 'none';
  document.querySelector('#archive-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Load emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);

    // Clear the emails view
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Display each email
    emails.forEach(email => {
      const emailElement = document.createElement('div');
      emailElement.className = 'email';
      emailElement.innerHTML = `
        <div><strong>From:</strong> ${email.sender}</div>
        <div><strong>Subject:</strong> ${email.subject}</div>
        <div><strong>Timestamp:</strong> ${email.timestamp}</div>
      `;
      emailElement.addEventListener('click', () => load_email(email.id));
      document.querySelector('#emails-view').append(emailElement);
    });
  });
}

function load_email(email_id) {
  // Fetch the email
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    // Print email
    console.log(email);

    // Show the email view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#sent-view').style.display = 'none';
    document.querySelector('#archive-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'block';

    // Display the email
    const emailView = document.createElement('div');
    emailView.innerHTML = `
      <div><strong>From:</strong> ${email.sender}</div>
      <div><strong>To:</strong> ${email.recipients.join(', ')}</div>
      <div><strong>Subject:</strong> ${email.subject}</div>
      <div><strong>Timestamp:</strong> ${email.timestamp}</div>
      <hr>
      <div>${email.body}</div>
    `;
    document.querySelector('#emails-view').append(emailView);
  });
}

function send_email() {
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
  });

}

function archive_email(email_id) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: true
    })
  })
  .then(() => load_mailbox('inbox'));
}
