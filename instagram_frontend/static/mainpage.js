//모달
const body = document.querySelector('body');
const modal = document.querySelector('.modal');
const btnOpenPopup = document.querySelector('.btn-open-popup');

btnOpenPopup.addEventListener('click', () => {
    modal.classList.toggle('show');

    if (modal.classList.contains('show')) {
        body.style.overflow = 'hidden';
    }
});

modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.classList.toggle('show');

        if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
        }
    }
});

function cardview() {
    if (this.parentNode.getElementsByTagName('div')[0].style.display != '') {
        this.parentNode.getElementsByTagName('div')[0].style.display = '';
        this.value = '숨기기';
    } else {
        this.parentNode.getElementsByTagName('div')[0].style.display = 'none';
        this.value = '더보기';
    }
}
