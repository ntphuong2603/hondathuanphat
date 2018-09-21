function showBooking(){
  var select = $('#bookingType').val();
  var ajaxString = '/ajax/nhanvien/showBooking_notConfirm';
  if (select == 0){
    ajaxString = '/ajax/nhanvien/showBooking_all';
  } else if (select == 2) {
    ajaxString = '/ajax/nhanvien/showBooking_confirmed';
  }
  $.ajax({
    url : ajaxString,
    type : 'POST',
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      $('#btnShowBook').html('Đang lấy dữ liệu ...');
    },
    success : function(data){
      $('#tableBodyData').html(data);
      $('#btnShowBook').html('Hiển thị dữ liệu');
      if (select != 1){
        $('#confirmNumber').html($('input:checkbox:checked').length);
        $('#btnSubmitConfirm').addClass('disabled');
      } else {
        $('#btnSubmitConfirm').removeClass('disabled');
      }
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}

function showDetail(detailID) {
    $('#key_ID').val(detailID);
    $('#Booking_detail .modal-body').html(
      '<b>Khách hàng: </b>' + $('#' + detailID + '_name').text() +
      '<br/><b>Điện thoại: </b>' + $('#' + detailID + '_phone').text() +
      '<br/><b>Loại xe: </b>' + $('#' + detailID + '_model').text() +
      '<br/><b>Hẹn vào ngày: </b>' + $('#' + detailID + '_date').text() + ' <b>lúc: </b>' + $('#' + detailID + '_time').text() +
      '<br/><b>Hiện tượng: </b>' + $('#' + detailID + '_symptom').val() +
      '<br/><b>Danh sách phụ tùng: </b>' + $('#' + detailID + '_partList').val());
    if ($('#' + detailID + '_checkConfirm').prop('checked')){
      $('#btnConfirm').hide();
    } else {
      $('#btnConfirm').show();
    }
    $('#Booking_detail').modal('show');
}

function changeStatus(checkbox_ID){
  var checkbox_ID = '#' + checkbox_ID;
  var id_pos = checkbox_ID.indexOf('_', 0)-1;
  if (id_pos > 0) {
    var id = checkbox_ID.substr(1,id_pos);
    var info_ID = '#' + id + '_status';
  } else {
    var info_ID = checkbox_ID + '_status';
    checkbox_ID = checkbox_ID + '_checkConfirm';
  }
  if ($(checkbox_ID).prop('checked')){
    $(info_ID).html('Rồi');
    $(checkbox_ID).prop("checked");
    $(checkbox_ID).val('True');
    $('#confirmNumber').html(parseInt($('#confirmNumber').text())+1);
  } else {
    $(info_ID).html('Chưa');
    $(checkbox_ID).val('False');
    $('#confirmNumber').html(parseInt($('#confirmNumber').text())-1);
  }
}

function confirmStatus(){
  $('#' + $('#key_ID').val() + '_status').html('Rồi');
  $('#' + $('#key_ID').val() + '_checkConfirm').prop( "checked", true);
  $('#confirmNumber').html(parseInt($('#confirmNumber').text()) + 1);
}

function submitStatus(){
  var checkboxListChecked;
  $.ajax({
    url : '/ajax/nhanvien/changeBookingStatus',
    type : 'POST',
    data : {
      'confirmList': function(){
        var confirmList = [];
        var checkboxList = $('input:checkbox:checked');
        for (var i=0; i < checkboxList.length; i++){
            var position = checkboxList[i].id.indexOf('_', 0);
            confirmList.push(checkboxList[i].id.substr(0,position));
        }
        checkboxListChecked = confirmList;
        return confirmList;
      },
    },
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      $('#btnSubmitConfirm').html('Đang cập nhật ...');
    },
    success : function(data){
      for (var i=0; i < checkboxListChecked.length; i++){
        $('#' + checkboxListChecked[i] + "_all").remove();
      }
      $('#btnSubmitConfirm').html("Số lượng đã xác nhận <span class='badge badge-light' id='confirmNumber'>0</span>");
      $('#confirmNumber').html('0');
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}
