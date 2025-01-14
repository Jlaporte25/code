document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('#all_posts').addEventListener('click', () => load_posts('all'));
    document.querySelector('#profile').addEventListener('click', () => load_posts('<str:username>'));
    document.querySelector('#post-form').addEventListener('submit', create_post); 
});

function load_posts(page) {
    fetch(`posts/${page}`)
    .then(response => response.json())
    .then(posts => {
        posts.forEach(post => {
            const newPost = document.createElement('div');
            newPost.className = 'list-group-item';
            newPost.innerHTML = `${post.user} ${post.content} ${post.timestamp} ${post.likes}`;
            document.querySelector('#posts-view').append(newPost);
        });
    });
}

function create_post(event) {
    event.preventDefault();
    const postForm = document.querySelector('#post-form');
    const content = postForm.querySelector('#content').value;
    const user = postForm.user;
    // Add logic to handle the post creation

    fetch('/create_post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // If using Django, include CSRF token
        },
        body: JSON.stringify({
            content: content,
            user: user
        })
    })
    .then(response => response.json())
    .then(result => {
        // Handle the response from the server
        console.log(result);
        if (result.success) {
            // Optionally, reload posts or update the UI
            load_posts('all');
        } else {
            // Handle error
            alert(result.error);
        }
    });
}


