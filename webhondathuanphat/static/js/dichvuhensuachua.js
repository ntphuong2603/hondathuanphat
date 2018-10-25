//imgList = []
var fd;
function setToken(xhr, settings){
  xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
}

function getGioHen(){
  var ngayChon = $('#ngayHen').val().split("-");
  var now = new Date();
  var giobatdau = (new Date(ngayChon[2], ngayChon[1]-1, ngayChon[0], 08, 00, 00));
  var gioketthuc = (new Date(ngayChon[2], ngayChon[1]-1, ngayChon[0], 20, 00, 00));
  //console.log(now);
  $('#gioHen').html("<option disabled selected value=''>Chọn giờ</option>")
  now.setHours(now.getHours() + 2);
  while (giobatdau <= gioketthuc){
    if (giobatdau > now){
      gioHen = giobatdau.toTimeString().substr(0,5);
      $('#gioHen').append("<option value=" + gioHen + ">" + gioHen +"</option>");
    }
    giobatdau.setMinutes(giobatdau.getMinutes()+30)
    //console.log(giobatdau);
  }
}

function checkingInput(inputID) {
  var value = $('#' + inputID).val();
  //console.log(inputID);
  if (value.length == 0){
    $('#error' + inputID).show();
    return false;
  } else {
    $('#error' + inputID).hide();
    return true;
  }
}

function phoneChecking() {
  var reg = RegExp('^[0-9]{7,11}$');
  ketqua = reg.test($('#phoneNumber').val());
  if (ketqua == true){
    $('#errorphoneNumber').hide();
  } else {
    $('#errorphoneNumber').show();
  }
  return ketqua
}

function selectChecking(){
  //console.log($('#ngayHen').val());
  //console.log($('#gioHen').val());
  if ($('#ngayHen').val() == null  || $('#gioHen').val() == null){
    $('#errorDateTime').show();
    return false;
  } else {
    $('#errorDateTime').hide();
    return true;
  }
}

function kiemtraThongtin(){
  if (checkingInput('customerName') && phoneChecking() && checkingInput('modelName') && selectChecking()){
    return true;
  } else {
    return false;
  }
}

function goiLichHen() {
    if (kiemtraThongtin() == true){
      $('#xacnhNoidung').html("Khách hàng: <b>" + $('#customerName').val() + "</b> có điện thoại số: " + $('#phoneNumber').val() + "<br/>" +
                               "Đặt lịch vào ngày: " + $('#ngayHen').val() + " lúc: " + $('#gioHen').val() + "<br/>" +
                               "Để sửa chữa xe: " + $('#modelName').val() + "<br/>");
      $('#xacnhanLichhen').modal('show');
    }
}

function getImgList(){
  var list = [];
  if ($('#addPictures').prop('checked')==true){
    $.each($("img[id*='_img']"), function(img){
      console.log(img);
      list.append(img.prop('src'))
    });
    console.log(list);
  }
  return list;
}

function getFormData(){
  var form_data = new FormData();
  form_data.append('cname', $('#customerName').prop("value"));
  form_data.append('phone', $('#phoneNumber').val());
  form_data.append('model', $('#modelName').val());
  form_data.append('datep', $('#ngayHen').val());
  form_data.append('timep', $('#gioHen').val());
  form_data.append('sympt', $('#symptomDescription').val());
  form_data.append('partl', $('#partList').val());
  if ($('#addPictures').prop('checked')==true){
    var file_data = [];
    file_data.push($("#11_file").prop("files")[0]);
    file_data.push($("#12_file").prop("files")[0]);
    file_data.push($("#21_file").prop("files")[0]);
    file_data.push($("#22_file").prop("files")[0]);
    form_data.append('files', file_data);
    form_data.append('file1', $("#11_file").prop("files")[0]);
    form_data.append('file2', $("#12_file").prop("files")[0]);
  }
  //console.log(form_data);
  fd = form_data;
  return form_data;
}

function dangkyLichHen() {
  var form_data = new FormData();
  form_data.append('cname', $('#customerName').val());
  form_data.append('phone', $('#phoneNumber').val());
  form_data.append('model', $('#modelName').val());
  form_data.append('datep', $('#ngayHen').val());
  form_data.append('timep', $('#gioHen').val());
  form_data.append('sympt', $('#symptomDescription').val());
  form_data.append('partl', $('#partList').val());
  if ($('#addPictures').prop('checked')==true){
    form_data.append('file1', $("#11_file").prop("files")[0]);
    form_data.append('file2', $("#12_file").prop("files")[0]);
  }
  console.log(form_data);
  $.ajax({
    url : '/ajax/dichvu/dangkyLichhen',
    type : 'POST',
    dataType: 'json',
    processData: false,
    contentType: false,
    data : form_data,
    beforeSend: function(xhr, settings){
      setToken(xhr, settings);
      $('#btnGoilichHen').html('Đang gởi ...');
    },
    success : function(data){
      if (data['result']=='OK'){
        $('#noidungKetqua').html("Hẹn lịch sửa chữa thành công !!!");
        $('#btnClose').on('click', function(){
          window.location.assign('');
        });
      } else {
        $('#noidungKetqua').html("Hẹn lịch sửa chữa thất bại, vui lòng liên hệ cửa hàng để được trợ giúp !!!");
      }
      $('#btnGoilichHen').html('Hẹn lịch');
      $('#errorHenLich').modal('show');
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}

function showImage(inputFile){
  var reader = new FileReader();
  reader.onload = function (e){
    $('#'+inputFile.id.substr(0,2)+'_img').attr('src', e.target.result);
  }
  reader.readAsDataURL(inputFile.files[0]);
}

function showPictures() {
  //console.log($('#addPictures').prop('checked'));
  if ($('#addPictures').prop('checked')==true){
    $('#1').show();
    $('#2').show();
  } else {
    $('#1').hide();
    $('#2').hide();
  }
}
