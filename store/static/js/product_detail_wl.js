// Add to wishlist
document.addEventListener('DOMContentLoaded', () => {
    const isAuthenticated = document.getElementById('auth-status').getAttribute('data-authenticated') === 'True';

    document.querySelectorAll('.button2').forEach(button => {
        button.addEventListener('click', function(event) {
            // Prevent the default button action
            event.preventDefault();
            event.stopPropagation();

            if (!isAuthenticated) {
                alert('Please log in to add items to your wishlist.');
                window.location.href = '/login/'; // Redirect to login page
                return;
            }

            const productId = this.getAttribute('data-product-id');
            fetch(`/add_to_wishlist/${productId}/`)
                .then(response => {
                    if (response.ok) {
                        alert('Product added to wishlist!');
                    } else {
                        alert('Failed to add product to wishlist!');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while adding the product to the wishlist!');
                });
        });
    });
});
