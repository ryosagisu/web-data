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
  // echo "Valid";

  foreach ($x->getElementsByTagName("Bidang") as $node) {
    if (validNodeKKNI($node)) {
      $dataKKNI = shownode($node);
    }
  }


  //TODO: use 'kodeUnitKompetensi' value from $dataKKNI and/or show only value of 'kodeUnitKompetensi' from $dataKKNI, currently showing all 'kodeUnit' from 'TujuanUtama' in SKKNI that contains one of 'kodeUnitKompetensi'
  foreach ($y->getElementsByTagName("TujuanUtama") as $node) {
    if (validNodeSKKNI($node)) {
      $dataSKKNI = shownode($node);
    }
  }
  echo json_encode($dataKKNI);
  echo "<br/><br/><br/>";
  echo json_encode($dataSKKNI);

  //TODO: write logic for peta_okupasi
}

function shownode($x) {
  $i = 0;
  foreach ($x->childNodes as $p){
    // echo $i++ . "<br/>";
    // echo $p->nodeName;
    if ($p->nodeType != XML_ELEMENT_NODE) continue;
    if(!isset($result[$p->nodeName])) $result[$p->nodeName] = array();

    if (hasChild($p)) {
      // echo $p->nodeName.' -> Nodes with child<br>';
      // $temp = shownode($p);
      // if(!isset($result[$p->parentNode->nodeName])) echo $p->parentNode->nodeName;
      // $result = array_merge_recursive($result, shownode($p));
      array_push($result[$p->nodeName], shownode($p));
    } 
    else{
      array_push($result[$p->nodeName], $p->nodeValue);
      // echo $p->nodeName.' : '.$p->nodeValue.'<br>';
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

//TODO: make this function dynamic
function validNodeKKNI(DOMNode $domNode){
  return $domNode->getElementsByTagName("domain")->item(0)->nodeValue == "Pengoperasian Komputer" && $domNode->getElementsByTagName("level")->item(0)->nodeValue == "1";
}

//TODO: make this function dynamic
function validNodeSKKNI(DOMNode $domNode){
  return $domNode->getElementsByTagName("kodeUnit")->item(0)->nodeValue == "J.63OPR00.001.2";
}

//TODO: make this function dynamic
function validNodePetaOkupasi(DOMNode $domNode){
  return $domNode->getElementsByTagName("domain")->item(0)->nodeValue == "Pengoperasian Komputer" && $domNode->getElementsByTagName("level")->item(0)->nodeValue == "1";
}
?>
