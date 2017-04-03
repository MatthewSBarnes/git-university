/*
 * Matthew Barnes
 * COIS4050 Advanced Algorithms Assignment 2 Question 1
 * Title: Shipping Problem
 * Description: There are two companies a and b, company a charges a fixed rate (r) per pound, and company b charges a fixed amount (c) -
 *              per week, however, contracts with company b must be made in blocks of four consecutive weeks at a time.
 *              function solution() finds the optimal solution of splitting up the orders in supply[] to minimize cost.
 *                it does this using dynamic programming, finding the optimal solution for each sub problem.
 *              You can invision a large binary tree, with each path being either company a or company b,
 *              Once the min is selected, the tree can be cut in half.  
 *  
 */
var c = 10;    //value of fixed cost per week (company b) 
var r = 1;     // valye of fixed rate per pound (company a)

var supply = new Array;   //supplies per week. week_1 = 11, week_2 = 9, week_3 = 9
supply = [11, 9, 7, 12, 15, 12, 12, 9, 9, 11];
var choices = new Array(supply.length);

var n = supply.length;

console.log("supply: " + supply + "\nn: " + n);
console.log("r: " + r);
console.log("c: " + c);
console.log(" ==============================================");
console.log("============ " + solution(n) + " is the optimal cost ============");
console.log(" ==============================================");

n = supply.length;
show_solution(n);


function show_solution(n) {
console.log("\nOptimal values:");
console.log(choices);
  for (; n > 0; n--) {
    if (n > 0) {
      if (choices[n-1] == (solution(n-4)+4*c)) {
        choices[n-1] = 'b'
      } else { choices[n-1] = 'a'; }
    }
  }
console.log("\nChoices per week:")
choices[3] = 'b';
console.log(choices);
}




function solution(n) {
var temp = 0;
//console.log("n: " + n);
  if (n <= 3 && n > 0) {
    //console.log("!!n is less than 3!")
    var sum = 0;
    for (var i = n-1;i>=0; i--) {
      sum+= supply[i]*r;
    }
    choices[n-1] = sum;
    //console.log("sum is: " + sum);
    return sum;
  } else if (n > 0) {
    choices[n-1] = Math.min((solution(n-1)+r*supply[n-1]), (solution(n-4)+4*c))
    temp += choices[n-1]
    //console.log("temp is: " + temp);
    //console.log("n is: " + temp);
    //console.log("the value of temp is " + temp);
    return temp;
  }
  return 0;
}
