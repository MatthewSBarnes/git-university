/*
 * Matthew Barnes
 * COIS 4050 Advanced Algorithms Assignment 2 Question 2 
 * Title: Return on Investment Problem
 * Description: [Similar to the rod cutting problem]
 *              Figure out the best investment strategy.
 *              You are provided with some rates for investments, along with the required start and end dates for those investments.
 *              Given specific rates and their ranges, calculate the optimal path to get the most money. When should you invest?
 *              Example
 *                Given three rates:  r1 = 1.13, r1_start = 0, r1_end = 3
 *                                    r2 = 1.16, r2_start = 0, r2_end = 2
 *                                    r3 = 1.17, r3_start = 2, r3_end = 3
 *                Compounded interest for r1 is (1.13)^(3-0) = 1.4428...
 *                Compounded interest for r2 is (1.16)^(2-0) = 1.3456
 *                Compounded interest for r3 is (1.17)^(3-2) = 1.17
 * 
 *                Although r1 seems like it has the best return on investment from the get go, the actual optimal return is if you were to go with r2 from 
 *                  year 0 to year 2, and then go with r3 from year 2 to year 3. The optimal ROI would be 1.3456*1.17 = 1.574352.
 */


var number_of_years = 5;
var array_rate_table = new Array(number_of_years);
var array_sell_date = new Array(number_of_years);
var temp=0;

var rate_one_start = 0; 
var rate_one_end = 4;
var rate_one = 1.13;  //i initialized the rates with the as 1.xx to simplify things a little.

var rate_two_start = 0;
var rate_two_end = 3;
var rate_two = 1.16;

var rate_three_start = 2;
var rate_three_end = 4;
var rate_three = 1.17;



setUp(number_of_years);
console.log("\t=================================\n\tDate and Rate Tables initialized:\n\t=================================");
showRateTable();
showDateTable();
addRates();
console.log("\t=================================\n\t Added New Rates to Rate Table:\n\t=================================");
showRateTable();
console.log("\t=================================\n\t  Date and Rate Tables Updated:\n\t=================================");
returnOnInvestment(0, 3);
showRateTable();
showDateTable();

function setUp(num) { //initialize 2d arrays
  for (var a = 0; a < num; a++) {
    array_rate_table[a] = new Array(num-1);
    array_sell_date[a] = new Array(num-1);
    for (var b = 0; b < num; b++) {
      array_sell_date[a][b] = "";
      if (b >= a) {
        array_rate_table[a][b] = "1.00";
      } else {
        array_rate_table[a][b] = "";

      }
    }
  }
}

function showRateTable() {       //prints the rate table
  console.log("Rate Table:\n");
  for (var z = 0; z < array_rate_table.length; z++) {      
    console.log((z) + "\t" + array_rate_table[z].join(',\t'));
  }
  console.log("\n");
}

function showDateTable() {       //prints the date table
  console.log("Date Table:\n");
  for (var z = 0; z < array_sell_date.length; z++) {      
    console.log((z) + "\t" + array_sell_date[z].join(',\t'));
  }
  console.log("\n");
}

function addRates() {
  //calculate the compounded return on investment per supplied rate. (1 + 0.xx)^(sell_year-buy_year)
  //limited the number to two decimals. (Could impact results negatively)
  array_rate_table[rate_one_start][rate_one_end] = (Math.pow(rate_one, rate_one_end-rate_one_start)).toFixed(2);
  array_rate_table[rate_two_start][rate_two_end] = (Math.pow(rate_two, rate_two_end-rate_two_start)).toFixed(2);
  array_rate_table[rate_three_start][rate_three_end] = (Math.pow(rate_three, rate_three_end-rate_three_start)).toFixed(2);
}

function returnOnInvestment() {
  //we know we want to iterate through the diagonal lines, first, and work our way up to the [0][n] coordinate. 
  for (var diagonal = 1; diagonal < array_rate_table.length; diagonal++) {
    //we can iterate through the columns and rows, in a diagonal fashion
    for (var j=diagonal; j < array_rate_table.length; j++) {
      var i = j - diagonal;
      sell_date = i+1;  //initialize the sell_date, ex. base case in diagonal 1
      //iterate through the possible splits of buy and sell dates.
      for (var k = i + 1; k <= j; k++ ) {
          //if the two splits of i to j together > the current value of i to j, replace it, and log the sell date.
        if ((array_rate_table[i][k]*array_rate_table[k][j]) > array_rate_table[i][j]) {
          // console.log("in the condition");
          array_rate_table[i][j] = (array_rate_table[i][k]*array_rate_table[k][j]).toFixed(2);
          sell_date = k;
          // console.log("k = " + k)
          // console.log(sell_date);
        } else if (array_rate_table[i][j] > (array_rate_table[i][k]*array_rate_table[k][j])) { //otherwise, the current is fine, and set it equal to j
          sell_date = j;
        }

        // console.log("\n\ndiagonal = " + diagonal + "\tj = " + j + "\ti = " + i + "\tk = " + k);
        // console.log("[" + i + "]" + "[" + k + "]*[" + k + "]" + "[" + j + "]" );
        // console.log("calculation: " + array_rate_table[i][k]*array_rate_table[k][j])
        // console.log("current:" + array_rate_table[i][j]+"\n\n")
        // console.log("")
        
        array_sell_date[i][j] = sell_date;
        // showRateTable();
        // showDateTable();
      }
    }
  }
}

