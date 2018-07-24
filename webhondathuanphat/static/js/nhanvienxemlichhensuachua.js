function changeInfo(checkbox_ID){
  checkbox_ID = '#' + checkbox_ID;
  var id_pos = checkbox_ID.indexOf('_', 0) + 1;
  var id = checkbox_ID.substr(0,id_pos);
  var info_ID = id + 'changeInfo';
  //if ($(checkbox_ID).checked == true){
  //console.log($(checkbox_ID).val());
  if ($(checkbox_ID).val()=='False'){
    $(info_ID).html('Đã xác nhận');
    $(checkbox_ID).val('True');
    //alert('Đã xác nhận');
  } else {
    $(info_ID).html('Chưa xác nhận');
    $(checkbox_ID).val('False');
    //alert('CHUA');
  }
  //console.log($(checkbox_ID).val());
  //console.log(info_ID);
}

function showDetail(detailID) {
    var modalID = '#' + detailID + "_detail";
    $(modalID).modal('show');
    //alert(detailID + modalID);
}

function updateStatus(booking_id){
  var id_pos = booking_id.indexOf('_', 0);
  var id = booking_id.substr(0,id_pos);
  var confirm_ID = '#' + id + '_checkConfirm';
  //console.log(id_pos);
  //console.log(id);
  $.ajax({
    url : '/ajax/nhanvien/changeBookingStatus',
    data: {
      'id': id,
      'confirm': $(confirm_ID).val()
    },
    type : 'POST',
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
    },
    success : function(data){
      alert('Đã cập nhật xong');
      $('#' + id + "_all").hide();
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}
