function get_page_num() {
    let page_num = document.getElementsByClassName('current_page')[0].textContent
    page_num = parseInt(page_num, 10)
    return page_num
}
function get_max_page() {
    let max_page = document.getElementsByClassName('last_page')[0].textContent
    max_page = parseInt(max_page, 10)
    return max_page
}


document.querySelectorAll('button.sorting_link').forEach(function (element) {
    element.addEventListener('click', function () {

        document.querySelectorAll('button.sorting_link').forEach(function (element) {
            element.parentElement.classList.remove('sorting_checked_item')
            element.classList.remove('active_sorting_link')
        })
        element.parentElement.classList.add('sorting_checked_item')
        element.classList.add('active_sorting_link')

        let sort_order = document.querySelector("input[type='radio']:checked").value
        page_num = get_page_num()
        ajax_sorting(sort_order, element.value, page_num)
    })
})

document.querySelectorAll("input[name='sort_order']").forEach(function (element) {
    element.addEventListener('click', function () {

        document.querySelectorAll("input[name='sort_order']").forEach(function (element) {
            element.parentElement.classList.remove('sorting_checked_item')
        })
        element.parentElement.classList.add('sorting_checked_item')

        let current_sorting_value = document.getElementsByClassName('active_sorting_link')[0].value
        page_num = get_page_num()
        ajax_sorting(element.value, current_sorting_value, page_num)
    })
})


function ajax_sorting(sort_order = 'desc', sorting_value = 'vote_count', page_num = 1) {


    fetch(`/catalog_sorting/${page_num}/?sort_order=${sort_order}&sorting_value=${sorting_value}`)

        .then(function (response) {
            if (response.ok) {
                return response.json()
            }
            else {
                throw new Error(`Error status: ${response.status}`)
            }
        })

        .then(function (movies) {
            history.pushState(null, '', `/catalog/${page_num}/?sort_order=${sort_order}&sorting_value=${sorting_value}`)

            const container = document.getElementsByClassName('catalog_items')[0]
            container.innerHTML = ''

            movies[0].forEach(function (movie) {

                let imdb_rating = movie['fields'].imdb_rating
                if (imdb_rating != null) {
                    rating = `<span class="catalog_item_imdb_rating">${movie['fields'].imdb_rating.toFixed(1)}/10 IMDB</span>`
                }
                else {
                    rating = `<span class="catalog_item_imdb_rating">${movie['fields'].vote_average.toFixed(1)}/10 TMDB</span>`
                }

                const catalog_item = document.createElement('div')
                catalog_item.classList.add('catalog_item')
                catalog_item.innerHTML = 
                `<a href="/movie_detail/${movie.pk}" class="catalog_item_link">
                    <div class="catalog_item_poster">
                        <img src="{% static '' %}" alt="Poster img" class="catalog_poster">
                    </div>
                    <span class="catalog_item_name">${movie['fields'].title}</span>
                    <div class="catalog_item_info">
                        <span class="catalog_item_release_date">${movie['fields'].release_date}</span>
                        ${rating}
                    </div>
                </a>`
                container.appendChild(catalog_item);
            })

            document.getElementsByClassName('current_page')[0].textContent = movies[1]['current_page']
            document.getElementsByClassName('last_page')[0].textContent = movies[1]['last_page']
        })

        .catch(function (error) {
            console.log(`Error: ${error.message}`)
        })

}

document.addEventListener('DOMContentLoaded', function () {
    let url = new URL(window.location);
    let sort_order = url.searchParams.get('sort_order')
    let sorting_value = url.searchParams.get('sorting_value')
    page_num = get_page_num()
    if (sort_order == null & sorting_value == null) {
        ajax_sorting(undefined, undefined, page_num)
    }
    ajax_sorting(sort_order, sorting_value, page_num)

    if(sort_order=='asc'){
        document.querySelectorAll("input[name='sort_order']").forEach(function (element) {
            element.parentElement.classList.remove('sorting_checked_item')
        })
        document.querySelector("input[id='asc']").parentElement.classList.add('sorting_checked_item')
        document.querySelector("input[id='asc']").checked = true
    }

    if(sorting_value=='vote_average'){
        document.querySelectorAll('button.sorting_link').forEach(function (element) {
            element.parentElement.classList.remove('sorting_checked_item')
            element.classList.remove('active_sorting_link')
        })
        document.querySelector('button[value="vote_average"]').parentElement.classList.add('sorting_checked_item')
        document.querySelector('button[value="vote_average"]').classList.add('active_sorting_link')
    }
    else if(sorting_value=='release_date'){
        document.querySelectorAll('button.sorting_link').forEach(function (element) {
            element.parentElement.classList.remove('sorting_checked_item')
            element.classList.remove('active_sorting_link')
        })
        document.querySelector('button[value="release_date"]').parentElement.classList.add('sorting_checked_item')
        document.querySelector('button[value="release_date"]').classList.add('active_sorting_link')
    }
})

document.getElementsByClassName('first_link')[0].addEventListener('click', function () {
    let url = new URL(window.location);
    let sort_order = url.searchParams.get('sort_order')
    let sorting_value = url.searchParams.get('sorting_value')
    first_page = 1
    ajax_sorting(sort_order, sorting_value, first_page)
    window.scrollTo({ top: 0, behavior: 'smooth' })
})
document.getElementsByClassName('previous_link')[0].addEventListener('click', function () {
    let url = new URL(window.location);
    let sort_order = url.searchParams.get('sort_order')
    let sorting_value = url.searchParams.get('sorting_value')
    page_num = get_page_num()
    let previous_link = page_num - 1
    ajax_sorting(sort_order, sorting_value, previous_link)
    window.scrollTo({ top: 0, behavior: 'smooth' })
})
document.getElementsByClassName('next_link')[0].addEventListener('click', function () {
    let url = new URL(window.location);
    let sort_order = url.searchParams.get('sort_order')
    let sorting_value = url.searchParams.get('sorting_value')
    page_num = get_page_num()
    let next_link = page_num + 1
    ajax_sorting(sort_order, sorting_value, next_link)
    window.scrollTo({ top: 0, behavior: 'smooth' })

})
document.getElementsByClassName('last_link')[0].addEventListener('click', function () {
    let url = new URL(window.location);
    let sort_order = url.searchParams.get('sort_order')
    let sorting_value = url.searchParams.get('sorting_value')
    max_page = get_max_page()
    ajax_sorting(sort_order, sorting_value, max_page)
    window.scrollTo({ top: 0, behavior: 'smooth' })
})
