function predictImage() {
    var fileInput = document.getElementById('imageUpload');
    var file = fileInput.files[0];
    var reader = new FileReader();
    
    if (!file) {
        alert("Please select an image first");
        return;
    }
    
    // Show loading spinner
    document.getElementById('loading').style.display = 'block';
    document.getElementById('result').style.display = 'none';
    
    reader.onload = function(e) {
        var base64Image = e.target.result.split(',')[1];
        
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image: base64Image
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide loading spinner
            document.getElementById('loading').style.display = 'none';
            document.getElementById('result').style.display = 'block';
            
            if (data[0].error) {
                document.getElementById('result').innerHTML = 'Error: ' + data[0].error;
            } else {
                document.getElementById('result').innerHTML = 'Prediction: ' + data[0].image;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loading').style.display = 'none';
            document.getElementById('result').style.display = 'block';
            document.getElementById('result').innerHTML = 'Error: ' + error.message;
        });
    };
    
    reader.readAsDataURL(file);
}
