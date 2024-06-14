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

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const targetID = this.getAttribute('href').substring(1);
    const targetElement = document.getElementById(targetID);

    if (targetElement) {
      const offsetTop = targetElement.offsetTop;

      window.scrollTo({
        top: offsetTop - 0, // Ajusta el -0 si necesitas un desplazamiento más fino
        behavior: 'smooth'
      });
    }
  });
});
