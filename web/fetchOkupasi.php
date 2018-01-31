<?php
if (!empty($_POST['val'])) {
    $data = array();
    $connect = mysqli_connect('us-cdbr-iron-east-05.cleardb.net', 'b96437655ec530', 'd19e6630', 'heroku_696bdd3205855b4') or die(mysqli_error());
    $query = mysqli_query($connect, "SELECT kd_profesi, nama_profesi FROM kkni where jenjang = '".$_POST['val']."'");
    $i = 0;
    while($row = mysqli_fetch_array($query, MYSQLI_BOTH)){
    	$data[$i]['nama_profesi'] = $row['nama_profesi'];
        $data[$i]['kd_profesi'] = $row['kd_profesi'];
    	$i++;
    }
	echo json_encode($data);
}else{
	echo json_encode('Failed fetch');
}
?>

