// dropdown menu
let header_dropdown_menu = document.getElementsByClassName('header_account_menu')[0]
let header_dropdown_element = document.getElementsByClassName('dropdown_menu')[0]
header_dropdown_menu.addEventListener('click',visible)
function visible(){
    header_dropdown_element.classList.toggle('visible');
}
document.addEventListener('click', hiden)
function hiden(event) {
    if (!header_dropdown_menu.contains(event.target) && !header_dropdown_element.contains(event.target)) {
        header_dropdown_element.classList.remove('visible');
    }
};


// overlay
let open_overlay_link = document.getElementsByClassName('dropdown_item_link')[2]
let open_overlay = document.getElementsByClassName('open_overlay')[0]
let overlay = document.getElementsByClassName('overlay')[0]
let cancel_overlay = document.getElementsByClassName('cancel_overlay')[0]
open_overlay_link.addEventListener('click',open_overlay_linkF)
function open_overlay_linkF(){
    open_overlay.classList.toggle('visible');
}
open_overlay.addEventListener('click', cancel_overlayF)
function cancel_overlayF(event) {
    if (!open_overlay_link.contains(event.target) && !overlay.contains(event.target)) {
        open_overlay.classList.remove('visible');
    }
};
cancel_overlay.addEventListener('click', cancel_btn_overlayF)
function cancel_btn_overlayF(){
    open_overlay.classList.remove('visible');
}
// overlay
let rating_open_overlay_link = document.getElementsByClassName('rating_button')[0]
let open_overlay2 = document.getElementsByClassName('open_overlay')[1]
let overlay2 = document.getElementsByClassName('overlay')[1]
let cancel_overlay2 = document.getElementsByClassName('cancel_overlay')[1]
rating_open_overlay_link.addEventListener('click',rating_open_overlay_linkF)
function rating_open_overlay_linkF(){
    open_overlay2.classList.toggle('visible');
}
open_overlay2.addEventListener('click', cancel_overlayF2)
function cancel_overlayF2(event) {
    if (!rating_open_overlay_link.contains(event.target) && !overlay2.contains(event.target)) {
        open_overlay2.classList.remove('visible');
    }
};

// add to list menu
document.getElementsByClassName('add_list_button')[0].addEventListener('click',f);
function f(){
    document.getElementsByClassName('hiden_add_menu')[0].classList.toggle('visible')
}