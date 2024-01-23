
window.addEventListener('load', function () {
    navBar = document.getElementById('nav-bar');
    quickContact = document.querySelector('.quick-contact')


    document.addEventListener('scroll', function () {
        if (window.pageYOffset > 100) {
            navBar.classList.add('fixed')
            quickContact.classList.add('show')
        }
        else {
            navBar.classList.remove('fixed')
            quickContact.classList.remove('show')
        }
    })
})

function showList(id) {
    dropdown  = document.getElementById(id)
    dropdownList =  dropdown.querySelector('.dropdown-list')
    dropdownItems =  dropdown.querySelectorAll('.dropdown-item')

    dropdownList.classList.toggle('hide')


    window.addEventListener('click', function(e) {
        if (!e.target.classList.contains('dropdown-select')) {
             dropdownList.classList.add('hide')
        }
    })
}


