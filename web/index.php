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
        <span class="box">Profesional</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang8">
        <input type="radio" name="jenjang" value="8"/>
        <span class="box">Strata-2</span>
      </div>

      <div class="p-2 custom-checkbox" id="jenjang9">
        <input type="radio" name="jenjang" value="9"/>
        <span class="box">Strata-3</span>
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
    <div class="container">
      <h5 id="hasilJenjang">Jenjang</h5>
      <h5 id="hasilDomain">Domain</h5>
      <h5>Kemungkinan jabatan: </h5>
      <ol id="hasilJabatan"></ol>
      <h5>Unit kompetensi: </h5>
      <ol id="hasilUK"></ol>
      <h5>Pengetahuan: </h5>
      <ol id="hasilPengetahuan"></ol>
      <h5>Skill: </h5>
      <ol id="hasilSkill"></ol>
      <h5>Sikap Kerja: </h5>
      <ol id="hasilSikap"></ol>
    </div>
    <!-- <div id="hasilnya"></div> -->
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
      var hasil = JSON.parse(data);
      $("#hasilJenjang").html('');
      $("#hasilDomain").html('');
      $("#hasilJabatan").html('');
      $("#hasilUK").html('');
      $("#hasilPengetahuan").html('');
      $("#hasilSkill").html('');
      $("#hasilSikap").html('');
      //Jenjang
      $("#hasilJenjang").html('Level: '+ hasil.KKNI[0].Jenjang[0].level);
      //Domain
      $("#hasilDomain").html('Domain: '+ hasil.KKNI[0].domain);
      //Kemungkinan jabatan
      var kemungkinanJabatan = [];
      $.each(hasil.KKNI[0].Jenjang[0].kemungkinanJabatan, function(i, item) {
        kemungkinanJabatan.push('<li>' + item + '</li>');
      });
      $('#hasilJabatan').append( kemungkinanJabatan.join('') );
      //Unit Kompetensi
      var uk = [];
      // $.each(hasil.KKNI[0].Jenjang[0].UnitKompetensi, function(i, item) {
      //   uk.push('<li>' + item.judulUnitKompetensi[0] + '</li>');
      // });
      $.each(hasil.SKKNI[0].FungsiKunci[0].FungsiUtama[0].UnitKompetensi, function(i, item) {
        uk.push('<li>' + item.judulUnit[0] + '<p>' + item.deskripsiUnit[0] + '</p></li>');
      });
      $('#hasilUK').append( uk.join('') );
      //Pengetahuan
      var pengetahuan = [];
      $.each(hasil.SKKNI[0].FungsiKunci[0].FungsiUtama[0].UnitKompetensi[0].PanduanPenilaian[0].pengetahuan, function(i, item) {
        pengetahuan.push('<li>' + item + '</li>');
      });
      $('#hasilPengetahuan').append( pengetahuan.join('') );
      //Skill
      var skill = [];
      $.each(hasil.SKKNI[0].FungsiKunci[0].FungsiUtama[0].UnitKompetensi[0].PanduanPenilaian[0].keterampilan, function(i, item) {
        skill.push('<li>' + item + '</li>');
      });
      $('#hasilSkill').append( skill.join('') );
      //Sikap kerja
      var sikapKerja = [];
      $.each(hasil.SKKNI[0].FungsiKunci[0].FungsiUtama[0].UnitKompetensi[0].PanduanPenilaian[0].sikapKerja, function(i, item) {
        sikapKerja.push('<li>' + item + '</li>');
      });
      $('#hasilSikap').append( sikapKerja.join('') );
    }
  });
});
});


</script>

</html>
