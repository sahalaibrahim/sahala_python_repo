
const weatherForm = document.getElementById('weather-form');
const latInput = document.getElementById('lat');
const lonInput = document.getElementById('lon');
const getLocationButton = document.getElementById('getLocationButton');


function handleLocation(position) {
  const { latitude, longitude } = position.coords;
  latInput.value = latitude;
  lonInput.value = longitude;
  weatherForm.submit();
 
}


function handleLocationError(error) {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      alert('User denied location access.');
      break;
    case error.POSITION_UNAVAILABLE:
      alert('Location information is unavailable.');
      break;
    case error.TIMEOUT:
      alert('Location retrieval timed out.');
      break;
    default:
      alert('An error occurred while retrieving location.');
  }
}




weatherForm.addEventListener('submit', (event) => {


  const lat = document.getElementById('lat').value;
  const lon = document.getElementById('lon').value;
  if (!lat || !lon) {
    alert('Please enter both latitude and longitude');
    return; 
  }

  
  alert('Form submitted with Latitude: ' + lat + ' and Longitude: ' + lon);
});


if (getLocationButton) {

  getLocationButton.addEventListener('click', () => {
    if (navigator.geolocation) {
  
      navigator.geolocation.getCurrentPosition(handleLocation, handleLocationError);
    } else {
      alert('Geolocation is not supported by this browser.');
    }
  });
}
