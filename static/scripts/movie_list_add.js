document.querySelectorAll('button.add_list_item').forEach(function(element){
    element.addEventListener('click',function(){
        ajax_add_in_list(element.value)
    })
})

let movie_id = document.querySelector("input.hiden_mv_id").value
let csrf_token = document.querySelector("input[name='csrfmiddlewaretoken']").value
function ajax_add_in_list(value){
    fetch(`/add_to_list/`,
        {
            method:'POST',
            headers: {
                "X-CSRFToken":csrf_token,
                "Content-Type": "application/json"
              },
            body: JSON.stringify({ 'film_status': value, 'movie_id':movie_id }),
        })
    

    .then(function(response){
        if(response.ok){
            return response.json()
        }
        else{
            throw new Error(`Error status: ${response.status}`)
        }
    })

    .then(function(data){
        console.log(data)
        let list_status_value = data['list_status'].toString();
        document.querySelector("button.add_list_button").innerText = list_status_value.charAt(0).toUpperCase() + list_status_value.slice(1)
        location.reload() 
        
    })

    .catch(function(error){
        console.log(`Error: ${error.message}`)
    })

}