// $('.remove-btn').click(function() {
//     const productId = $(this).data('product-id');
//     const size = $(this).data('size');
//     const cartItemId = $(this).data('cart-item-id');
//     const csrftoken = getCookie('csrftoken'); // Assuming you already have the getCookie function

//     $.ajax({
//         url: '/remove-from-cart/', // URL to your Django view that handles removal
//         type: 'POST',
//         data: {
//             'product_id': productId,
//             'size': size,
//             'cart_item_id': cartItemId,
//             csrfmiddlewaretoken: csrftoken // CSRF token, required for POST requests in Django
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 // Remove the product div
//                 $(`div[data-product-id="${productId}"][data-size="${size}"]`).parent().remove();

//                 // Update the order summary values
//                 $('#cart-subtotal').text('Rs. ' + response.new_subtotal);
//                 $('#cart-tax').text('Rs. ' + response.new_tax);
//                 $('#cart-total').text('Rs. ' + response.new_total);

//                 // Update the shopping cart HTML dynamically
//                 const cartHtml = '';
//                 $.each(response.cart_items, function(index, item) {
//                     cartHtml += `
//                         <div class="product">
//                             <div class="pro_detail">
//                                 <div class="product-image">
//                                     <img src="${item.product.image_url}">
//                                 </div>
//                                 <div class="product-details">
//                                     <div class="product-title">${item.product.name}</div>
//                                 </div>
//                             </div>
//                             <div class="product-size">
//                                 <span class="size-word">Size: </span>
//                                 <div class="size">${item.size}</div>
//                             </div>
//                             <div class="product-price">
//                                 <span class="price-word">Price: </span>
//                                 <div class="price">Rs. ${item.price}</div>
//                             </div>
//                             <div class="product-quantity">
//                                 <input type="number" class="form-control w-25 quantity" value="${item.quantity}" min="1">
//                             </div>
//                             <div class="product-removal">
//                                 <button class="remove-btn" data-product-id="${item.product.id}" data-size="${item.size}" data-cart-item-id="${item.id}"><i class="fa-regular fa-trash-can"></i></button>
//                             </div>
//                         </div>
//                     `;
//                 });
//                 $('#shopping-cart').html(cartHtml);

//                 // Optional: Display a message or update other elements
//                 alert("Item removed successfully!");
//             } else {
//                 alert("Error removing item from cart.");
//             }
//         },
//         error: function(xhr, status, error) {
//             // Handle any errors here
//             alert("Error removing item from cart.");
//         }
//     });












// $('.remove-btn').click(function() {
//     const productId = $(this).data('product-id');
//     const size = $(this).data('size');
//     const csrftoken = getCookie('csrftoken'); // Assuming you already have the getCookie function

//     $.ajax({
//         url: '/remove-from-cart/', // URL to your Django view that handles removal
//         type: 'POST',
//         data: {
//             'product_id': productId,
//             'size': size,
//             csrfmiddlewaretoken: csrftoken // CSRF token, required for POST requests in Django
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 // Remove the product div
//                 $(`div[data-product-id="${productId}"][data-size="${size}"]`).parent().remove();

//                 // Update the order summary values
//                 $('#cart-subtotal').text('Rs. ' + response.new_subtotal);
//                 $('#cart-tax').text('Rs. ' + response.new_tax);
//                 $('#cart-total').text('Rs. ' + response.new_total);

//                 // Update the shopping cart HTML dynamically
//                 const cartHtml = '';
//                 $.each(response.cart_items, function(index, item) {
//                     cartHtml += `
//                         <div class="product">
//                             <div class="pro_detail">
//                                 <div class="product-image">
//                                     <img src="${item.product.image_url}">
//                                 </div>
//                                 <div class="product-details">
//                                     <div class="product-title">${item.product.name}</div>
//                                 </div>
//                             </div>
//                             <div class="product-size">
//                                 <span class="size-word">Size: </span>
//                                 <div class="size">${item.size}</div>
//                             </div>
//                             <div class="product-price">
//                                 <span class="price-word">Price: </span>
//                                 <div class="price">Rs. ${item.price}</div>
//                             </div>
//                             <div class="product-quantity">
//                                 <input type="number" class="form-control w-25 quantity" value="${item.quantity}" min="1">
//                             </div>
//                             <div class="product-removal">
//                                 <button class="remove-btn" data-product-id="${item.product.id}" data-size="${item.size}"><i class="fa-regular fa-trash-can"></i></button>
//                             </div>
//                         </div>
//                     `;
//                 });
//                 $('#shopping-cart').html(cartHtml);

//                 // Optional: Display a message or update other elements
//                 alert("Item removed successfully!");
//             } else {
//                 alert("Error removing item from cart.");
//             }
//         },
//         error: function(xhr, status, error) {
//             // Handle any errors here
//             alert("Error removing item from cart.");
//         }
//     });
// });








// $('.remove-btn').click(function() {
//     const productId = $(this).data('product-id');
//     const size = $(this).data('size');
//     const csrftoken = getCookie('csrftoken'); // Assuming you already have the getCookie function

//     $.ajax({
//         url: '/remove-from-cart/', // URL to your Django view that handles removal
//         type: 'POST',
//         data: {
//             'product_id': productId,
//             'size': size,
//             csrfmiddlewaretoken: csrftoken // CSRF token, required for POST requests in Django
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 // Remove the product div
//                 $(`div[data-product-id="${productId}"][data-size="${size}"]`).parent().remove();

//                 // Update the order summary values
//                 $('#cart-subtotal').text('Rs. ' + response.new_subtotal);
//                 $('#cart-tax').text('Rs. ' + response.new_tax);
//                 $('#cart-total').text('Rs. ' + response.new_total);

//                 // Optional: Display a message or update other elements
//                 alert("Item removed successfully!");
//             } else {
//                 alert("Error removing item from cart.");
//             }
//         },
//         error: function(xhr, status, error) {
//             // Handle any errors here
//             alert("Error removing item from cart.");
//         }
//     });
// });

