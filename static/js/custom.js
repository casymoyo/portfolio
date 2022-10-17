// Active class 
$('.link-item').on('click', function () {
        
    $(this).addClass('active').siblings().removeClass('active');
    
});

// footer date
const d = document.getElementById('date')
let ft = new Date()
d.innerHTML = ft.getFullYear();

// const header = document.getElementById('links');
// const links = header.getElementsByClassName('link');
// for(var i = 0; i<links.length; i++){
//     links[i].addEventListener(
//         'click', function(){
//             var current = document.getElementsByClassName('active');
//             current[0].className = current[0].className.replace('active', '');
//             this.className += 'active';
//         }
//     )
// }
