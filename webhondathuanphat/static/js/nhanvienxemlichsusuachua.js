
var listThanhvien;
var testData;
$(function(){
    $.ajax({
      url: '/ajax/nhanvien/getListThanhvien',
      type: 'POST',
      beforeSend:function(xhr, settings){
        xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      },
      success: function(data){
        $('#groupInput').show();
        $('#thanhvienList').html('');
        data.listThanhvien.forEach(function(eachThanhvien){
          $('#thanhvienList').append("<a href='#' class='dropdown-item' id='" + eachThanhvien + "' onclick='getThanhvien(this.id);'>" + eachThanhvien + "</a>");
        });
        listThanhvien = data.listThanhvien;
        $('#txtThanhvien').removeAttr('disabled');
        $('#btnShowHistory').removeClass('disabled');
      },
      error: function(data){
        alert('Something wrong, please contact webadmin!')
      }
    });
});

function showSuggestThanhvien(){
  var thanhvien = $('#txtThanhvien').val();
  $("#thanhvienList").show();
  for (var i=0; i < listThanhvien.length; i++){
    if (listThanhvien[i].indexOf(thanhvien)>=0){
      $('#' + listThanhvien[i]).show();
    } else {
      $('#' + listThanhvien[i]).hide();
    }
  }
}

function getThanhvien(thanhvienID) {
  $("#thanhvienList").hide();
  $('#txtThanhvien').val(thanhvienID);
}

function showHistory(){
  $.ajax({
    url: '/ajax/nhanvien/xemLichsuSudungDichvu',
    data: {
      'usr' : $('#txtThanhvien').val(),
    },
    type: 'POST',
    beforeSend:function(xhr, settings){
      xhr.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
      $('#btnShowHistory').html('Đang tìm ...');
    },
    success: function(data){
      $('#historyList').show();
      $('#historyDetail').html('');
      $('#historyDate').html('');
      //console.log(data);
      testData = data;
      for (key in data.history){
        var eachDay = data.history[key]
        var day_id = key.replace(/-/g,'');
        $('#historyDate').append(
          "<a class='list-group-item d-flex justify-content-between py-1' href='#"
          + day_id + "'>"
          + key
          + "<span class='badge badge-danger badge-pill'> "
          + (eachDay.amount/1000).toLocaleString()
          + " </span>"
          + "</a>"
        );
        $('#historyDetail').append(
          "<div id='" + day_id + "'>"
          + "<h5>" + key + "</h5>"
          + "<p>Giờ vào: " + eachDay.timein + " - Giờ ra: " + eachDay.timeout
          + "<br/>Loại xe: " + eachDay.modelName + "- Biển số: " + eachDay.plateNumber
          + "<br/>Số km: " + eachDay.mileage.toLocaleString() + " km"
          + "<br/>Tên thợ: " + eachDay.mech
          + "<br/>Công việc: " + eachDay.service
          + "<br/>Thanh toán: " + eachDay.amount.toLocaleString() + " VND</p></div>"
        );
      };
      $('#btnShowHistory').html('Tìm khách hàng');
    },
    error: function(data){
      alert('Something wrong, please contact webadmin!')
    }
  });
}
