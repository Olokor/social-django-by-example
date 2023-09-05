const siteUrl = '/127.0.0.1:8000/';
const styleUrl = siteUrl + '/static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// load css

var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href  = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link)

// load html
var body = document.getElementsByTagName('body')[0];
boxHtml = `
    <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Select an image to bookmark:</h1>
        <div class="images"></div>
    </div>
`

body.innerHTML +=boxHtml;

function bookmarkletletLunch(){
    bookmarklet = document.getElementById('bookmarklet')
    var image_found = bookmarklet.querySelector('.immages')

    // clear image found
    image_found.innerHTML = '';
    // bookmarklet display type
    bookmarklet.style.display = 'block'
    // close event
    bookmarklet.querySelector('#close')
        .addEventListener('click', function(){
        bookmarklet.style.display = 'none'
    });

}
bookmarkletletLunch();

// find image in DOM with minimum dimension

images = document.querySelector("img[src$='.jpeg'], img[src$='.jpg'], img[src$='.png']");
images.forEach(images => {
    if(images.naturalWidth >= minWidth && images.naturalHeight >= minHeight){
        var image_found = document.createElement('img');
        image_found.src = image.src;
        imagesFound.append(imagesFound)
    }
