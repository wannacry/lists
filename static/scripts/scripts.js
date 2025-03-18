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


// settings_overlay
let settings_open_overlay_link = document.getElementsByClassName('panel_item_logout')[0]
settings_open_overlay_link.addEventListener('click',settings_open_overlay_link_visible)
function settings_open_overlay_link_visible(){
    open_overlay.classList.toggle('visible');
}

// sex_options
let sex_options_border = document.getElementsByClassName('option_input_container')[0]
let sex_options = document.getElementsByClassName('option_input')[0]
let sex_options_container= document.getElementsByClassName('sex_options_container')[0]
sex_options.addEventListener('click',open_sex_options)
function open_sex_options(){
    sex_options_border.classList.toggle('new_border');
    sex_options_container.classList.toggle('visible');
}
let none_value = document.getElementsByClassName('sex_option_item')[0]
none_value.addEventListener('click',none_valueF)
function none_valueF(){
    sex_options_border.classList.remove('new_border');
    sex_options_container.classList.remove('visible');
    sex_options.value = 'Not specified'
}
let get_male_value = document.getElementsByClassName('sex_option_item')[1]
get_male_value.addEventListener('click',get_male_valueF)
function get_male_valueF(){
    sex_options_border.classList.remove('new_border');
    sex_options_container.classList.remove('visible');
    sex_options.value = 'Male'
}
let get_female_value = document.getElementsByClassName('sex_option_item')[2]
get_female_value.addEventListener('click',get_female_valueF)
function get_female_valueF(){
    sex_options_border.classList.remove('new_border');
    sex_options_container.classList.remove('visible');
    sex_options.value = 'Female'
}
