<?php
ini_set('display_errors', 0);
ini_set('display_startup_errors', 0);
error_reporting(0);

$file = 'plotMe.xml';
$fh = @fopen($file, 'r');
if (!$fh) {
    echo "<html>";
    echo "<head><title>Error</title></head>";
    echo "<body>";
    echo "<h1>If you are not seeing the drawing, probably you are an idiot. Here's what you need to do:</h1>";
    echo "</body></html>";
    exit;
}

$xml = fread($fh, filesize($file));
fclose($fh);

$w = 1920;
$h = 1080;

$im = imagecreatetruecolor($w, $h);
imageantialias($im, true);
$backgroundColor = imagecolorallocate($im, 33, 33, 33);
imagefilledrectangle($im, 0, 0, $w, $h, $backgroundColor);

$d = new DOMDocument();
if ($d->loadXML($xml)) {
    $lines = arr($d->getElementsByTagName('Line'));
    $arcs = arr($d->getElementsByTagName('Arc'));
    
    foreach ($lines as $line) {
        imageline(
            $im,
            (int)$line['XStart'],
            $h - (int)$line['YStart'],
            (int)$line['XEnd'],
            $h - (int)$line['YEnd'],
            color((!isset($line['Color'])) ? null : $line['Color'])
        );
    }
    
    foreach ($arcs as $arc) {
        $len = (int)$arc['Radius'] * 2;
        imagearc(
            $im,
            (int)$arc['XCenter'],
            $h - (int)$arc['YCenter'],
            $len,
            -$len,
            (int)$arc['ArcStart'],
            (int)$arc['ArcStart'] + (int)$arc['ArcExtend'],
            color((!isset($arc['Color'])) ? null : $arc['Color'])
        );
    }

    $textColor = imagecolorallocate($im, 255, 255, 255);
    imagestring($im, 5, 10, 10, "Author TGrozdanovski", $textColor);
} else {
    echo "<html><head><title>Error</title></head><body>";
    echo "<p>Probably mistake by an idiot who don't know anything.</p>";
    echo "</body></html>";
    exit;
}

header('Content-Type: image/png');
imagepng($im);
imagedestroy($im);

function arr($os) {
    $ret = [];
    foreach ($os as $o) {
        $tmp = [];
        if ($o->childNodes->length) {
            foreach ($o->childNodes as $node) {
                $tmp[$node->nodeName] = $node->nodeValue;
            }
        }
        $ret[] = $tmp;
    }
    return $ret;
}

function color($c) {
    switch ($c) {
        case 'blue':
            return 255;
        case 'green':
            return 65280;
        case 'red':
            return 16711680;
        case 'yellow':
            return 16776960;
        default:
            return 16777215;
    }
}
?>
