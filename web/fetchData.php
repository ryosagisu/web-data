<?php
if (!empty($_POST['val'])) {
	$data = array();
    $result = array();
    $connect = mysqli_connect('us-cdbr-iron-east-05.cleardb.net', 'b96437655ec530', 'd19e6630', 'heroku_696bdd3205855b4') or die(mysqli_error());
    if (strpos($_POST['val'], ',')) {
        $list = explode(',', $_POST['val']);
        $sql="SELECT kd_kompetensi FROM peta_okupasi";
        for($i = 0; $i < sizeof($list); $i++){
            if ($i == 0) {
                $sql.=" where kode_okupasi = '$list[$i]'";
            }else{
                $sql.=" or kode_okupasi = '$list[$i]'";
            }
        }
        $query = mysqli_query($connect, $sql);
        $i = 0;
        while($row = mysqli_fetch_array($query, MYSQLI_ASSOC)){
            $data[$i] = $row['kd_kompetensi'];
            $i++;
        }
    }else{
        $query = mysqli_query($connect, "SELECT kd_kompetensi FROM peta_okupasi where kode_okupasi = '".$_POST['val']."'");
        $i = 0;
        while($row = mysqli_fetch_array($query, MYSQLI_ASSOC)){
            $data[$i] = $row['kd_kompetensi'];
            $i++;
        }
    }
    $data = array_unique($data);
    $sql2="SELECT * FROM skkni";
    if (sizeof($data) > 0) {
        if (sizeof($data) > 1) {
            for($i = 0; $i < sizeof($data); $i++){
                if ($i == 0) {
                    $sql2.=" where kode_unit = '$data[$i]'";
                }else{
                    $sql2.=" or kode_unit = '$data[$i]'";
                }
            }
            $query2 = mysqli_query($connect, $sql2);
            while($row = mysqli_fetch_array($query2, MYSQLI_ASSOC)){
                $result[] = $row;
            }
        }else{
            $query = mysqli_query($connect, "SELECT * FROM skkni where kode_unit = '".$data[0]."'");
            while($row = mysqli_fetch_array($query, MYSQLI_ASSOC)){
                $result[] = $row;
            }       
        }
        echo json_encode($result);
    }else{
        echo json_encode('Gada data bro!');
    }
}else{
	echo json_encode('Failed fetch');
}
?>