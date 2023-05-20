var song_id = null;

$.ajax({
  url: 'http://127.0.0.1:7777/config',
  type: 'GET',
  success: function(data) {
    switch(data.widget.position) {
      case "leftcenter":
        $("body").css("align-items", "center");
        $("body").css("justify-content", "flex-start");
        break;

      case "leftdown":
      $("body").css("align-items", "flex-end");
      $("body").css("justify-content", "flex-start");
      break;     

      case "centerup":
        $("body").css("align-items", "flex-start");
        $("body").css("justify-content", "center");
        break;
  
      case "center":
        $("body").css("align-items", "center");
        $("body").css("justify-content", "center");
        break;
    
      case "centerdown":
        $("body").css("align-items", "flex-end");
        $("body").css("justify-content", "center");
        break;
      
      case "rightup":
        $("body").css("align-items", "flex-start");
        $("body").css("justify-content", "flex-end");
        break;
      
      case "rightcenter":
        $("body").css("align-items", "center");
        $("body").css("justify-content", "flex-end");
        break;

      case "rightdown":
        $("body").css("align-items", "flex-end");
        $("body").css("justify-content", "flex-end");
        break;
    };
  }
});

function loop() {
  setTimeout(function() {
    $.ajax({
      url: 'http://127.0.0.1:7777/spotify',
      type: 'GET',
      success: function(data) {
        if (song_id !== data.id) {
          song_id = data.id;

          $(".background").fadeOut(500);

          setTimeout(function() {
            $(".image").css("background-image", "url(" + data.image_url + ")");
            $("#title").html(data.title);
            $("#title").removeClass("animate");
            $("#artists").html(data.artists.join(", "));
            $("#artists").removeClass("animate");
          }, 500);

          $(".background").delay(500).fadeIn();

          animate()
        };
      }});

    loop();
  }, 2000)};

loop();

function animate() {
  setTimeout(function() {
      if (($("#title-div").width() + 20) < $("#title").width()) {
        $("#title").addClass("animate");
      }

      if (($("#artists-div").width() + 20) < $("#artists").width()) {
        $("#artists").addClass("animate");
      }
  }, 2000)};