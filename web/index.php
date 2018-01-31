<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
  <title>PROFIL LULUSAN GENERATOR</title>
</head>
<body>
<div class="container">
      <h2 class="text-center">PROFIL LULUSAN GENERATOR</h2>
      <h4 class="text-center">Pilih Jenjang</h4>
   <div class="inputs">
      <div class="area">
         <div class="row">
            <div class="col-3">
               <span class="input active-radio">
              <label for="jenjang1">SMP</label>
              <input type="radio" name="jenjang" value="1" id="jenjang1">
              <span class="click-efect x-174 y-128" style="margin-left: 25px; margin-top: 32px; width: 500px; height: 500px; top: -250px; left: -250px;"></span>
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang2">SMA</label>
              <input type="radio" name="jenjang" value="2" id="jenjang2">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang3">D1</label>
              <input type="radio" name="jenjang" value="3" id="jenjang3">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang4">D2</label>
              <input type="radio" name="jenjang" value="4" id="jenjang4">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang5">D3</label>
              <input type="radio" name="jenjang" value="5" id="jenjang5">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang6">S1</label>
              <input type="radio" name="jenjang" value="6" id="jenjang6">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang7">PRO</label>
              <input type="radio" name="jenjang" value="7" id="jenjang7">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang8">S2</label>
              <input type="radio" name="jenjang" value="8" id="jenjang8">
            </span>
            </div>
            <div class="col-3">
               <span class="input no-active-radio">
              <label for="jenjang9">S3</label>
              <input type="radio" name="jenjang" value="9" id="jenjang9">
            </span>
            </div>
         </div>
      </div>
      <br><br><br><br><br>
      <h4 class="text-center">Pilih Profesi</h4>
      <div class="area">
         <div class="row" id="listOkupasi"></div>
      </div>
      <button type="button" class="btn btn-primary" style="margin-top: 30px;" id="cekPL">Cek</button>
   </div>
    <br><br><br>
    <h4 class="text-center">Hasil</h4>
    <div id="hasilnya"></div>
