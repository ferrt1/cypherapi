document.addEventListener('DOMContentLoaded', function() {
  const menuIcon = document.getElementById('menu-icon');
  const nav = document.getElementById('nav');
  const overlay = document.getElementById('overlay');

  menuIcon.addEventListener('click', function() {
    nav.classList.toggle('open');
    setTimeout(function() {
      overlay.classList.toggle('open');
    }, 300); 
  });

  overlay.addEventListener('click', function() {
    nav.classList.remove('open');
    overlay.classList.remove('open');
  });
});