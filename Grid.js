function pointsToWGSCells($points, $zoomLevel) {
    $cells = array();
    $map = array();
    $prevCell = null;
    for ($i = 0; $i < count($points); $i++) {
        $N = round($points[$i]["lat"] * $zoomLevel);
        $E = round($points[$i]["lng"] * $zoomLevel);
        $id = $E."-".$N;
        $cell = array();
        $cell["easting"] = $E;
        $cell["northing"] = $N;
        //
        $cell["id"] = $id;
        //
        $cell["lat"] = $E;
        $cell["lng"] = $N;
        //
        $cell["interpolation"] = 0;
        if ($prevCell != null) {
            $newCells = $this - > doWGSInterpolation($prevCell, $cell, $zoomLevel);
            for ($k = 0; $k < count($newCells); $k++) {
                if ($map[$newCells[$k]["id"]] != 1) {
                    $newCells[$k]["interpolation"] = 1;
                    array_push($cells, $newCells[$k]);
                    $map[$newCells[$k]["id"]] = 1;
                }
            }
        }
        if ($map[$id] != 1) {
            $map[$id] = 1;
            array_push($cells, $cell);
        }
        $prevCell = $cell;
    }
/*
    $dilCells = array();
    for ($i = 0; $i < count($cells); $i++) {
        $cells[$i]["dilation"] = 0;
        //
        $N = $cells[$i];
        $N["northing"]++;
        $S = $cells[$i];
        $S["northing"]--;
        $E = $cells[$i];
        $E["easting"]--;
        $W = $cells[$i];
        $W["easting"]++;
        //
        $NE = $cells[$i];
        $NE["northing"]++;
        $NE["easting"]--;
        $NW = $cells[$i];
        $NW["northing"]++;
        $NW["easting"]++;
        $SE = $cells[$i];
        $SE["northing"]--;
        $SE["easting"]--;
        $SW = $cells[$i];
        $SW["northing"]--;
        $SW["easting"]++;
        //
        $newCells = array();
        array_push($newCells, $N);
        array_push($newCells, $S);
        array_push($newCells, $E);
        array_push($newCells, $W);
        array_push($newCells, $NE);
        array_push($newCells, $NW);
        array_push($newCells, $SE);
        array_push($newCells, $SW);
        for ($j = 0; $j < count($newCells); $j++) {
            $cell = $newCells[$j];
            $latlng = array();
            $cell["lat"] = $cell["northing"];
            $cell["lng"] = $cell["easting"];
            $cell["id"] = $cell["easting"].
            "-".$cell["northing"];
            $cell["dilation"] = 1;
            if ($map[$cell["id"]] != 1) {
                $map[$cell["id"]] = 1;
                array_push($dilCells, $cell);
            }
        }
    }
    for ($i = 0; $i < count($dilCells); $i++) {
        array_push($cells, $dilCells[$i]);
    }
    unset($earth);
*/
    return $cells;
}
/*
function separateCells($C) {
    $cells = array();
    $dilatedCells = array();
    for ($i = 0; $i < count($C); $i++) {
        if ($C[$i]["dilation"] == 0) {
            array_push($cells, $C[$i]);
        } else {
            array_push($dilatedCells, $C[$i]);
        }
    }
    $cellRepresentation = array();
    $cellRepresentation["C"] = $cells;
    $cellRepresentation["Cd"] = $dilatedCells;
    return $cellRepresentation;
}
*/
function doWGSInterpolation($c1, $c2, $zoomLevel) {
    //$earth = new Earth();
    //
    $minE = min($c1["easting"], $c2["easting"]);
    $maxE = max($c1["easting"], $c2["easting"]);
    $minN = min($c1["northing"], $c2["northing"]);
    $maxN = max($c1["northing"], $c2["northing"]);
    //
    $deltaE = $maxE - $minE;
    $deltaN = $maxN - $minN;
    //
    $cells = array();
    if ($deltaN > $deltaE) {
        for ($i = $minN + 1; $i <= $maxN - 1; $i++) {
            $cell = array();
            $cell["easting"] = $c1["easting"] + round(($c2["easting"] - $c1["easting"]) * ($i - $c1["northing"]) / ($c2["northing"] - $c1["northing"]));
            $cell["northing"] = $i;
            $cell["lat"] = $cell["northing"];
            $cell["lng"] = $cell["easting"];
            $cell["id"] = $cell["easting"]."-".$cell["northing"];
            array_push($cells, $cell);
        }
    } else {
        for ($i = $minE + 1; $i <= $maxE - 1; $i++) {
            $cell = array();
            $cell["easting"] = $i;
            $cell["northing"] = $c1["northing"] + round(($c2["northing"] - $c1["northing"]) * ($i - $c1["easting"]) / ($c2["easting"] - $c1["easting"]));
            $cell["lat"] = $cell["northing"];
            $cell["lng"] = $cell["easting"];
            $cell["id"] = $cell["easting"]."-".$cell["northing"];
            array_push($cells, $cell);
        }
    }
    //echo count($cells)." ";
    return $cells;
}