$(document).ready(function () {
    listing();
    bsCustomFileInput.init();
});

function open_photo_box() {
    $('#upload_photo').click(function () {
        $('#first_modal').css({
            display: 'flex',
        });
        $(document.body).css({
            overflow: 'visible',
        });
    });
}

function close_photo_box() {
    $('#close_photo').click(function () {
        $('#first_modal').css({
            display: 'none',
        });
        $(document.body).css({
            overflow: 'visible',
        });
    });
}

function posting() {
    let content_txt = $('#content_txt').val();

    let content_photo = $('#content_photo')[0].files[0];
    let form_data = new FormData();
    form_data.append('content_photo_give', content_photo);
    form_data.append('content_txt_give', content_txt);

    $.ajax({
        type: 'POST',
        url: '/content',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response['msg']);
            window.location.reload();
        },
    });
}

function listing() {
    $.ajax({
        type: 'GET',
        url: '/listing',
        data: {},
        success: function (response) {
            let contents = response['contents'];
            for (let i = 0; i < contents.length; i++) {
                let content_txt = contents[i]['content_txt'];
                let content_photo = contents[i]['content_photo'];

                let temp_html = `<div class="card" style="width: 293px; height: 293px; object-fit: cover; display: inline-block">
                                        <img src="../static/${content_photo}" class="card-img-top">
                                        <div class="card-body">
                                            <p class="card-text">${content_txt}</p>
                                        </div>
                                    </div>`;

                $('#cards_box').append(temp_html);
            }
        },
    });
}
