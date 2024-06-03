document.addEventListener('DOMContentLoaded', () => {
  const isAuthenticated = document.getElementById('auth-status').getAttribute('data-authenticated') === 'True';

  document.querySelectorAll('.p_wl_icon').forEach(iconContainer => {
      iconContainer.addEventListener('click', function(event) {
          // Prevent the default link action and stop propagation
          event.preventDefault();
          event.stopPropagation();

          if (!isAuthenticated) {
              alert('Please log in to add items to your wishlist.');
              window.location.href = '/login/'; // Redirect to login page
              return;
          }

          const productId = iconContainer.getAttribute('data-product-id');
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

document.addEventListener('DOMContentLoaded', function () {
    // Get all wishlist icons
    const wishlistIcons = document.querySelectorAll('.wishlist-icon');

    // Add click event listener to each wishlist icon
    wishlistIcons.forEach(icon => {
        icon.addEventListener('click', function (event) {
            // Prevent the default action
            event.preventDefault();
            event.stopPropagation();

            // Get the product ID from the data attribute
            const productId = icon.closest('.p_wl_icon').dataset.productId;

            // Perform the wishlist action here (e.g., AJAX request to add/remove from wishlist)
            console.log(`Wishlist icon clicked for product ID: ${productId}`);
            // Add your AJAX request or other functionality here
        });
    });
});
