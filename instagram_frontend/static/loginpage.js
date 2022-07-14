function toggle_sign_up() {
    $('#no-sign').addClass('is-hidden');
    $('#sign-box').removeClass('is-hidden');
    $('#id_value').addClass('is-hidden');
    $('#password_value').addClass('is-hidden');
    $('#regi-id').removeClass('is-hidden');
    $('#regi-name').removeClass('is-hidden');
    $('#regi-username').removeClass('is-hidden');
    $('#regi-pw').removeClass('is-hidden');
    $('#btn_register').removeClass('is-hidden');
    $('#btn_login').addClass('is-hidden');
    $('#forget_pw').addClass('is-hidden');
    $('#register_text').removeClass('is-hidden');
}

function toggle_sign() {
    $('#sign-box').addClass('is-hidden');
    $('#no-sign').removeClass('is-hidden');
    $('#id_value').removeClass('is-hidden');
    $('#password_value').removeClass('is-hidden');
    $('#regi-id').addClass('is-hidden');
    $('#regi-name').addClass('is-hidden');
    $('#regi-username').addClass('is-hidden');
    $('#regi-pw').addClass('is-hidden');
    $('#btn_register').addClass('is-hidden');
    $('#btn_login').removeClass('is-hidden');
    $('#forget_pw').removeClass('is-hidden');
    $('#register_text').addClass('is-hidden');
}

function sign_up() {
    let id = $('#regi-id').val();
    let name = $('#regi-name').val();
    let username = $('#regi-username').val();
    let pw = $('#regi-pw').val();

    console.log(id, pw);

    if ((id == '', pw == '', name == '', username == '')) {
        alert('빈칸을 입력해주세요!');
        return;
    }

    if (!is_password(pw)) {
        alert('비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자');
        $('#regi-pw').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/sign_up/save',
        data: {
            id_give: id,
            name_give: name,
            username_give: username,
            pw_give: pw,
        },
        success: function (response) {
            alert('회원가입을 축하드립니다!');
            window.location.replace('/login');
        },
    });
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/; //정규표현식
    return regExp.test(asValue);
}

function check_id() {
    let id = $('#regi-id').val();

    $.ajax({
        type: 'POST',
        url: '/sign_up/check_id',
        data: {
            id_give: id,
        },
        success: function (response) {
            if (response['exists']) {
                alert('이미 존재하는 아이디입니다.');
                $('#regi-id').focus();
            } else {
                check_username();
            }
        },
    });
}

function check_username() {
    let username = $('#regi-username').val();

    $.ajax({
        type: 'POST',
        url: '/sign_up/check_username',
        data: {
            username_give: username,
        },
        success: function (response) {
            if (response['exists']) {
                alert('이미 존재하는 사용자이름입니다.');
                $('#regi-username').focus();
            } else {
                sign_up();
            }
        },
    });
}

function sign_in() {
    let id = $('#id_value').val();
    let pw = $('#password_value').val();

    if ((id == '', pw == '')) {
        alert('빈칸을 입력해주세요!');
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/sign_in',
        data: {
            id_give: id,
            pw_give: pw,
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], { path: '/' });
                window.location.replace('/');
            } else {
                alert(response['msg']);
            }
        },
    });
}
