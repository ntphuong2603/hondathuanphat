var listPhoneBooking;
var listBookingDetail;
$(function(){
    $.ajax({
      url: '/ajax/nhanvien/getPhoneBookingList',
      type: 'POST',
      beforeSend:function(xhr, settings){
        xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      },
      success: function(data){
        $('#phoneBookinglist').html('');
        console.log(data.listPhoneBooking);
        data.listPhoneBooking.forEach(function(eachPhoneNumber){
          $('#phoneBookinglist').append("<a href='#' class='dropdown-item' id='" + eachPhoneNumber + "' onclick='getBookingDetail(this.id);'>" + eachPhoneNumber + "</a>");
        });
        listPhoneBooking = data.listPhoneBooking;
        listBookingDetail = data.bookingDetail;
        //console.log(listPhoneBooking);
      },
      error: function(data){
        alert('Something wrong, please contact webadmin!')
      }
    });
});

function getBookingDetail(phoneNumber){
  $('#phone').val(phoneNumber);
  $('#phoneBookinglist').hide();
  var bookingDetail;
  $.each(listBookingDetail, function(key, value){
    if (value.pho == phoneNumber){
      bookingDetail = value;
    }
  });
  console.log(bookingDetail);
  $.each($('#formDangKy :input:text'), function(key, value){
    //console.log(key, value);
    if (value.id.indexOf('txt')>=0){
      var id = value.id.toLowerCase().substr(3,3);
      $(value).val(bookingDetail[id]);
      //console.log(id, bookingDetail[id]);
    }
  });
  $.each($('#formDangKy :input:text'), function(key, value){
    if ($(value).val().length == 0){
      $(value).attr('disabled', false);
    }
  });
}

function showSuggestPhoneThanhvien(){
  var thanhvien = $('#phone').val();
  $("#phoneBookinglist").show();
  for (var i=0; i < listPhoneBooking.length; i++){
    if (listPhoneBooking[i].indexOf(thanhvien)>=0){
      $('#' + listPhoneBooking[i]).show();
    } else {
      $('#' + listPhoneBooking[i]).hide();
    }
  }
}

function showCustomer(){
  $('#phone').attr('disabled', !($('#bookedCustomer').prop('checked')));
  $("input[id*='txt']").attr('disabled', $('#bookedCustomer').prop('checked'));
}

function nhanXeVao(){
  $.ajax({
    url : '/ajax/nhanvien/themxevaotram',
    type: 'POST',
    data : {
      'cus' : $('#txtCustomerName').val(),
      'pho' : $('#txtPhone').val(),
      'mod' : $('#txtModel').val(),
      'mil' : $('#txtMileage').val(),
      'ser' : $('#txtService').val(),
      'mec' : $('#txtMech').val(),
      'amt' : '0',
      'din' : ' '
    },
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken',
                           $("input[name='csrfmiddlewaretoken'").val());
      $('#btnNhanXeVao').html('Đang đăng ký nhận xe ...');
    },
    success : function(data){
      //console.log(data);
      $('#danhsachxedangsuachua').append(data);
      $('#numberXeDangSuaChua').html(parseInt($('#numberXeDangSuaChua').html())+1);
      $('#formDangKy').modal('hide');
      $('#btnNhanXeVao').html('Nhận xe');
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!');
    },
  });
}

function thanhtoan(idCustomer){
  $('#noidungThanhtoan').html($('#' + idCustomer).html());
  $('#noidungThanhtoan :input').prop('disabled', 'disabled');
  $('#noidungThanhtoan :button').hide();
  $('#formThanhtoan').modal('show');
}

function getData(){
  var result = {};
  $.each($('#noidungThanhtoan :input:text'), function(key, value){
    result[value.id.split('-')[1]] = $(value).val();
  });
  //console.log(result);
  return result;
}

function hoantatThanhtoan(){
  $.ajax({
    url : '/ajax/nhanvien/thanhtoantienDichvu',
    type: 'POST',
    data : {'timestamp': $('#noidungThanhtoan .card-title').text(),
            'serviceData': getData(),
            },
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken',
                           $("input[name='csrfmiddlewaretoken'").val());
    },
    success : function(data){
      if (data.result == 'OK'){
        $('#formThanhtoan').modal('hide');
        location.reload();
      }
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!');
    },
  });
}

function timXeDaHenTruoc(){
  var phoneNumber = $('#phone').val();
  $.ajax({
    url: '/ajax/nhanvien/timXeDaHenTruoc',
    type: 'POST',
    data: {'phone' : phoneNumber},
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken',
                           $("input[name='csrfmiddlewaretoken'").val());
    },
    success : function(data){

    },
    error: function(data){
      alert('Something wrong, please contact webadmin!');
    },
  });
}
