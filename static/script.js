

const onSubmit = async () => {

    var imagesInput = document.getElementById('imagesInput');
    var output = document.getElementById('output');
    var formData = new FormData();
    for (const file of imagesInput.files) { // new for loop adds all files to images list
        formData.append('images', file);
      }
    
    
    req= await fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    data=await req.json();
    if(data.status==200){
        output.innerText=data["disease"]
        
    }
}
      

      

 
  
    
