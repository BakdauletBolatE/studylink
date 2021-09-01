
    const linksL = document.querySelectorAll('.header__nav-link');
    document.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            document.querySelector('.header').classList.add('header--shadow');
            if (linksL.length>0){
                linksL.forEach(link=>{
                    link.classList.add('header__nav-link--shadow');
                })
            }
            
        }
        else{
            document.querySelector('.header').classList.remove('header--shadow');
            if (linksL.length>0){
                linksL.forEach(link=>{
                    link.classList.remove('header__nav-link--shadow');
                })
            }
        }
    })
    const menuLinks = document.querySelectorAll('._goto-links[data-goto]');

    if (menuLinks.length > 0) {
        menuLinks.forEach(link => {
            link.addEventListener('click', onMenuLinkClick);

        })

        function onMenuLinkClick(e){
            e.preventDefault();
            const menuLink = e.target;
            if (menuLink.dataset.goto && document.querySelector(menuLink.dataset.goto)) {
                const gotoBlock = document.querySelector(menuLink.dataset.goto);
                const gotoBlockValue = gotoBlock.getBoundingClientRect().top + pageYOffset - document.querySelector('.header').offsetHeight - 30; 
                window.scrollTo(
                    {
                        top:gotoBlockValue,
                        behavior: 'smooth'
                    }
                )
                if (mobileMenu.classList.contains('mobileMenu--opened')){
                    header.classList.remove('header--closed');
                    wrapper.classList.remove('body--block');
                    mobileMenu.classList.remove('mobileMenu--opened');
                }
            }
        }
    }

    


    let button = document.getElementById('responsiveBtn');
    let header = document.querySelector('.header');
    let wrapper = document.querySelector('body');
    let mobileMenu = document.querySelector('.mobileMenu');
    button.addEventListener('click', ()=>{
        header.classList.toggle('header--closed');
        header.classList.remove('header--shadow');
        wrapper.classList.toggle('body--block');
        mobileMenu.classList.toggle('mobileMenu--opened');
    })
    

    
    const swiper = new Swiper('.main-slide', {
        // Optional parameters
        direction: 'horizontal',
        loop: true,
        
        breakpoints: {
            // when window width is >= 320px
            320: {
              slidesPerView: 1,
            },
            // when window width is >= 480px
            480: {
              slidesPerView: 1,
            },
            // when window width is >= 640px
            640: {
              slidesPerView: 2,
            spaceBetween: 20
            },
            1000: {
                slidesPerView: 3,
            spaceBetween: 20
            }
          },
        // // If we need pagination
        pagination: {
          el: '.swiper-pagination',
        },
      
        // // Navigation arrows
        // navigation: {
        //   nextEl: '.swiper-button-next',
        //   prevEl: '.swiper-button-prev',
        // },
      
        // And if we need scrollbar
        scrollbar: {
          el: '.swiper-scrollbar',
        },
      });

      const swiper2 = new Swiper('.slide-effects', {
        direction: 'horizontal',
        loop: true,
        breakpoints: {
            // when window width is >= 320px
            320: {
                slidesPerView: 2,
            },
            // when window width is >= 480px
            480: {
                slidesPerView: 2,
            },
            // when window width is >= 640px
            640: {
              slidesPerView: 2,
            },
            1000: {
                slidesPerView: 3,
                spaceBetween: 30,
            }
          },
        spaceBetween: 30,
        centeredSlides: true,
        
    })

    var maskPhoneNumber = document.getElementById('phone-mask');
    var maskOptions = {
            mask: '+7\\(000)-000-00-00'
    };
    var mask = IMask(maskPhoneNumber, maskOptions);
    
    let maskMaskInput = document.getElementById('input-edu');

    let eduMask = IMask(maskMaskInput, maskOptions)

    maskPhoneNumber.addEventListener('input', ()=>{
        console.log(mask);
    })










