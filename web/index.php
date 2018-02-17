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
    <div class="d-flex justify-content-between" style="height: 60px;"  id="jenjang">
      <div class="p-2 custom-checkbox" id="jenjang1">
        <input type="radio" name="jenjang" value="1"/>
        <span class="box">SMP</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang2">
        <input type="radio" name="jenjang" value="2"/>
        <span class="box">SMA</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang3">
        <input type="radio" name="jenjang" value="3"/>
        <span class="box">Diploma I</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang4">
        <input type="radio" name="jenjang" value="4"/>
        <span class="box">Diploma II</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang5">
        <input type="radio" name="jenjang" value="5"/>
        <span class="box">Diploma III</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang6">
        <input type="radio" name="jenjang" value="6"/>
        <span class="box">Strata-1</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang7">
        <input type="radio" name="jenjang" value="7"/>
        <span class="box">Strata-2</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang8">
        <input type="radio" name="jenjang" value="8"/>
        <span class="box">Strata-3</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang9">
        <input type="radio" name="jenjang" value="9"/>
        <span class="box">Profesor</span>
      </div>
    </div>

    <br/><br/><br/>

    <h4 class="text-center">Pilih Domain</h4>
    <div class="d-flex justify-content-between flex-wrap" id="domain">
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="1">
        <span class="box">DATA MANAGEMENT SYSTEM</span> 
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="2">
        <span class="box">PROGRAMMING AND SOFTWARE DEVELOPMENT</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="3">
        <span class="box">HARDWARE AND DIGITAL PERIPHERALS</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="4">
        <span class="box">NETWORK AND INFRASTRUCTURE</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="5">
        <span class="box">OPERATION AND SYSTEM TOOLS</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="6">
        <span class="box">INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="7">
        <span class="box">IT GOVERNANCE AND MANAGEMENT</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="8">
        <span class="box">IT PROJECT MANAGEMENT</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="9">
        <span class="box">IT ENTERPRISE ARCHITECTURE</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="10">
        <span class="box"">IT SECURITY AND COMPLIANCE</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="11">
        <span class="box"">IT SERVICES MANAGEMENT SYSTEM</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="12">
        <span class="box"">IT AND COMPUTING FACILITIES MANAGEMENT</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="13">
        <span class="box"">IT MULTEMEDIA</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="14">
        <span class="box"">IT MOBILITY AND INTERNET OF THINGS</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="15">
        <span class="box"">INTEGRATION APPLICATION SYSTEM</span>
      </div>
      <div class="p-2 custom-checkbox">
        <input type="checkbox" name="domain" value="16">
        <span class="box"">IT CONSULTANCY AND ADVISORY</span>
      </div>
    </div>

  </div>
      <button type="button" class="btn btn-primary" style="margin-top: 30px;" id="cekPL">Cek</button>
    </div>
    <br/><br/><br/>
    <h4 class="text-center">Hasil</h4>
    <div id="hasilnya"></div>
</body>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
  $(".custom-checkbox").click(function() {
    // GET THE INPUT
    var activeInput = $(this).children("input");
    
    if(activeInput.is(':checked')) {
      // DESELECT IF ALREADY CHECKED
      $(activeInput).prop("checked", false);
    } else {
      // SELECT IF NOT CHECKED
      $(activeInput).prop("checked", true);
    }
    
    // IF RADIO REMOVE SELECTION FROM OTHER OPTIONS
    if(activeInput.is('[type=radio]')){
      var nonActiveInput = $(this).siblings().children("input");
      $(nonActiveInput).prop("checked", false);
    }
  });

$("#cekPL").click(function(){
  var selected = [], level;

  $("#jenjang div").each(function(){
    if ($(this).find("input").prop("checked")) {
      level = $(this).find("input").attr('value');
    }
  });

  $("#domain div").each(function(){
    if ($(this).find("input").prop("checked")) {
      selected.push($(this).find("span").text());
      // console.log($(this).find("span").text());
    }
  });

  $.ajax({
    type: 'POST',
    url: 'fetchData.php',
    data:{
      'domain': selected,
      'level': level,
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
        "<div class='row'><p>Tujuan Utama: "+tu.toString()+"</p><br/><p>Fungsi Kunci: "+fk.toString()+"</p><br/><p>Fungsi Utama: "+fu.toString()+"</p><br/><p>Kode Unit: "+ku.toString()+"</p><br/><p>Judul Unit: "+ju.toString()+"</p><br/><p>Elemen Kompetensi: "+ek.toString()+"</p><br/><p>Deskripsi Unit: "+du.toString()+"</p><br/><p>Panduan Penilaian: "+pp.toString()+"</p><br/><p>Konteks Penilaian: "+kp.toString()+"</p><br/><p>Keterampilan: "+kt.toString()+"</p><br/><p>Aspek Kritis: "+ak.toString()+"</p><br/><p>Sikap Kerja: "+sk.toString()+"</p><br/><p>Pengetahuan: "+pn.toString()+"</p><br/><p>Batasan Variabel: "+bv.toString()+"</p><br/><p>Konteks Variabel: "+kv.toString()+"</p><br/></div>";
      $("#hasilnya").html(data);
      // $("#hasilnya").html(result);
    }
  });
});
});


</script>

</html>
