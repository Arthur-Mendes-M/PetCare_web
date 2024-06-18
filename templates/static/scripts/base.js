lucide.createIcons();

let hamburger_menu = document.getElementById("hamburger_menu")
let hamburger_menu_middle_bar = document.querySelector("#hamburger_menu span")

let secondary_menu = document.querySelector(".secondary_menu")

let logout_buttons = document.querySelectorAll(".logout")

let all_menu_links = document.querySelectorAll('#side_menu nav ul li, .secondary_menu nav ul li')

all_menu_links.forEach((link, index) => {
    let page = link.getAttribute('data-page')

    link.classList.remove('current')

    if (window.location.pathname.endsWith(page)) {
        all_menu_links[index].classList.add('current')
    }
})

hamburger_menu.addEventListener('click', () => {
    hamburger_menu_middle_bar.classList.toggle('show')
    secondary_menu.classList.toggle('show')
})

logout_buttons.forEach(button => {
    button.addEventListener('click', () => {
        let confirmation = confirm("Você realmente deseja sair do sistema?")
    
        if (confirmation) {
            window.location.href = '/logout'
        }
    })
})