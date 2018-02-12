<?php
//load kkni data set

$kkni = file_get_contents("kkni.xml");
$x = new DOMDocument();
$x->loadXML($kkni);

//load skkni data set
$skkni = file_get_contents("skkni.xml");
$y = new DOMDocument();
$y->loadXML($skkni);

//load peta_okupasi data set
$peta_okupasi = file_get_contents("peta_okupasi.xml");
$z = new DOMDocument();
$z->loadXML($peta_okupasi);

$listKompetensi = array();
//compare data set with schema
if ($x->schemaValidate("kkni.xsd") && $y->schemaValidate("skkni.xsd") && $z->schemaValidate("peta_okupasi.xsd")) {

  $domain = $_POST['domain'];
  $level = $_POST['level'];
  $dataKKNI = array();
  $dataSKKNI = array();

  foreach ($x->getElementsByTagName("Bidang") as $node) {
    if (validNode($node, "domain", $domain)) {
      array_push($dataKKNI, shownode($node, "KKNI", $level));
    }
  }
  $listKompetensi = array_unique($listKompetensi);

  //read skkni data set and only fetch used 'kodeUnit'
  foreach ($y->getElementsByTagName("TujuanUtama") as $node) {
    if (validNode($node, "kodeUnit", $listKompetensi)) {
      array_push($dataSKKNI, shownode($node, "SKKNI", $listKompetensi));
    }
  }
  $data["KKNI"] = $dataKKNI;
  $data["SKKNI"] = $dataSKKNI;
  // echo json_encode($listKompetensi);
  // echo "<br/><br/><br/>";
  // print_r($dataKKNI);
  // echo json_encode($dataKKNI);
  // echo "<br/><br/><br/>";
  // echo json_encode($dataSKKNI);
  echo json_encode($data);

  //TODO: write logic for peta_okupasi
}

function shownode($x, $root, $set="") {
  $i = 0;
  foreach ($x->childNodes as $p){
    if ($p->nodeType != XML_ELEMENT_NODE) continue;
    if(!isset($result[$p->nodeName])) $result[$p->nodeName] = array();
    if ($root == "KKNI" && $p->nodeName == "kodeUnitKompetensi") array_push($GLOBALS['listKompetensi'], $p->nodeValue);

    if (hasChild($p)) {
      if ($root == "KKNI" && $p->nodeName == "Jenjang") {
        if(!validNode($p, "level", $set)) continue;
      }

      if ($root == "SKKNI" && $p->nodeName == "UnitKompetensi") {
        if(!validNode($p, "kodeUnit", $set)) continue;
      } 
      array_push($result[$p->nodeName], shownode($p, $root, $set));     
    } 
    else{
      array_push($result[$p->nodeName], $p->nodeValue);
    }
  }
  return $result;
}

function hasChild($p) {
  if ($p->hasChildNodes()) {
    foreach ($p->childNodes as $c) {
      if ($c->nodeType == XML_ELEMENT_NODE)
        return true;
    }
  }
  return false;
}

function validNode(DOMNode $domNode, $tagName, $value){
  return is_array($value) ? in_array($domNode->getElementsByTagName($tagName)->item(0)->nodeValue, $value) : $domNode->getElementsByTagName($tagName)->item(0)->nodeValue == $value;
}
?>
