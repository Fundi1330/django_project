function loadImage() {
    $('#image').change(() => {
        document.getElementById('add-image').close();
        document.getElementById('add-post').show();
        let image = new FormData();
        //document.getElementById('image-upload')
        image.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        image.append('file', document.getElementById('image').files[0]);
        $.ajax('/add_post/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': image,
            'processData': false,
            'contentType': false,
            'success': (data) => {
                document.getElementById('post-image').setAttribute('src', '../static/images/upload.png')
            }
        });
    });
}
function ajax() {
    $('#add-post-btn').click(() => {
        let btn = $(this);
        $.ajax(btn.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'title': $('#id_title').val(),
                'body': $('#id_body').val()
            },
            'success': (data) => {
                document.getElementById('post').innerHTML += `<a href="${data['id']}">${data['title']}</a>`;
                document.getElementById('add-post').close();
                document.getElementById('page').inert = false;
            }
        });
    });
}
function clicks() {
        $('#open-dialog-btn').click(() => {
            document.getElementById('add-image').show();
            document.getElementById('page').inert = true;
        });
        $('#close-btn').click(() => {
            document.getElementById('add-image').close();
            document.getElementById('page').inert = false;
        });
        $('#close-btn1').click(() => {
            document.getElementById('add-post').close();
            document.getElementById('page').inert = false;
        })
    }


$(document).ready(function () { 
    clicks();
    loadImage();
    ajax();
    document.getElementById('add-image').addEventListener('close', () => {
        document.getElementById('page').inert = false;
    }) 
 })