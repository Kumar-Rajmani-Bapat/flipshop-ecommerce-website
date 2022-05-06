function init() {

}

function changeImage(event) {
   var mainImage = document.getElementById('mainImage')
   mainImage.src = event.target.src
}
window.onload = init;