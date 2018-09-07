function showBooking(){
  var select = $('#bookingType').val();
  var ajaxString = '/ajax/nhanvien/showBooking_notConfirm';
  if (select == 0){
    ajaxString = '/ajax/nhanvien/showBooking_all';
  } else if (select == 2) {
    ajaxString = '/ajax/nhanvien/showBooking_confirmed';
  }
  console.log(ajaxString);
  $.ajax({
    url : ajaxString,
    type : 'POST',
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      $('#btnShowBook').html('Đang lấy dữ liệu ...');
    },
    success : function(data){
      console.log(data);
      $('#tableBodyData').html(data);
      $('#btnShowBook').html('Hiển thị');
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}
