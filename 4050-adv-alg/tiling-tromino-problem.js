/*
 * Computer Science and Information Systems
 * COIS 4050 | Advanced Algorithms 
 * Title: Tiling / Tromino Problem
 * Author: Matthew Barnes
 * Description:
 *        setUp:                A square grid with length/width 2^k is created and populated with 0.
 *        addSquareTile:        A single tile is placed in any location on the matrix.
 *        detectSquareTile:     The square tile's location within the current subsquare is determined, and centerTiles is passed the direction.
 *        centerTiles:          A tromino (L shape) is placed within the center of the subsquare.
 *                              It is placed where the opening section is towards the single tile. ("L" opens towards the North East)
 *                              For each direction, there is a recursive call to detect the new square tile, [part of the tromino, or single tile]
 *                                and then place centerTiles on the center of the subsquare. This continues until the size of the subsquare is 2.
 *                                at which point the "depth" of the square will return up a level, and look at the next available subsquare.
 */



/* 
 *  The declaration of variables
 */

var k = 4;                // the exponent
var n = Math.pow(2, k);   //the length of the matrix will be n^k length and width
var grid = new Array (n); //the grid
var tile_order;           //the current number of the tile to be placed
var square_x = 12;         //single tile's x value
var square_y = 8;         //single tile's y value
var single_tile_location; //the direction that the single tile is in
var sub_square_top_x;     //the x value that defines the beginning of the subsection of the array
var sub_square_top_y;     //the y value that defines the beginning of the subsection of the array
var length;               //just another value for n (:

function twoDigit(number) {         //padding function, so that everything is at least 2 digits. 
  var twodigit = number >= 10 ? number : "0"+number.toString();
  return twodigit;
}

function setUp() {                //creates square matrix full of 00, resets tile_order
  console.log("Setting up....");
  tile_order = "01";
  for(var a=0; a< n; a++) {      //iterate through the cols
    grid[a] = new Array(n);
    for(var b=0; b< n; b++) {    //iterate through the rows
      grid[a][b] = "00";
    };
  };
}

function showGrid() {       //prints the grid
  console.log("Current Grid:\n");
  for (var z = grid.length-1; z >= 0; z--) {      //this way its more like a cartesian plane.
    console.log((z) + "\t" + grid[z]);
  }
  console.log("\n");
}

function addSquareTile(square_x, square_y) {    //adds the single square tile
  grid[square_y][square_x] = tile_order;
  tile_order++;
}

function detectSquareTile(square_x, square_y, sub_square_top_x, sub_square_top_y, length) {
  // console.log('================================================================');
  // console.log('sub_square_top_x: ' + sub_square_top_x + '\nsub_square_top_y: ' + sub_square_top_y + '\nlength: ' + length);
  // console.log('square_x: ' + square_x + '\nsquare_y: ' + square_y);
  // console.log('================================================================');
  if (square_x >= sub_square_top_x + length/2) {
    if (square_y >= sub_square_top_y + length/2) {
      single_tile_location = "NE";
    } else {
      single_tile_location = "SE";
    }
  } else {
    if (square_y >= sub_square_top_y + length/2) {
      single_tile_location = "NW";
    } else {
      single_tile_location = "SW";
    }
  }
  console.log("Location of single tile is " + single_tile_location + " : " + square_x + ", " + square_y);
  centerTiles(single_tile_location, sub_square_top_x, sub_square_top_y, length, square_x, square_y);   //doesnt send square x or square y
  // return single_tile_location;
}

