function setToken(xhr, settings){
  xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
}

function veTrangcanhan() {
  window.location.assign('/thanhvien/thongtincanhan');
}

function showKetquaDangnhap(ketqua){
  if (ketqua==true){
    $('#noidungKetquaDangnhap').html("Đăng nhập <span class='text-primary'><b>thành công</b></span>.<br/><br/>Xin chào thành viên <b>" + $('#usr').val() + "</b>.");
    $('#btnVetrangCanhan').show();
    $('#btnDangnhaplai').hide();
  } else  {
    $('#btnDangnhap').html('Đăng nhập');
    $('#noidungKetquaDangnhap').html("Thông tin đăng nhập <span class='text-danger'><b>thất bại</b></span>.<br/><br/><b>Tên đăng nhập hoặc mật khẩu không đúng.</b>");
  }
  $('#ketquaDangnhap').modal('show');
}


function dangnhap(){
  //console.log("Member signIN function !!! - U: " + $('#usr').val() + " - P: " + $('#pwd').val())
  if ($('#usr').val().length > 0 && $('#pwd').val().length > 0){
    $('#usrError').hide();
    $('#pwdError').hide();
    $.ajax({
      url : '/ajax/thanhvien/dangnhap',
      type : 'POST',
      data : {
        'usr':$('#usr').val(),
        'pwd':$('#pwd').val()
      },
      beforeSend:function(xhr, settings){
        setToken(xhr, settings);
        $('#btnDangnhap').html('Đang kiểm tra ...');
      },
      success : function(data){
        showKetquaDangnhap(data['login']=='OK');

      },
      error: function(data){
        alert('Something wrong, please contact webadmin!');
      },
    });
  } else {
    if ($('#usr').val().length == 0 && $('#pwd').val().length == 0) {
      $('#usrError').show();
      $('#pwdError').show();
    } else {
       if ($('#usr').val().length == 0){
         $('#usrError').show();
         $('#pwdError').hide();
       } else {
         $('#usrError').hide();
         $('#pwdError').show();
       }
    }
  }

}
