$(document).ready(function(){

    $('.settings').click(function(){
      $.ajax({
        url: '/index',
        type: 'get',
        contentType: 'application/json',
        data: {
          set_audio_volume_value: set_audio_volume.value,
          set_audio_speed_value: set_audio_speed.value
        },
      })

    })

})


function fun1() {

    send_result1.innerHTML=set_audio_volume.value;

}

function fun2() {

    send_result2.innerHTML=set_audio_speed.value;

}