

 document.getElementById('openSidebarIcon').addEventListener('click', showSidebar);
  function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
  }
  function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
  }




//   function hideSidebar(){
//     const sidebar = document.querySelector('.sidebar');
//     if (window.innerWidth <= 768) { // Check if window width is less than or equal to 768px (Bootstrap's mobile breakpoint)
//         sidebar.style.display = 'none';
//     }
// }

// function showSidebar(){
//     const sidebar = document.querySelector('.sidebar');
//     if (window.innerWidth <= 768) { // Check if window width is less than or equal to 768px (Bootstrap's mobile breakpoint)
//         sidebar.style.display = 'flex';
//     }
// }

// document.getElementById('openSidebarIcon').addEventListener('click', function() {
//     showSidebar(); // Always show sidebar when icon is clicked
// });

// // Call hideSidebar on window resize to ensure sidebar is hidden on larger screens
// window.addEventListener('resize', hideSidebar);
