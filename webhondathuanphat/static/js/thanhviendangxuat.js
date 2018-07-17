function dangxuat(){
  //console.log("Checking member - User: " + $('#usr').val())
  $.ajax({
    url : '/ajax/thanhvien/thanhvienDangxuat',
    type : 'POST',
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      $('#btnXacnhanDangxuat').html('Đang thực hiện đang xuất ...');
    },
    success : function(data){
      window.location.assign('')
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}

function huyDangxuat(){
  window.location.assign('/thanhvien/thongtincanhan')
}
