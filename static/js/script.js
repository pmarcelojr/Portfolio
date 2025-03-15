// Abre e fecha menu lateral em modo mobile

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () => {
  menuMobile.classList.contains('bi-list')
    ? menuMobile.classList.replace('bi-list', 'bi-x')
    : menuMobile.classList.replace('bi-x', 'bi-list');
    body.classList.toggle('menu-nav-active');
});

// Fechar o menu quando clicar em algum item e muda o icone para list
const menuItems = document.querySelectorAll('.nav-item');

menuItems.forEach(item => {
  item.addEventListener('click', () => {
    if (body.classList.contains('menu-nav-active')) {
      body.classList.remove('menu-nav-active');
      menuMobile.classList.replace('bi-x', 'bi-list');
    }
  });
});

// Animar todos os itens da página que tiverem atributo data-anime
const itens = document.querySelectorAll('[data-anime]');

const animeScroll = () => {
  const windowTop = window.pageYOffset + (window.innerHeight * 3) / 4;

  itens.forEach(item => {
    if (windowTop > item.offsetTop) {
      item.classList.add('animate');
    } else {
      item.classList.remove('animate');
    }
  });
}

window.addEventListener('scroll', () => {
  animeScroll();
});
