let urlBase = 'http://localhost:8000/';

$(document).ready(function(){

    const authHeaders = {'X-CSRFToken': 'xYVavrIiypW3jPAHYDB174EmZDKY7RoK'};

    $('.like-btn').click(function(event){
        event.preventDefault();
        const postId  = $(this).data('post-id');
        let data = document.getElementsByClassName(postId)[0];
        if (data.classList.contains('bi-heart')) {
            data.classList.remove('bi-heart')
            data.classList.add('bi-heart-fill')
            url = urlBase + `api/posts/${postId}/like/`;
            method = 'POST'
        } else {
            data.classList.remove('bi-heart-fill')
            data.classList.add('bi-heart')
            url = urlBase + `api/posts/${postId}/dislike/`;
            method = 'DELETE'
        }
        $.ajax({
            url: url,
            method: method,
            headers: authHeaders,
        })
    })
})