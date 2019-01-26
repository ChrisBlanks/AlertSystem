//Define this in your script before: var x = document.getElementById(id);
function getLocation() {

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
	
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude; 
  
  x.value = "Latitude: " + position.coords.latitude + "\nLongitude: " + position.coords.longitude;
}