</div>
</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript">
$("#cekPL").click(function(){
var selected = [];
$('#listOkupasi input[name="profesi"]:checked').each(function() {
    selected.push($(this).attr('value'));
});
if (selected.length > 0) {
  $.ajax({
    type: 'POST',
    url: 'fetchData.php',
    data:{
      'val': selected.toString(),
      'ajax': true,
    },
    success: function(data){
      console.log(data);
      $("#hasilnya").html('');
      var tu = [], fk = [], fu = [], ku = [], ju = [], ek = [], du = [], pp = [], kp = [], kt = [], ak = [], sk = [], pn = [], bv = [], kv = [];
      for(var i = 0; i < JSON.parse(data).length; i++){
        tu.push(JSON.parse(data)[i].tujuan_utama);
        fk.push(JSON.parse(data)[i].fungsi_kunci);
        fu.push(JSON.parse(data)[i].fungsi_utama);
        ku.push(JSON.parse(data)[i].kode_unit);
        ju.push(JSON.parse(data)[i].judul_unit);
        ek.push(JSON.parse(data)[i].elemen_kompetensi);
        du.push(JSON.parse(data)[i].deskripsi_unit);
        pp.push(JSON.parse(data)[i].panduan_penilaian);
        kp.push(JSON.parse(data)[i].konteks_penilaian);
        kt.push(JSON.parse(data)[i].ketrampilan);
        ak.push(JSON.parse(data)[i].aspek_kunci);
        sk.push(JSON.parse(data)[i].sikap_kerja);
        pn.push(JSON.parse(data)[i].pengetahuan);
        bv.push(JSON.parse(data)[i].batasan_variabel);
        kv.push(JSON.parse(data)[i].konteks_variabel);
      }
      var result = 
        "<div class='row'><p>Tujuan Utama: "+tu.toString()+"</p><br><p>Fungsi Kunci: "+fk.toString()+"</p><br><p>Fungsi Utama: "+fu.toString()+"</p><br><p>Kode Unit: "+ku.toString()+"</p><br><p>Judul Unit: "+ju.toString()+"</p><br><p>Elemen Kompetensi: "+ek.toString()+"</p><br><p>Deskripsi Unit: "+du.toString()+"</p><br><p>Panduan Penilaian: "+pp.toString()+"</p><br><p>Konteks Penilaian: "+kp.toString()+"</p><br><p>Keterampilan: "+kt.toString()+"</p><br><p>Aspek Kritis: "+ak.toString()+"</p><br><p>Sikap Kerja: "+sk.toString()+"</p><br><p>Pengetahuan: "+pn.toString()+"</p><br><p>Batasan Variabel: "+bv.toString()+"</p><br><p>Konteks Variabel: "+kv.toString()+"</p><br></div>";
      $("#hasilnya").html(result);
    }
  });
}else{
  alert("Pilih profesi dulu bro!");
}
});
</script>
<script type="text/javascript">
$(document).ready(function() {
  $.ajax({
    method: 'post',
    url: 'fetchOkupasi.php',
    data: {
      'val': '1',
      'ajax': true,
    },
    success: fetchSucceed
  });
  $('input[name=jenjang]').change(function(){
      var value = $('input[name=jenjang]:checked').val();
      $.ajax({
        method: 'post',
        url: 'fetchOkupasi.php',
        data: {
          'val': value,
          'ajax': true,
        },
        success: fetchSucceed
      });
    });
  function fetchSucceed(data){
    $('#listOkupasi').html('');
    $.each(JSON.parse(data), function(index,value){
      var checkbox=
      "<div class='col-3-3'><span class='input'><label for='profesi"+index+"'>"+value.nama_profesi+"</label><input type='checkbox' name='profesi' id='profesi"+index+"' value='"+value.kd_profesi+"'></span></div>";
      $("#listOkupasi").append($(checkbox));
    });
  }
});
</script>
<script type="text/javascript">
$(document).on("click", ".area .input", function(e){
   $("label[type='checkbox']", this)
   var pX = e.pageX,
      pY = e.pageY,
      oX = parseInt($(this).offset().left),
      oY = parseInt($(this).offset().top);
   $(this).addClass('active');
   if ($(this).hasClass('active')) {
      $(this).removeClass('active')
      if ($(this).hasClass('active-2')) {
         if ($("input", this).attr("type") == "checkbox") {
            if ($("span", this).hasClass('click-efect')) {
               $(".click-efect").css({
                  "margin-left": (pX - oX) + "px",
                  "margin-top": (pY - oY) + "px"
               })
               $(".click-efect", this).animate({
                  "width": "0",
                  "height": "0",
                  "top": "0",
                  "left": "0"
               }, 400, function() {
                  $(this).remove();
               });
            } else {
               $(this).append('<span class="click-efect x-' + oX + ' y-' + oY + '" style="margin-left:' + (pX - oX) + 'px;margin-top:' + (pY - oY) + 'px;"></span>')
               $('.x-' + oX + '.y-' + oY + '').animate({
                  "width": "500px",
                  "height": "500px",
                  "top": "-250px",
                  "left": "-250px",
               }, 600);
            }
         }
         if ($("input", this).attr("type") == "radio") {
            $(".area .input input[type='radio']").parent().removeClass('active-radio').addClass('no-active-radio');
            $(this).addClass('active-radio').removeClass('no-active-radio');

            $(".area .input.no-active-radio").each(function() {
               $(".click-efect", this).animate({
                  "width": "0",
                  "height": "0",
                  "top": "0",
                  "left": "0"
               }, 400, function() {
                  $(this).remove();
               });
            });

            if (!$("span", this).hasClass('click-efect')) {
               $(this).append('<span class="click-efect x-' + oX + ' y-' + oY + '" style="margin-left:' + (pX - oX) + 'px;margin-top:' + (pY - oY) + 'px;"></span>')
               $('.x-' + oX + '.y-' + oY + '').animate({
                  "width": "500px",
                  "height": "500px",
                  "top": "-250px",
                  "left": "-250px",
               }, 600);
            }

         }
      }
      if ($(this).hasClass('active-2')) {
         $(this).removeClass('active-2')
      } else {
         $(this).addClass('active-2');
      }
   }
});
</script>
</html>