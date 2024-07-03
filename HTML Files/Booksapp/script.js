var popupoverlay=document.querySelector(".popup-overlay")
var popupbox=document.querySelector(".popup-box")
var addbutton=document.getElementById("add-popup")

addbutton.addEventListener("click",function(){
    popupoverlay.style.display="block"
    popupbox.style.display="block"
})

function can(event){
    event.preventDefault()
    popupbox.style.display="none";
    popupoverlay.style.display="none";
}

var addcontainer=document.querySelector(".container")
var addbook=document.getElementById("add-book")
var booktitle=document.getElementById("book-title")
var bookauthor=document.getElementById("book-author")
var shortdesc=document.getElementById("book-desc")

addbook.addEventListener("click",function(event){
    event.preventDefault()
    var div=document.createElement("div")
    div.setAttribute('class','book-container')
    div.innerHTML=`<h2>${booktitle.value}</h2>
    <h3>${bookauthor.value}</h3>
    <p>${shortdesc.value}</p>
    <button onclick="delbook(event)">Delete</button>`
    addcontainer.append(div)
    popupbox.style.display="none";
    popupoverlay.style.display="none";

})

function delbook(event){
    event.target.parentElement.remove()
}
