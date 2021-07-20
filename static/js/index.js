import * as THREE from 'https://unpkg.com/three@0.119.0/build/three.module.js'
import { OrbitControls } from 'https://unpkg.com/three@0.119.0/examples/jsm/controls/OrbitControls.js'


document.addEventListener("DOMContentLoaded", function() {


    const menuLinks = document.querySelectorAll('.header__nav-link[data-goto]');

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
            }
        }
    }

    // three js planet 

    const element = document.getElementById('mapTravelId');

    if (element) {
        const group = new THREE.Group();
    const scene = new THREE.Scene();
        scene.background = new THREE.Color( 0xffffff );

    const camera = new THREE.PerspectiveCamera(
        75,
        element.clientWidth/element.clientHeight,
        0.1,
        1000
    );

    let material = new THREE.ShaderMaterial({
        extensions: {
            derivatives: "#extension GL_OES_standard_derivatives : enable"
        },
        side: THREE.DoubleSide,
        uniforms: {
            time: { value: 0},
            resolution: { value: new THREE.Vector4() }
        },
        vertexShader:   document.getElementById('sphere-vertex-shader').textContent,
        fragmentShader: document.getElementById('sphere-fragment-shader').textContent
    })
    const renderer = new THREE.WebGL1Renderer(
        {
            antialias: true
        }
    )

    renderer.setSize(element.clientWidth,element.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    element.appendChild(renderer.domElement);
    let controller = new OrbitControls(camera, renderer.domElement);
controller.enableZoom = false;

// to disable rotation
controller.enableRotate = true;

// to disable pan
controller.enablePan = false;

    const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(1,30,30),
        new THREE.MeshBasicMaterial({
            // color: 0xff0000
            map: new THREE.TextureLoader().load('static/textures/globevector.png')
        })
    );
    camera.position.z = 3;
    // if (window.innerWidth <= 400){
    //     camera.position.z = 4;
    // }
    group.add(sphere);
    // group.position.set(0.2,0,0);


    let kazakhstanPin = new THREE.Mesh(
        new THREE.SphereBufferGeometry(0.02,20,20),
        new THREE.MeshBasicMaterial({
            color: 0xFF9156
        })
    )

    let englandPin = new THREE.Mesh(
        new THREE.SphereBufferGeometry(0.02,20,20),
        new THREE.MeshBasicMaterial({
            color: 0x5F67EC
        })
    )

    let usaPin = new THREE.Mesh(
        new THREE.SphereBufferGeometry(0.02,20,20),
        new THREE.MeshBasicMaterial({
            color: 0x4DCCFF
        })
    )


    group.add(kazakhstanPin);
    group.add(englandPin);
    group.add(usaPin);
    scene.add(group);


function convertCoordinate(h,w,element) {
    let phi   = (90-h) * (Math.PI/180);
    let theta = (w+180) * (Math.PI/180);

    let x = -(Math.sin(phi) * Math.cos(theta));
    let z = (Math.sin(phi) * Math.sin(theta));
    let y = (Math.cos(phi));
    element.position.set(x,y,z);

    return {
        x,y,z
    }
}

const kaz = convertCoordinate(48.019573, 66.923684, kazakhstanPin);
const eng = convertCoordinate(51.509865, -0.118092, englandPin);
const usa = convertCoordinate(37.09024,-95.712891, usaPin);

function getCurve(p1,p2) {
    let v1 = new THREE.Vector3(p1.x,p1.y,p1.z);
    let v2 = new THREE.Vector3(p2.x,p2.y,p2.z);
    let points = [];
    for (let i = 0; i<=20; i++) {
        let p = new THREE.Vector3().lerpVectors(v1, v2, i/20);
        p.normalize();
        p.multiplyScalar(1+0.1*Math.sin(Math.PI*i/20));
        points.push(p);
        
    }

    let curve = new THREE.CatmullRomCurve3(points);
    const geometry = new THREE.TubeGeometry(curve, 20, 0.01, 8, false);
    const materialt = new THREE.MeshBasicMaterial({color: 0x0000ff});
    const mesh = new THREE.Mesh(geometry,material);
    group.add(mesh);

    return points;
}

getCurve(kaz,eng);
getCurve(kaz,usa);
getCurve(eng,usa);



let time = 0;
function animate(){
    time += 0.05;
    material.uniforms.time.value = time;
    requestAnimationFrame(animate);
    group.rotation.y += 0.001;
    renderer.render(scene,camera);
}
animate();
    }

    

// three js planet end


    let button = document.getElementById('responsiveBtn');
    let links = document.querySelectorAll('.header__nav-item');
    let closeBtn = document.querySelector('.header__nav-close');
    let header = document.querySelector('.header');
    let headerNav = document.querySelector('.header__nav');
    button.addEventListener('click', ()=>{
        links.forEach(link=>{
            link.style.display = 'block';
            headerNav.classList.add('header__nav--active');
        })
        closeBtn.style.display = 'block';
    })
    closeBtn.addEventListener('click', ()=>{
        links.forEach(link=>{
            link.style.display = 'none';
            headerNav.classList.remove('header__nav--active');
            closeBtn.style.display = 'none';
        })
    })


    // Slider

    const swiper = new Swiper('.swiper-container', {
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



});










