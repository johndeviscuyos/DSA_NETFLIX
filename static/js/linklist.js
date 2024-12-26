document.addEventListener('DOMContentLoaded', function () {
  document.body.classList.add('fade-in');

  const links = document.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      document.body.classList.remove('fade-in');
      setTimeout(() => {
        window.location.href = this.href;
      }, 500);
    });
  });
});