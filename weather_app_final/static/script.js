console.log('JavaScript is running!');
const weatherForm = document.getElementById('weather-form');
const latInput = document.getElementById('lat');
const lonInput = document.getElementById('lon');
const getLocationButton = document.getElementById('getLocationButton');

// Function to handle successful location retrieval
function handleLocation(position) {
  const { latitude, longitude } = position.coords;
  latInput.value = latitude;
  lonInput.value = longitude;
  // Optionally, submit the form automatically
   //weatherForm.submit();  // Uncomment to submit automatically
   weatherForm.submit();
 
}

// Function to handle location access denial or errors
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



// Handle form submission logic
weatherForm.addEventListener('submit', (event) => {
  // event.preventDefault(); // Prevent default form submission

  const lat = document.getElementById('lat').value;
  const lon = document.getElementById('lon').value;
  if (!lat || !lon) {
    alert('Please enter both latitude and longitude');
    return; // Exit the function if any field is empty
  }

  // You can add a success message or logic here after form validation (optional)
  alert('Form submitted with Latitude: ' + lat + ' and Longitude: ' + lon);
});

// Handle location button click (if button exists)
if (getLocationButton) {

  getLocationButton.addEventListener('click', () => {
    if (navigator.geolocation) {
  
      navigator.geolocation.getCurrentPosition(handleLocation, handleLocationError);
    } else {
      alert('Geolocation is not supported by this browser.');
    }
  });
}
