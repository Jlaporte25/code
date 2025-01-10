document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#all_posts').addEventListener(onclick, () => load_posts());
    document.querySelector('post-form').onsubmit = () => create_post();
})

function load_posts(post) {
    document.querySelector('#posts-view').innerHTML = '';

    fetch(`posts/${post}`)
    .then(response => response.json)
    .then(posts => {

        posts.forEach(post => {
            const newPost = document.createElement('div');
            newPost.className = 'list-group-item'
            newPost.innerHTML = `${post.user} ${post.content} ${post.timestamp} ${post.likes}`;
            document.querySelector('#posts-view').append(newPost);
        });
    })
}

function create_post() {
    const postForm = document.querySelector('#post-form');
    const content = postForm.querySelector('#content').value;
    const user = postForm.querySelector('#user').value;
    const timestamp = postForm.querySelector('#timestamp').value;


    fetch('/create_post', {
        method: 'POST',
        body: JSON.stringify({
            content: content,
            user: user,
            timestamp: timestamp,
            likes: likes

        })
    })

    .then(response => response.json())
    .then(result => {
        console.log(result);
        load_posts();
    });

    return false;

}