$(document).ready(() => {
    $.ajax('/edit_profile/', {
        'type': "POST",
        'async': true,
        'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'get_data': true
        },
        'dataType': "json",
        'success': function (data) {
            document.getElementById('id_username').value = data['username'];
            document.getElementById('id_email').value = data['email'];
            document.getElementById('id_bio').value = data['bio'];
            document.getElementById('profile-img').setAttribute('src', data['avatar'])
        }
    });
    
});


function edit_profile() {
    $.ajax('/edit_profile/', {
        'type': "POST",
        'async': true,
        'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'edit': true,
            'username': document.getElementById('id_username').value,
            'email': document.getElementById('id_email').value,
            'bio': document.getElementById('id_bio').value
        },
        'dataType': "json",
        'success': function (data) {
            console.log('success')
        }
    });
}