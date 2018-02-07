<?php

$domain = "Pengoperasian Komputer"
$level = "1"

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
  // showDOMNode($x);

  echo $x->getElementsByTagName("KKNI")->item(0)->nodeValue; 
  $data = array();
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
    foreach ($domNode->childNodes as $node)
    {
        print $node->nodeName.':'.$node->nodeValue . "<br/>";
        if($node->hasChildNodes()) {
            showDOMNode($node);
        }
    }    
}
?>
