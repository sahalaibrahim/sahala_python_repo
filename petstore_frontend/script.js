document.addEventListener('DOMContentLoaded', function() {
    if (document.URL.includes('index.html'))
    {
    const petListContainer = document.getElementById('petList');
    const findPetByStatusBtn = document.getElementById('findPetByStatusBtn');
    const findPetByIdBtn = document.getElementById('findPetByIdBtn');
    const deletePetBtn = document.getElementById('deletePetBtn');
    findPetByStatusBtn.addEventListener('click', findPetByStatus);
    findPetByIdBtn.addEventListener('click', findPetById);
    deletePetBtn.addEventListener('click', deletePet);
    function findPetByStatus()
     {
        const status = prompt("Enter the status you want to search for (e.g., available, pending, sold):");

        fetch(`https://petstore.swagger.io/v2/pet/findByStatus?status=${status}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to find pets by status');
            }
            return response.json();
        })
        .then(data => {
            
            const petInfo = document.createElement('div');
            petInfo.textContent = `Pets found by status: ${JSON.stringify(data)}`;
            petListContainer.appendChild(petInfo);
        })
        .catch(error => {
            console.error('Error finding pets by status:', error);
            
        });

        console.log('Find Pet by Status button clicked');
    }

    
    function findPetById() {
        const petId = parseInt(prompt("Enter the ID of the pet you want to find:"));

        if (isNaN(petId)) {
            console.error('Invalid pet ID');
            return;
        }

        fetch(`https://petstore.swagger.io/v2/pet/${petId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to find pet by ID');
            }
            return response.json();
        })
        .then(data => {
            
            const petInfo = document.createElement('div');
            petInfo.textContent = `Pet found by ID: ${JSON.stringify(data)}`;
            petListContainer.appendChild(petInfo);
        })
        .catch(error => {
            console.error('Error finding pet by ID:', error);
            
        });

        console.log('Find Pet by ID button clicked');
    }
    
    function deletePet() {
        const petId = parseInt(prompt("Enter the ID of the pet you want to delete:"));

        if (isNaN(petId)) {
            console.error('Invalid pet ID');
            return;
        }

        fetch(`https://petstore.swagger.io/v2/pet/${petId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to delete pet');
            }
            console.log('Pet deleted successfully');
            
        })
        .catch(error => {
            console.error('Error deleting pet:', error);
            
        });

        console.log('Delete Pet button clicked');
    }
    }
    else if (document.URL.includes('post.html')) {
        const petListContainer2 = document.getElementById('petList2');
        const submitButton = document.getElementById('addPetBtn');
        submitButton.addEventListener('click', getData);
           function getData()
           {
            const id = parseInt(document.getElementById('petId').value);
            const category = {
                id: parseInt(document.getElementById('categoryId').value), 
                name: document.getElementById('categoryName').value
            };
            const name = document.getElementById('petName').value;
            const photoUrl = document.getElementById('photoUrl').value;
            const tagId = parseInt(document.getElementById('tagId').value); 
            const tagName = document.getElementById('tagName').value;
            const status = document.getElementById('status').value;
            
    
            const newPetData = {
                id: id,
                category: category,
                name: name,
                photoUrls: [photoUrl],
                tags: [{ id: tagId, name: tagName }],
                status: status
            };
            

        fetch(`https://petstore.swagger.io/v2/pet`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newPetData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to add pet');
            }
            return response.json();
        })
        .then(data => {
            
            const petInfo = document.createElement('div');
            petInfo.textContent = `Added Pet: ${data.name}, Status: ${data.status}`;
            petListContainer2.appendChild(petInfo);
        })
        .catch(error => {
            console.error('Error adding pet:', error);
            
        });

        console.log('Add Pet button clicked');
    }

        
        
    }
    else if (document.URL.includes('update.html')){
        const updatePetBtn = document.getElementById('updatepetbtn');
        updatePetBtn.addEventListener('click', updatePet);
    function updatePet() {
        
        const petId = parseInt(document.getElementById('updatePetId').value);
        
        const updatedName = document.getElementById('updatePetName').value;
        const updatedCategory = {
            id: parseInt(document.getElementById('updateCategoryId').value),
            name: document.getElementById('updateCategoryName').value
        };
        const updatedPhotoUrl = document.getElementById('updatePhotoUrl').value;
        const updatedTagId = parseInt(document.getElementById('updateTagId').value);
        const updatedTagName = document.getElementById('updateTagName').value;
        const updatedStatus = document.getElementById('updateStatus').value;
    
        
        const updatedPetData = {
            id: petId,
            name: updatedName,
            category: updatedCategory,
            photoUrls: [updatedPhotoUrl],
            tags: [{ id: updatedTagId, name: updatedTagName }],
            status: updatedStatus
        };
    
        
        fetch(`https://petstore.swagger.io/v2/pet`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedPetData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update pet');
            }
            return response.json();
        })
        .then(data => {
            
            const petInfo = document.createElement('div');
            petInfo.textContent = `Updated Pet: ${data.name}, Status: ${data.status}`;
            petListContainer.appendChild(petInfo);
        })
        .catch(error => {
            console.error('Error updating pet:', error);
            
        });
    
        console.log('Update Pet button clicked');
    }
    }

    
    
    
    

    
    
});
