const cross = document.querySelector('.cross');
const nav = document.querySelector('.nav');
const bars = document.querySelector('.fa-bars');
const header = document.querySelector('.header');
const body = document.querySelector('body');
const loader = document.querySelector('.loading')

bars.addEventListener('click', () => {
    nav.classList.add('active');
    body.classList.add('scrolldisable');
})

cross.addEventListener('click', () => {
    nav.classList.remove('active');
    body.classList.remove('scrolldisable');
})

window.addEventListener('scroll', () => {
    window.scrollY > 100 ? header.classList.add('sticky') : header.classList.remove('sticky');
})

window.addEventListener('load',() => {
    loader.classList.add('hidden');
})