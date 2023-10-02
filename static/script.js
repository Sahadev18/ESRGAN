function displayImage() {
  // Create an image element
  var img = document.createElement('img');

  // Set the image source
  img.src = './static/SR.jpg';  // Replace with the actual path to your image

  // Set any additional attributes you need (e.g., width, height)
  img.setAttribute('width', '200');

  // Get the container div to display the image
  var imageContainer = document.getElementById('imageContainer');

  // Clear previous content in the container
  imageContainer.innerHTML = '';

  // Append the image to the container
  imageContainer.appendChild(img);
}
