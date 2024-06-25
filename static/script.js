document.getElementById('upload-form').onsubmit = async function (event) {
  event.preventDefault();
  const formData = new FormData();
  const imageFile = document.getElementById('image-input').files[0];
  formData.append('image', imageFile);

  const response = await fetch('/upload', {
    method: 'POST',
    body: formData,
  });
  const result = await response.json();
  if (result.filepath) {
    document.getElementById('image-container').innerHTML = `<img src="${result.filepath}" alt="Uploaded Image">`;
  }
};

document.getElementById('histogram-btn').onclick = async function () {
  const imageSrc = document.querySelector('#image-container img').src;
  const response = await fetch('/histogram', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ filepath: imageSrc }),
  });
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  document.getElementById('image-container').innerHTML = `<img src="${url}" alt="Histogram Equalized Image">`;
};

document.getElementById('edge-btn').onclick = async function () {
  const imageSrc = document.querySelector('#image-container img').src;
  const response = await fetch('/edge_detection', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ filepath: imageSrc }),
  });
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  document.getElementById('image-container').innerHTML = `<img src="${url}" alt="Edge Detected Image">`;
};

document.getElementById('convolution-btn').onclick = async function () {
  const imageSrc = document.querySelector('#image-container img').src;
  const response = await fetch('/convolution', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ filepath: imageSrc }),
  });
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  document.getElementById('image-container').innerHTML = `<img src="${url}" alt="Convoluted Image">`;
};
