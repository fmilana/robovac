var mybot = '<div class="chatCont" id="chatCont">'+
              '<div id="result_div" class="resultDiv"></div>'+
              '<div class="chatForm input-group" id="chat-div">'+
                '<input type="text" class="col-10 form-control input-sm" id="chat-input" autocomplete="off" placeholder="Type something..."'+ 'class="form-control bot-txt"/>'+
                '<button id="send-button" class="col-2 btn btn-dark btn-sm">Send</button>' +
              '</div>'+
            '</div>';

$("mybot").html(mybot);

function sendMessage(message) {
  console.log(message);
  if (message) {
    var post_url = '/chatbotproxy/';
    var post_data = {'message': message};
    fetch(post_url, {
      method: 'POST',
      body: JSON.stringify(post_data),
      credentials: 'include',
      headers: {'Content-Type': 'application/json'}
    }).then(res => res.json()).then(response => {
      console.log('POST response:', response);
      processResponse(response);
    }).catch(error => {
      console.log('POST error:', error);
    });

    $("#result_div").append("<p id='user-message'> " + message + "</p><br>");
    $('#result_div').scrollTop($('#result_div')[0].scrollHeight);
    $("#chat-input").val('');

    setTimeout(function(){
      $('#result_div').append('<img id="typing-gif" src="' + staticUrl + 'robovac/images/typing.svg">')
      console.log('appending gif........');
      $('#result_div').scrollTop($('#result_div')[0].scrollHeight);
    }, 500);

    $('#typing-gif').remove();

    $('#result_div').css("height", "calc(100vh - 220px)");
  } else {
    $('#typing-gif').remove();
  }
}

function processResponse(data) {
  data = data[0];

  // var responseDelay = data['text'].length * 20
  // if (responseDelay < 1000) {
  //   responseDelay = 1000;
  // }

  // setTimeout(function() {
    appendBotMessage(data['text']);
  // }, responseDelay);
}

function appendBotMessage(message) {
  console.log('message = ' + message);

  $('#typing-gif').remove();
  $("#result_div").append("<p id='bot-message'>" + message + "</p><br>");
  $('#result_div').scrollTop($('#result_div')[0].scrollHeight);
}

$("#send-button").click(function() {
  sendMessage($("#chat-input").val());
});

$('#chat-input').keyup(function (e) {
  if (e.keyCode === 13) {
    sendMessage($("#chat-input").val());
  }
});
