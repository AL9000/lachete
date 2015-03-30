 $( document ).ready(function() {

    // INCLUDE ONLY IF USER IS LOGGED

    setTimeout(update_position, 30000);

    function update_position() {
        if (navigator && navigator.geolocation) {
        var watchId = navigator.geolocation.watchPosition(send_position,
                                                          errorCallback,
                                                          {enableHighAccuracy:true,timeout:60000,maximumAge:0});

        } else {
          console.log('Geolocation is not supported');
        }
      }
    }

    function errorCallback() {}

    function send_position(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        $.post( "/gps/users/", { longitude: longitude, latitude: latitude } );
    }
});

