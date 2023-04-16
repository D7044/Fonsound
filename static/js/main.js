$(document).ready(function(){

    $('.settings').click(function(){
      $.ajax({
        url: '/index',
        type: 'get',
        contentType: 'application/json',
        data: {
          set_audio_volume_value: set_audio_volume.value,
          set_audio_speed_value: set_audio_speed.value,
          set_audio_high_pass_value: set_audio_high.value,
          set_audio_low_pass_value: set_audio_low.value,
          set_audio_pan_value: set_audio_pan.value,
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

function fun3() {

    send_result3.innerHTML=set_audio_high.value;

}

function fun4() {

    send_result4.innerHTML=set_audio_low.value;

}
function fun5() {

    send_result5.innerHTML=set_audio_pan.value;

}