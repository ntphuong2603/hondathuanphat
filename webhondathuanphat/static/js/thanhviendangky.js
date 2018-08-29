function setToken(xhr, settings){
  xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
}

function vedangnhap(){
  window.location.assign('/thanhvien/thongtincanhan');
}

function kiemtraMatkhau(){
  var matkhau = $('#pwd').val();
  var ketqua = false;
  if ((matkhau.length > 6)){
    $('#pwdError').hide();
    if (matkhau != $('#confirm_pwd').val()){
      $('#confirm_pwdError').show();
    } else {
      $('#confirm_pwdError').hide();
      ketqua = true;
    }
  } else {
    $('#pwdError').show();
  }
  return ketqua;
}

function showKetquaDangky(ketqua){
  if (ketqua==true){
    $('#noidungKetqua').html("<p>Thành viên đăng ký <span class='text-primary'><b>thành công</b></span> với tên đăng nhập là: <b>" + $("#usr").val() + "</b></p>");
    $('#btnVedangNhap').show();
  } else {
    $('#noidungKetqua').html("<p>Thành viên đăng ký <span class='text-danger'><b>thất bại</b></span> với tên đăng nhập là: <b>" + $("#usr").val() + "</b></p>");
  }
  $('#ketquaDangkyThanhvien').modal('show');
}

function dangkyThanhvien(){
  if (kiemtraMatkhau()==true ){
    $.ajax({
      url : '/thanhvien/dangky',
      type : 'POST',
      data : {
        'usr' : $('#usr').val(),
        'pwd' : $('#pwd').val(),
      },
      beforeSend: function(xhr, settings){
        setToken(xhr, settings);
        $('#btnSubmitDangky').html('Đang thực hiện ...');
      },
      success : function(data){
        if (data['user']=='OK'){
          showKetquaDangky(true);
        } else {
          //console.log('User create UN-successfully!');
          showKetquaDangky(false);
        }
      },
      error: function(data){
        alert('Something wrong, please contact webadmin!')
      },
      complete: function(){
        $('#btnSubmitDangky').html('Gởi đăng ký');
      }
    });
  }
}
