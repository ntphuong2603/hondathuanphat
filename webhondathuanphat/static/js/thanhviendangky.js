function setToken(xhr, settings){
  xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
}

function vedangnhap(){
  window.location.assign('/thanhvien/thongtincanhan');
}

function showUserInfo(data){
  if (data['user'] == 'NG') {
    $('#ketquaKiemtraTendangnhap').attr('value','userOK');
    $('#btnKiemtra').removeClass('btn-danger');
    $('#btnKiemtra').addClass('btn-primary');
    $('#usrInfo').removeClass('text-danger');
    $('#usrInfo').addClass('text-primary');
    $('#usrInfo').html("Có thể sử dụng tên đăng nhập '<b>" + $("#usr").val() +"</b>'.");
  } else {
    $('#usrInfo').html('Tên đăng nhập đã được sử dụng hay chưa được kiểm tra, hãy chọn tên khác bằng cách thêm ký số hoặc sử dụng địa chỉ email.');
  }
}

function kiemtraTendangnhap(){
  $.ajax({
    url : '/ajax/thanhvien/kiemtraTendangnhap',
    type : 'POST',
    data : {'usr' : $("#usr").val()},
    beforeSend:function(xhr, settings){
      setToken(xhr, settings);
      $('#btnKiemtra').html('Đang kiểm tra ...');
    },
    success : function(data){
      $('#btnKiemtra').html('Kiểm tra tên đăng nhập');
      $('#usrInfo').show();
      showUserInfo(data);
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}

function changeConfirmInput(){
  if ($('#mth_confirm').val() == 'phone') {
    $('#phone_confirm').show();
    $('#email_confirm').hide();
  } else {
    $('#email_confirm').show();
    $('#phone_confirm').hide();
  }
  $('#phoneError').hide();
  $('#emailError').hide();
}

function ketquaKiemtraTendangnhap(){
  if ($("#ketquaKiemtraTendangnhap").val()=="userOK"){
    return true;
  } else {
    var data = {'user': 'OK'};
    showUserInfo(data);
    return false;
  }
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

function kiemtraXacnhan(){
  var phuongThuc = $('#mth_confirm').val();
  var ketqua = false;
  if (phuongThuc == 'phone'){
    var reg = RegExp('^[0-9]{7,11}$');
    ketqua = reg.test($('#phone_confirm').val());
    //console.log('ketqua Phone: ' + String(ketqua));
  } else if (phuongThuc == 'email') {
    var reg = RegExp('^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$');
    var reg1 = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    console.log($('#email_confirm').val());
    ketqua = reg1.test(String($('#email_confirm').val()).toLowerCase());
  }
  if (!ketqua){
    $('#' + phuongThuc + 'Error').show();
  } else {
    $('#' + phuongThuc + 'Error').hide();
  }
  //console.log(String(ketqua));
  return ketqua;
}

function kiemtraThongtinDangky(){
  //tendangnhap = $('#ketquaKiemtraTendangnhap').val();
  //console.log(String(ketquaKiemtraTendangnhap()) + String(kiemtraMatkhau()) + String(kiemtraXacnhan()));
  return ketquaKiemtraTendangnhap() && kiemtraMatkhau() && kiemtraXacnhan();
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
  if (kiemtraThongtinDangky()==true ){
    $.ajax({
      url : '/thanhvien/dangky',
      type : 'POST',
      data : {
        'usr' : $('#usr').val(),
        'pwd' : $('#pwd').val(),
        'phone' : $('#phone_confirm').val(),
        'email' : $('#email_confirm').val(),
      },
      beforeSend: function(xhr, settings){
        setToken(xhr, settings);
        $('#btnSubmitDangky').html('Đang thực hiện ...');
      },
      success : function(data){
        if (data['user']=='OK'){
          //console.log('User create successfully!');
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
