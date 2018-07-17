function setToken(xhr, settings){
  xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
}

function changeStatus(btn_name){
  var field_name_pos = btn_name.indexOf('_', 5) + 1;
  var field_name = btn_name.substr(-(btn_name.length - field_name_pos));
  var btn_name_new = "#btn_";
  var btn_save = btn_name_new + 'save_' + field_name;
  var input_text = "#" + field_name;
  if (btn_name.indexOf('unlock') == -1){
    btn_name_new = btn_name_new + 'unlock_' + field_name;
    $(btn_save).show();
    $(input_text).attr('readonly', false);
  } else {
    btn_name_new = btn_name_new + 'lock_' + field_name;
    $(btn_save).hide();
    $(input_text).attr('readonly', true);
  }
  //console.log(btn_name, field_name_pos, field_name);
  $(btn_name_new).show();
  $("#" + btn_name).hide();
}

function saveInfo(btn_name) {
  var field_name_pos = btn_name.indexOf('_', 5) + 1;
  var field_name = btn_name.substr(-(btn_name.length - field_name_pos));
  var input_text = "#" + field_name;
  alert('info: ' + $(input_text).val())
}

function changeAll(btn_name){
    if (btn_name.indexOf('unlock') == -1){
      //$('#btn_unlock_all').show();
      //$('#btn_lock_all').hide();
      //$('#btn_save_all').show();
      $("button[id*='btn_unlock_']").show();
      $("button[id*='btn_lock_']").hide();
      $("button[id*='btn_save_']").show();
      $('input').attr('readonly', false);
    } else {
      //$('#btn_unlock_all').hide();
      //$('#btn_lock_all').show();
      //$('#btn_save_all').hide();
      $("button[id*='btn_unlock_']").hide();
      $("button[id*='btn_lock_']").show();
      $("button[id*='btn_save_']").hide();
      $('input').attr('readonly', true);
    }
    //console.log(btn_name);
}

function saveAll() {
  alert('info: ' + $('input').val())
}
