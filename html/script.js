var song_id = null
var now_playing = null

fetch("widget_config.json").then(response => response.json()).then(data => {
  if (data.LightMode.toLowerCase() == "true") {
    $(".background").css("background-color", "white");
    $(".background").css("color", "rgb(35, 35, 35)");
  }

  if (data.Position.toLowerCase() == "leftdown") {
    $("body").css("align-items", "flex-end");
    $("body").css("justify-content", "flex-start");
  }

  if (data.Position.toLowerCase() == "center") {
    $("body").css("align-items", "center");
    $("body").css("justify-content", "center");
  }

  if (data.Position.toLowerCase() == "rightup") {
    $("body").css("align-items", "flex-start");
    $("body").css("justify-content", "flex-end");
  }

  if (data.Position.toLowerCase() == "rightdown") {
    $("body").css("align-items", "flex-end");
    $("body").css("justify-content", "flex-end");
  }
})

function loop() {
  setTimeout(function() {
  fetch("now_playing.json").then(response => response.json()).then(data => {
    if (now_playing == null) {
      now_playing = "not null anymore lol"

      $("#now_playing").fadeOut(500)
      
      setTimeout(function() {
        $("#now_playing").html("Now playing")
      }, 500)

      $("#now_playing").delay(500).fadeIn()
    }

    if (song_id !== data.song_id) {
      song_id = data.song_id

      $("#p-wrapper").fadeOut(500)

      setTimeout(function() {
        $("#song_image").attr("src", data.song_image)
        $("#song_image").css("margin-top", "10px")
        $("#song_image").css("margin-right", "20px")
        $("#song_name").html(data.song_name)
        $("#artist_list").html("by " + data.artist_list)
      }, 500)

      $("#p-wrapper").delay(500).fadeIn()
    }
  })

  loop()
}, 1000)}

loop()