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
  document.querySelector('#email-view').style.display = 'none';

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
      newEmail.className = 'list-group-item list-group-item-action email border border-dark';
      newEmail.innerHTML = `<strong>${email.recipients}</strong> ${email.subject} ${email.timestamp}`;
      if (email.read) {
        newEmail.style.backgroundColor = 'lightgray';
      }
      newEmail.addEventListener('click', function() {
        view_email(email.id);
      });
      document.querySelector('#emails-view').append(newEmail);})

      if (emails.length === 0) {
        document.querySelector('#emails-view').innerHTML = '<p>No emails to display</p>';
      }
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

function view_email(email_id) {
  console.log(`Viewing email: ${email_id}`);

  // Show the email view and hide other views
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';

  // Clear out email view
  document.querySelector('#email-view').innerHTML = '';

  // Fetch email
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    console.log(email);

    // Display email
    const emailView = document.createElement('div');
    emailView.innerHTML = `<p><strong>From:</strong> ${email.sender}</p>
    <p><strong>To:</strong> ${email.recipients}</p>
    <p><strong>Subject:</strong> ${email.subject}</p>
    <p><strong>Body:</strong> ${email.body}</p>
    <p><strong>Timestamp:</strong> ${email.timestamp}</p>`;
    document.querySelector('#email-view').append(emailView);

    // Mark email as read
    fetch(`/emails/${email_id}`, {
      method: 'PUT',
      body: JSON.stringify({
        read: true
      })
    });

    // Add reply button
    const replyButton = document.createElement('button');
    replyButton.className = 'btn btn-sm btn-outline-primary';
    replyButton.innerHTML = 'Reply';
    replyButton.addEventListener('click', function() {
      reply_email(email);
    });
    document.querySelector('#email-view').append(replyButton);

    // Add archive button
    const archiveButton = document.createElement('button');
    archiveButton.className = 'btn btn-sm btn-outline-primary';
    if (email.archived) {
      archiveButton.innerHTML = 'Unarchive';
    } else {
      archiveButton.innerHTML = 'Archive';
    }

    archiveButton.addEventListener('click', function() {
      toggle_archive(email_id, email.archived);
    });
    document.querySelector('#email-view').append(archiveButton);
  });
}

function toggle_archive(email_id, archived) {
  console.log(`Toggling archive for email: ${email_id}`);

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: !archived
    })
  })
  .then(() => load_mailbox('archive'));
}

function reply_email(email) {
  console.log(`Replying to email: ${email.id}`);

  compose_email();

  // Pre-fill composition fields
  document.querySelector('#compose-recipients').value = email.sender;
  document.querySelector('#compose-subject').value = email.subject.startsWith('Re:') ? email.subject : `Re: ${email.subject}`;
  document.querySelector('#compose-body').value = '';
}

