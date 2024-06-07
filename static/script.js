document.addEventListener('DOMContentLoaded', function() {
    const addProductButton = document.getElementById('add-product');
    const productInputContainer = document.querySelector('.product-input-container');

    addProductButton.addEventListener('click', function() {
        const productInputRow = document.createElement('div');
        productInputRow.classList.add('product-input-row');
        productInputRow.innerHTML = `
            <textarea class="product-input" name="product_addresses" rows="1" placeholder="Enter product address..."></textarea>
            <button type="button" class="remove-product">-</button>
        `;
        productInputContainer.appendChild(productInputRow);

        
        productInputRow.querySelector('.remove-product').addEventListener('click', function() {
            productInputRow.remove();
        });
    });

    
    document.querySelectorAll('.remove-product').forEach(button => {
        button.addEventListener('click', function() {
            button.parentElement.remove();
        });
    });

    
    const form = document.getElementById('product-form');
    
   

    document.addEventListener('DOMContentLoaded', function() {
        const form = document.getElementById('product-form');
    
        form.addEventListener('submit', function(event) {
            event.preventDefault(); 
    
            const formData = new FormData(this);  
    
            fetch('/compare', {  
                method: 'POST',
                body: formData  
            })
            .then(response => response.json()) 
            .then(data => {
                print(data.result)
                console.log(data)


                
                const results = document.getElementById('comparison-results');
                results.innerHTML = `
                    <h3>Comparison Results:</h3>
                    <p>Product Addresses: ${data.product_addresses.join(', ')}</p>
                    <p>User Requirements: ${data.user_requirements}</p>
                    <p>Result: ${data.result}</p>
                `;
            })
            .catch(error => {
                console.error('Error:', error);
                const results = document.getElementById('comparison-results');
                results.innerHTML = `<p>An error occurred: ${error}</p>`;  
            });
        });
    });
    
});
