function isInView(element, offset) {
    var offset = offset || 0;
    var rect = element.getBoundingClientRect();
    return rect.top >= 0 && rect.bottom <= window.innerHeight;
}

function selectVideo(container) {
    for (var i = 0; i < container.childNodes.length; i++){
        if (container.childNodes[i].localName == "video"){
            return container.childNodes[i];
        }
    }
    return null;
}

var visible = new Event("inView");
var notVisible = new Event("outView");
var videos = document.querySelectorAll("video");
var postsContainer = document.querySelector(".container");
var videoContainers = document.querySelectorAll(".videoContainer");
var miniView = document.getElementById("miniView");
var closeMini = document.getElementById("closeMiniVideo");
var containers = {};
var miniVideo = null;

//Check if videos are in or out of view
document.addEventListener("scroll", function(){
    Array.prototype.forEach.call(videoContainers, function(container){
        if (isInView(container)){
            container.dispatchEvent(visible);
        } else {
            container.dispatchEvent(notVisible);
        }
    });
}, false);

//Event triggered when video is inside of view
Array.prototype.forEach.call(videoContainers, function(container){
    container.addEventListener("inView", function(){

        //if miniVideo is this, remove minivideo
        if (miniVideo) {
            if (containers[miniVideo.src] == container) {
                miniView.classList.remove("active");

                //place video back into correct container
                containers[miniVideo.src].appendChild(miniVideo);
                miniVideo.play();
                miniVideo = null;
            }
        }
    }, false);
});

//Event triggered when video is out of view
Array.prototype.forEach.call(videoContainers, function(container){
    container.addEventListener("outView", function(){

        var video = selectVideo(container);

        //if this video is playing and miniVideo is not this video
        if (video && !video.paused && miniVideo != video ) {
            var parent = video.parentElement;

            //if miniVideo contains another video
            if (miniVideo != null) {

                //pause other video
                miniVideo.pause();
                containers[miniVideo.src].appendChild(miniVideo);
                containers[miniVideo.src].removeAttribute("style");
            }

            //make this miniVideo
            miniVideo = video;

            //move video out of container and into miniview container
            parent.style.width = video.offsetWidth + "px";
            parent.style.height = video.offsetHeight + "px";
            parent.setAttribute("data-src", video.src);
            video.pause();
            miniView.classList.add("active");
            containers[video.src] = parent;

            //FIXME: this moves the node from original place to miniView, this is ideal
            //          ensure that it can be returned to the original position
            miniView.appendChild(video);
            miniVideo.play();
        }
    }, false);
});

closeMini.addEventListener('click', function(){

    //if miniVideo is this, remove minivideo
    if (miniVideo) {
        miniView.classList.remove("active");

        //place video back into correct container
        containers[miniVideo.src].appendChild(miniVideo);
        miniVideo = null;
    }
});

//Update miniView area to be 20px from post container
miniView.style.left = (postsContainer.getBoundingClientRect().right + 20) + "px";
miniView.style.right = "auto";

window.addEventListener("resize", function(){
    miniView.style.left = (postsContainer.getBoundingClientRect().right + 20) + "px";
}, false);