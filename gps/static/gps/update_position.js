 $( document ).ready(function() {

    // INCLUDE ONLY IF USER IS LOGGED
    update_position();
    setTimeout(function() {update_position();}, 30000);

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function update_position() {
        if (navigator && navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(send_position);
        } else {
          console.log('Geolocation is not supported');
        }
    }

    function errorCallback() {}

    function send_position(position) {
        $.ajax({
            url: '/gps/users/',
            type: 'POST',
            data: '{"longitude":'+position.coords.longitude+ ',"latitude":'+ position.coords.latitude+'}',
            headers: {"X-CSRFToken": getCookie('csrftoken'),
                      "Content-Type": "application/json"},
            dataType: "json",
        });
    }
});

