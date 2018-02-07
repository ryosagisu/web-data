<?php
$kkni = file_get_contents("kkni.xml");
$x = new DOMDocument();
$x->loadXML($kkni);

$skkni = file_get_contents("skkni.xml");
$y = new DOMDocument();
$y->loadXML($skkni);

$peta_okupasi = file_get_contents("peta_okupasi.xml");
$z = new DOMDocument();
$z->loadXML($peta_okupasi); // Or load if filename required
if ($x->schemaValidate("kkni.xsd") && $y->schemaValidate("skkni.xsd") && $z->schemaValidate("peta_okupasi.xsd")) {
  echo "Valid";

  foreach ($x->getElementsByTagName("Bidang") as $node) {
    if (validNode($node)) {
      // showDOMNode($node);
      $data = array();
      $data["deskripsi"] = getNodeValues($node->getElementsByTagName("deskripsi"));
      $data["kodeJenjangKKNI"] = getNodeValues($node->getElementsByTagName("kodeJenjangKKNI"));
      $data["sikapKerja"] = getNodeValues($node->getElementsByTagName("sikapKerja"));
      $data["peranKerja"] = getNodeValues($node->getElementsByTagName("peranKerja"));
      $data["kemungkinanJabatan"] = getNodeValues($node->getElementsByTagName("kemungkinanJabatan"));
      $data["UnitKompetensi"] = getNodeValues($node->getElementsByTagName("UnitKompetensi"));
      // $data["judulUnitKompetensi"] = getNodeValues($node->getElementsByTagName("judulUnitKompetensi"));

      // <UnitKompetensi>
      //   <kodeUnitKompetensi>J.63OPR00.001.2</kodeUnitKompetensi>
      //   <judulUnitKompetensi>Menggunakan Perangkat Komputer</judulUnitKompetensi>
      // </UnitKompetensi>
      // <UnitKompetensi>
      //   <kodeUnitKompetensi>J.63OPR00.002.2</kodeUnitKompetensi>
      //   <judulUnitKompetensi>Menggunakan Sistem Operasi</judulUnitKompetensi>
      // </UnitKompetensi>
    }
  }
  // var_dump($x->getElementsByTagName("peranKerja")->item(0));
  // var_dump ($x->getElementsByTagName("judulUnitKompetensi")->item(0)->hasChildNodes());
  echo json_encode($data);
  

  
  // echo $x->getElementsByTagName("KKNI");
  // echo $xmlText->Bidang->keterangan;
  // echo {"Bidang"}->xpath("parent::*");
  // $xmlText = simplexml_load_string($kkni);
  // echo "Valid Schema <br>";
  // echo $xmlText->Bidang->Jenjang->kodeJenjangKKNI . "<br/>";
  // foreach($xmlText->Bidang as $v){
  //   echo json_encode($v->get_parent_node());
  // }
  // echo json_encode($xmlText);
  // echo $xmlText->Bidang->Jenjang->sikapKerja[0];
}

function showDOMNode(DOMNode $domNode) {

  foreach ($domNode->childNodes as $node){
    print $node->nodeName.':'.$node->nodeValue . "<br/>";
    if($node->hasChildNodes()) {
      showDOMNode($node);
    }
  }    
}

function getNodeValues(DOMNodeList $domNodeList){
  $result = array();
  foreach ($domNodeList as $node) {
    if ($node->childNodes->length != 0) {
      echo $node->nodeValue;
    }
    array_push($result, $node->nodeValue);
  }
  return $result;
}

function validNode(DOMNode $domNode){
  return $domNode->getElementsByTagName("domain")->item(0)->nodeValue == "Pengoperasian Komputer" && $domNode->getElementsByTagName("level")->item(0)->nodeValue == "1";
}
?>
