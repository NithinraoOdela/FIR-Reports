
// to save form data into the local storage.
function savecache() {
  const formEl = document.getElementById("complaint-form");
  const formData = new FormData(formEl); 
  const allData = formData.getAll();
  const prev = JSON.parse(localStorage.getItem('cache')) || [];
  prev.push(allData);
  localStorage.setItem('cache', JSON.stringify(prev));

  
}

//popup
const popupButton = document.getElementById('popupButton');
const popup = document.getElementById('popup');
