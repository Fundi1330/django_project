
$(() => {
    $('#id_search').keyup(() => {
        $.ajax('/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'input': document.getElementById('id_search').value
            },
            'success': (data) => {
                document.getElementById('result').innerHTML = data;
            }
        })
    });
});

$(document).ready(() => {
    let btn = document.getElementById('open-search-btn');

    btn.addEventListener('click', () => {
        document.getElementById('search').show()
    });
});