function centerTiles(single_tile_location, sub_square_top_x, sub_square_top_y, length, square_x, square_y) {
  console.log("Adding L tile in correct orientation");
    switch(single_tile_location) {
      case("NW"):
        console.log('nw case');
        grid[sub_square_top_y + length/2][sub_square_top_x + length/2] = twoDigit(tile_order);     //places the L. top right
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2] = twoDigit(tile_order);    // bottom right
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2-1] = twoDigit(tile_order);     //bottom left
        tile_order++;
        showGrid();

        if (length>2) {
          //NW is where true single square location is so pass NW the normal square x and square y
          //recursive NW
          // console.log("entering NW subsquare NW");
          detectSquareTile(square_x, square_y, sub_square_top_x, sub_square_top_y+length/2, length/2);
          // console.log("up a level NW");
          //recursive NE
          // console.log("entering NE subsquare NW");
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2, sub_square_top_x+length/2, sub_square_top_y+length/2, length/2);
          // console.log("up a level NW");
          //recursive SW
          // console.log("entering SW subsquare NW");
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2-1, sub_square_top_x, sub_square_top_y, length/2);
          // console.log("up a level NW NW");      
          //recursive SE
          // console.log("entering SE subsquare NW NW");
          // console.log('sub_square_top_x: ' + sub_square_top_x + '\nsub_square_top_y: ' + sub_square_top_y + '\nlength: ' + length);
          // console.log('square_x: ' + square_x + '\nsquare_y: ' + square_y);
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2-1, sub_square_top_x+length/2, sub_square_top_y, length/2);
          // console.log("up a level");

          //square x and square y just get passed into NORTHWEST detectSquareTile function
          //its the L piece that gets sent in
          //Create a temp variable that gets sent in so you don't lose the true Single tile
        }
        break;

      case("NE"):
        // console.log('ne case');

        grid[sub_square_top_y + length/2][sub_square_top_x + length/2-1] = twoDigit(tile_order);     //places the L. top left
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2] = twoDigit(tile_order);    // bottom right
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2-1] = twoDigit(tile_order);     //bottom left
        tile_order++;
        showGrid();
        if (length>2) {
          //recursive NW, in NE case, needs to be top left of centre L
          // console.log("entering NW subsquare NE ");
          detectSquareTile(sub_square_top_x + length/2-1, sub_square_top_y + length/2, sub_square_top_x, sub_square_top_y+length/2, length/2);
          // console.log("up a level NE");      
          //recursive NE, in NE case, needs to be single tile.
          // console.log("entering NE subsquare NE");
          detectSquareTile(square_x, square_y, sub_square_top_x+length/2, sub_square_top_y+length/2, length/2);
          // console.log("up a level NE ");
          //recursive SW, in NE case, needs to be bottom left of centre L
          // console.log("entering SW subsquare NE");
          detectSquareTile(sub_square_top_x + length/2-1, sub_square_top_y + length/2-1, sub_square_top_x, sub_square_top_y, length/2);
          // console.log("up a level NE NE");
          //recursive SE, in NE case, needs to be bottom right of centre L
          // console.log("entering SE subsquare NE NE");
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2-1, sub_square_top_x+length/2, sub_square_top_y, length/2);
          // console.log("up a level NE");
        }
        break;

      case("SW"):
        // console.log('sw case');
        grid[sub_square_top_y + length/2][sub_square_top_x + length/2] = twoDigit(tile_order);     //places the L. top right
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2] = twoDigit(tile_order);    // bottom right
        grid[sub_square_top_y + length/2][sub_square_top_x + length/2-1] = twoDigit(tile_order);     //top left
        tile_order++;
        showGrid();
        if (length>2) {
          //recursive NW, in SW case must pass top left of L
          // console.log("entering NW subsquare SW");
          detectSquareTile(sub_square_top_x + length/2-1, sub_square_top_y + length/2, sub_square_top_x, sub_square_top_y+length/2, length/2);
          // console.log("up a level SW");        
          //recursive NE, in SW case must pass top right of L
          // console.log("entering NE subsquare SW");
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2, sub_square_top_x+length/2, sub_square_top_y+length/2, length/2);
          // console.log("up a level SW");
          //recursive SW, in SW case must pass square x and y
          // console.log("entering SW subsquare SW");
          detectSquareTile(square_x, square_y, sub_square_top_x, sub_square_top_y, length/2);
          // console.log("up a level SW SW ");
          //recursive SE, in SW case must pass bottom right
          // console.log("entering SE subsquare SW SW");
          // console.log("sub_square_top_x: " + sub_square_top_x + "\nsub_square_top_y: " + sub_square_top_y + "\nlength: " + length);
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2-1, sub_square_top_x+length/2, sub_square_top_y, length/2);
          // console.log("up a level");
        }
        break;

      case("SE"):
        // console.log('se case');
        grid[sub_square_top_y + length/2][sub_square_top_x + length/2] = twoDigit(tile_order);     //places the L top right
        grid[sub_square_top_y + length/2][sub_square_top_x + length/2-1] = twoDigit(tile_order);    // top left
        grid[sub_square_top_y + length/2-1][sub_square_top_x + length/2-1] = twoDigit(tile_order);  //bottom left 
        tile_order++;
        showGrid();
        if (length>2) {
          //recursive NW, in SE case, must pass top left of center
          // console.log("entering NW subsquare SE");
          detectSquareTile(sub_square_top_x + length/2-1, sub_square_top_y + length/2, sub_square_top_x, sub_square_top_y+length/2, length/2);
          // console.log("up a level SE");
          //recursive NE, in SE case, must pass top right of center
          // console.log("entering NE subsquare SE");
          detectSquareTile(sub_square_top_x + length/2, sub_square_top_y + length/2, sub_square_top_x+length/2, sub_square_top_y+length/2, length/2);
          // console.log("up a level SE");
          //recursive SW, in SE case, must pass bottom left of center 
          // console.log("entering SW subsquare SE");
                    // console.log(" fake fake fakeSQUARE x: " + square_x + "\n square y: " + square_y);
                    // console.log("imp sub_square_top_x: " + sub_square_top_x + "\nsub_square_top_y: " + sub_square_top_y + "\nlength: " + length);

          detectSquareTile(sub_square_top_x + length/2-1, sub_square_top_y + length/2-1, sub_square_top_x, sub_square_top_y, length/2);
          // console.log("up a level SE SE ");
          //recursive SE
          // console.log("entering SE subsquare SE SE");
          // console.log("SQUARE x: " + square_x + "\n square y: " + square_y);
                              // console.log("imp sub_square_top_x: " + sub_square_top_x + "\nsub_square_top_y: " + sub_square_top_y + "\nlength: " + length);

          detectSquareTile(square_x, square_y, sub_square_top_x+length/2, sub_square_top_y, length/2);
          // console.log("up a level SE");
        }
        break;
    }
  showGrid();
}

setUp();
showGrid();
addSquareTile(square_x, square_y);
showGrid();

single_tile_location = detectSquareTile(square_x, square_y, 0, 0, n);
showGrid();
