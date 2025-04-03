document.querySelectorAll('span.lists_link').forEach(function(element){
    element.addEventListener('click',function(){
        lists_ajax(element.textContent.toLowerCase())
    })
})

function lists_ajax(lists_status='all'){
    fetch(`/account/profile/lists_choise/?lists_status=${lists_status}`)
    .then(function(response){
        if(response.ok){
            return response.json()
        }
        else{
            throw new Error(`Error status: ${response.status}`)
        }
    })

    .then(function(status){
        history.pushState('',null,`/account/profile/list/?lists_status=${lists_status}`)

        const container = document.querySelector('div.list_adding_items')
        container.innerHTML = ''

        status.forEach(function(movie,index){
            console.log(movie.id)
            let item = document.createElement('div')
            item.classList.add('list_item')
            item.innerHTML = 
            `<a href='/movie_detail/${movie.id}' class="link_on_list_item">
                                <div class="list_adding_item">
                                    <div class="list_adding_item_poster">
                                        <img src="" alt="Poster" class="poster_img">
                                    </div>
                                    <div class="list_adding_item_info">
                                        <p>№${index+1}<span></span></p>
                                        <p>Name:<span> ${movie.title}</span></p>
                                        <p>Duration:<span>${movie.runtime}m</span></p>
                                        <p>Release date:<span>${movie.release_date}</span></p>
                                        <p>${movie.status[0].toUpperCase()+movie.status.slice(1)} date:<span>${movie.date_added}</span></p>
                                        <p>IMDB rating:<span>${movie.imdb_rating}/10</span></p>
                                        <p>TMDB rating:<span>${movie.vote_average}/10</span></p>
                                    </div>
                                </div>
                            </a>`
            container.appendChild(item)
        })
    })

    .catch(function(error){
        console.log(`Error: ${error.message}`)
    })
}

document.addEventListener('DOMContentLoaded',function(){
    let url = new URL(window.location)
    let status = url.searchParams.get('lists_status')
    if(status!=null){
        lists_ajax(status)
    }
    else{
        lists_ajax()
    }
})