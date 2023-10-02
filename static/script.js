function displayImage() {
  // Create an image element
  var img = document.createElement('img');

  // Set the image source
  img.src = './static/SR.jpg';  // Replace with the actual path to your image

  // Set any additional attributes you need (e.g., width, height)
  img.setAttribute('width', '200');

  // Create a download button
  var downloadBtn = document.createElement('a');
  downloadBtn.href = './static/SR.jpg';  // Replace with the actual path to your image
  downloadBtn.download = 'SR.jpg';  // Specify the desired download filename
  downloadBtn.innerText = 'Download Image';

  // Get the container div to display the image and the download button
  var imageContainer = document.getElementById('imageContainer');

  // Clear previous content in the container
  imageContainer.innerHTML = '';

  // Append the image and download button to the container
  imageContainer.appendChild(img);
  imageContainer.appendChild(downloadBtn);
}
