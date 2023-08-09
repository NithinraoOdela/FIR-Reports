// trigger_func to search input string 
function trigger_func()
{
       
            var searchInput = document.getElementById("searchInput");
            var searchButton = document.getElementById("searchButton");
            var table = document.querySelector("table");
        
            var searchTerm = searchInput.value.trim();
            let cases = document.getElementsByClassName('case_element');
           
            Array.from(cases).forEach(ele => {   // Iterating through each element in the cases collection.
                if(ele.firstElementChild.innerText === searchTerm){
                    ele.classList.add('changeBackground')
                }
                else{
                    ele.classList.remove('changeBackground');
                }
            });
}

