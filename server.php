<?php
$paramJson = $_POST['data'];
$param = json_decode($paramJson, true);

$server = new QueriesServer();
$server->processRequest($param);

class QueriesServer
{
		function processRequest($param,  $silent = false)
		{		
			$type = $param['request_type'];
			switch($type) 
			{
				case 'get_route':
					$response = $this->readRouteFromFile("1365683861651");
					break;
				default:
					$response = array('message' => 'Unknown operation!');
					break;
			}
			
			echo json_encode($response);
	
		}
		
		function readRouteFromFile($filename)
		{
			$route=array();
			
			$file = fopen($filename,"r");

			while(! feof($file))
			{
				$lineOfString=fgets($file);
				$components=explode(' ',$lineOfString);
				$point=array();
				$point["lat"]=(float)(trim($components[0]));
				$point["lng"]=(float)(trim($components[1]));
				$point["time"]=trim($components[2]);
				$point["alt"]=trim($components[3]);
				array_push($route,$point);
			}

			fclose($file);
			
			return $route;
		}
		
}



?>