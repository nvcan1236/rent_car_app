window.addEventListener('load', function () {
    navBar = document.getElementById('nav-bar');
    quickContact = document.querySelector('.quick-contact')
    welcomeImg = document.querySelector('.welcome-image')

    let i = 1;
    images = [
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510426/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_004742_mvqicz.jpg',
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510426/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_005359_n0mfqx.jpg',
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510426/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_004621_eaba4k.jpg',
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510426/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_005439_camlje.jpg',
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510426/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_004448_fc1upz.jpg',
        'https://res.cloudinary.com/dhwzmp1ef/image/upload/v1706510425/%E1%BA%A2nh%20xe/%E1%BA%A2nh%20%C4%91%E1%BA%A7u%20trang/IMG_20240129_004346_lbayos.jpg'
    ]
    setInterval(() => {
        console.log(images[i])
        console.log(i)
        welcomeImg.style.backgroundImage = `url(${images[i]})`
        if (i==5) {
            i=0;
        }
        else {
            i++;
        }

    }, 5000)


    document.addEventListener('scroll', function () {
        if (window.pageYOffset > 100) {
            navBar.classList.add('fixed')
//            quickContact.classList.add('show')
        } else {
            navBar.classList.remove('fixed')
//            quickContact.classList.remove('show')
        }
    })
})


function showList(id) {
    dropdown = document.getElementById(id)
    dropdownList = dropdown.querySelector('.dropdown-list')
    dropdownItems = dropdown.querySelectorAll('.dropdown-item')

    dropdownList.classList.toggle('hide')


    window.addEventListener('click', function (e) {
        if (!e.target.classList.contains('dropdown-select')) {
            dropdownList.classList.add('hide')
        }
    })
}

productMainImage = document.getElementById('car-main-img')
productSubImages = document.querySelectorAll('.sub-image')

function setMain(id) {
    console.log(productMainImage)
    productMainImage.src = productSubImages[id].src
    productSubImages.forEach(element => {
        element.classList.remove('active')
    });
    productSubImages[id].classList.add('active')

}

function showDetail(id) {
    window.location.href = `/car-detail?id=${id}`
}

//
// modal = document.getElementById('modal')
//
// function showModal(id) {
//
//     modal.classList.add('show')
// }
//
// function closeModal() {
//     modal.classList.remove('show')
// }

