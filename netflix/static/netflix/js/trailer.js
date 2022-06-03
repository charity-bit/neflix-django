// const video_key = 
// console.log(video_key.textContent)


var tag = document.createElement('script')
tag.src = "https://www.youtube.com/player_api"

var firstScriptTag = document.getElementsByTagName('script')[0]

firstScriptTag.parentNode.insertBefore(tag,firstScriptTag)


var player;

function onYouTubeIframeAPIReady(){
    player = new YT.Player('player',{
        height: '720',
        width: '1280',
        videoId: document.getElementById('video_key').textContent,
        controls:0,
        enablejsapi:1,
        origin:'http://localhost:8000/',
        playerVars: {
          'playsinline': 1
        },
        events: {
          'onReady': onPlayerReady,
          'onStateChange': onPlayerStateChange
        }

    })
}


function onPlayerReady(event){
    event.target.playVideo();
}


var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
      done = true;
    }
  }
  function stopVideo() {
    player.stopVideo();
}

window.addEventListener("load", (event) => {
  player.stopVideo();
});

const playTrailer = document.querySelector('.banner__button')
const stopTrailer = document.querySelector('.stop')

const trailerDiv = document.querySelector('.player')
playTrailer.addEventListener('click',()=>{
    
  trailerDiv.style.display = 'flex'

})

stopTrailer.addEventListener('click',()=>{
  player.stopVideo()
  trailerDiv.style.display = 'none'
  trailerFrame.style.display = 'none'
})
