const displayedImage = document.querySelector('.displayed-img')
const thumbBar = document.querySelector(".thumb-bar")
const button = document.querySelector("button")
const overlay = document.querySelector(".overlay")

for(i = 1; i <= 5; i++){
  // criar um elemento no html
  const newImage = document.createElement('img')
  newImage.setAttribute('src', 'images/pic'+ i + '.jpg')
  // adiciona a nova imagem no thumb-bar
  thumbBar.append(newImage)
  // troca a imagem principal
  newImage.onclick = function(e){
    displayedImage.src = e.target.src
  }
}

button.onclick = function(e){
  const btn = btn.getAttribute('class')
  if (btn === 'dark'){
    btn.setAttribute('class','light')
    btn.textContent = "Lighten"
    overlay.style.backgroundColor = "rgba(0,0,0,0.5)"
  } 
  else{
    btn.setAttribute('class','dark')
    btn.textContent = "Darken"
    overlay.style.backgroundColor = "rgba(0,0,0,0)"
  }
}
