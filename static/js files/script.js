
/* Toggle mobile menu 
var toggleButton = document.querySelector('.toggle');
var navbarLinks = document.querySelector('.nav-item');

toggleButton.addEventListener('click', function() {
   navbarLinks.classList.toggle('showmenu');
});  */

function classToggle() {
    const navs = document.querySelectorAll('.nav-item')
    
    navs.forEach(nav => nav.classList.toggle('show'));
  }
  
document.querySelector('.toggle')
.addEventListener('click', classToggle);