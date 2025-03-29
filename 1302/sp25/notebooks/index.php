<?php
/*
written by craig@123marbella.com on 19th Jan 2016

This script can be placed in a folder and will display the contents of the folder based on the file extensions you define in the settings below.

With this function you can:
- define a specific list of extensions to display on the page
- define a H1/title tag for the page
- define a custom logo
- restrict search engines from indexing the page (noindex)
- sort the list by filename ASC or DESC
*/

#######################################
//AUTHORSIED FILE EXTENSIONS
#######################################
//put a list of authorised file extensions in array format
//EG: 'pdf', 'jpeg', 'png', 'gif', 'bmp'
$file_extensions = array('pdf', 'txt', 'xls', 'gif', 'bmp', 'html', 'py', 'sql');

#######################################
//TITLE and H1 TAG
#######################################
$meta_title = "Directory Listing";

#######################################
//LOGO URL
#######################################
//$logo_url = "https://www.mydomain.com/downloads/top-logo.jpg";

#######################################
//Let search engines index this page?
#######################################
//set it to yes to allow SE's to index or no to hide from SE's
$index = "no";

#######################################
//Sort the list in asc or desc?
#######################################
//set the following to a-z for ascending order
//or z-a for desceing order
$sort = "a-z";

#######################################
//NO REAL NEED TO TOUCH THE NEXT PART
//UNLESS YOU KNOW WHAT YOU ARE DOING
#######################################
$files = array();
$directory = new DirectoryIterator(realpath(dirname(__FILE__)));
foreach ($directory as $fileinfo) {
    if ($fileinfo->isFile()) {
        $extension = strtolower(pathinfo($fileinfo->getFilename(), PATHINFO_EXTENSION));
        if (in_array($extension, $file_extensions)) {
            $files[] = $fileinfo->getFilename();
        }
    }
}
if($sort == "a-z") { asort($files); } else { rsort($files); }
$file_count = count($files);

function format_bytes($bytes, $precision = 2) {  
    $kilobyte = 1024;
    $megabyte = $kilobyte * 1024;
    $gigabyte = $megabyte * 1024;
    $terabyte = $gigabyte * 1024;
   
    if (($bytes >= 0) && ($bytes < $kilobyte)) {
        return $bytes . ' B';
 
    } elseif (($bytes >= $kilobyte) && ($bytes < $megabyte)) {
        return round($bytes / $kilobyte, $precision) . ' KB';
 
    } elseif (($bytes >= $megabyte) && ($bytes < $gigabyte)) {
        return round($bytes / $megabyte, $precision) . ' MB';
 
    } elseif (($bytes >= $gigabyte) && ($bytes < $terabyte)) {
        return round($bytes / $gigabyte, $precision) . ' GB';
 
    } elseif ($bytes >= $terabyte) {
        return round($bytes / $terabyte, $precision) . ' TB';
    } else {
        return $bytes . ' B';
    }
}
if($index == "no") {
	$no_index_tag = '<meta name="robots" content="noindex">';
}
function file_ext_strip($filename){
    return preg_replace('/.[^.]*$/', '', $filename);
}
function file_ext($filename) {
    $path_parts = pathinfo($filename);
	return $path_parts['extension'];
}
#######################################
?>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title><?php echo $meta_title ?></title>
<style>
body {font-family: Arial;font-size: 14px;}
h1 {font-size: 16px;	}
.subtext {margin-bottom:20px;margin-top:0px;font-size:11px;}
</style>
</head>
<body>
<?php echo $no_index_tag  ?>
<img src="<?php echo $logo_url ?>">
<h1><?php echo $meta_title ?></h1>
<p>Total Files: <?php echo $file_count  ?></p>
<?php
#######################################
//Edit your html here for the output of the file list
#######################################
$count = 1;
echo '<table width="760" border="0" cellspacing="0" cellpadding="0">';
echo '<tbody>';
foreach($files as $file) {
	
	//format the file name to a nice name without extension
	$file_name = file_ext_strip($file);
	$file_name = str_replace("-"," ",$file_name);
	$file_name = str_replace("_"," ",$file_name);
	$file_name = strtolower($file_name);
	$file_name = ucwords($file_name);	
	
	//get the file size in kb
	$file_size = filesize($file);
	$file_size = format_bytes($file_size, $precision = 2);
	
	//get file ext
	$file_ext = file_ext($file);
	$file_ext = strtoupper($file_ext);
	
	//get file date
	$file_date = date ("F d Y H:i", filemtime($file));
	
	//output the file name
	echo '<tr>';
   	echo '<td width="45" style="vertical-align:top;">'.$count.'.</td>'; 
	echo '<td>'. $file_name . " - " . $file_ext .'<br>';
	echo '<p class="subtext"><a href="'. $file . '" target="_blank">Download File</a> | Last Updated: '.$file_date.' | File Size: ' . $file_size . "</p>";
	echo '</td>';
    echo '</tr>';
	
	//increase count
	$count = $count + 1;
	
}
echo '</tbody>';
echo '</table>';
?>
</body>
</html>
