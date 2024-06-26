// document.getElementById('uploadForm').addEventListener('submit', function (event) {
//   event.preventDefault();
//   var formData = new FormData();
//   formData.append('image', document.getElementById('image').files[0]);

//   fetch('/upload', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.filepath) {
//         const beforeImage = document.getElementById('before-image');
//         beforeImage.src = data.filepath;
//         beforeImage.style.display = 'block';

//         const buttonsDiv = document.getElementById('buttons');
//         buttonsDiv.innerHTML = `
//               <button onclick="processImage('histogram', '${data.filepath}')">Equalize Histogram</button>
//               <button onclick="processImage('edge_detection', '${data.filepath}')">Edge Detection</button>
//               <button onclick="processImage('convolution', '${data.filepath}')">Apply Convolution</button>
//           `;
//       } else {
//         document.getElementById('result').innerText = data.error;
//       }
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//       document.getElementById('result').innerText = 'An error occurred.';
//     });
// });

// function processImage(endpoint, filepath) {
//   fetch(`/${endpoint}`, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ filepath: filepath }),
//   })
//     .then((response) => response.blob())
//     .then((blob) => {
//       var url = URL.createObjectURL(blob);
//       var img = document.getElementById('after-image');
//       img.src = url;
//       img.style.display = 'block';
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//       document.getElementById('result').innerText = 'An error occurred.';
//     });
// }

// document.getElementById('uploadForm').addEventListener('submit', function (event) {
//   event.preventDefault();
//   var formData = new FormData();
//   formData.append('image', document.getElementById('image').files[0]);

//   fetch('/upload', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.filepath) {
//         const beforeImage = document.getElementById('before-image');
//         beforeImage.src = data.filepath;
//         beforeImage.style.display = 'block';

//         const buttonsDiv = document.getElementById('buttons');
//         buttonsDiv.innerHTML = `
//               <button onclick="processImage('histogram', '${data.filepath}')">Equalize Histogram</button>
//               <button onclick="processImage('edge_detection', '${data.filepath}')">Edge Detection</button>
//               <button onclick="processImage('convolution', '${data.filepath}')">Apply Convolution</button>
//           `;
//       } else {
//         document.getElementById('result').innerText = data.error;
//       }
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//       document.getElementById('result').innerText = 'An error occurred.';
//     });
// });

// function processImage(endpoint, filepath) {
//   fetch(`/${endpoint}`, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ filepath: filepath }),
//   })
//     .then((response) => response.blob())
//     .then((blob) => {
//       var url = URL.createObjectURL(blob);
//       var img = document.getElementById('after-image');
//       img.src = url;
//       img.style.display = 'block';
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//       document.getElementById('result').innerText = 'An error occurred.';
//     });
// }

document.getElementById('uploadForm').addEventListener('submit', function (event) {
  event.preventDefault();
  var formData = new FormData();
  formData.append('image', document.getElementById('image').files[0]);

  fetch('/upload', {
    method: 'POST',
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.filepath) {
        const beforeImage = document.getElementById('before-image');
        console.log('Original image path:', data.filepath); // Debugging log
        beforeImage.src = data.filepath;
        beforeImage.style.display = 'block';

        const buttonsDiv = document.getElementById('buttons');
        buttonsDiv.innerHTML = `
              <button onclick="processImage('histogram', '${data.filepath}')">Equalize Histogram</button>
              <button onclick="processImage('edge_detection', '${data.filepath}')">Edge Detection</button>
              <button onclick="processImage('convolution', '${data.filepath}')">Apply Convolution</button>
          `;
      } else {
        document.getElementById('result').innerText = data.error;
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      document.getElementById('result').innerText = 'An error occurred.';
    });
});

function processImage(endpoint, filepath) {
  fetch(`/${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ filepath: filepath }),
  })
    .then((response) => response.blob())
    .then((blob) => {
      var url = URL.createObjectURL(blob);
      var img = document.getElementById('after-image');
      img.src = url;
      img.style.display = 'block';
    })
    .catch((error) => {
      console.error('Error:', error);
      document.getElementById('result').innerText = 'An error occurred.';
    });
}
