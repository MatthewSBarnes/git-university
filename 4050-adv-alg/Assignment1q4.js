/*
 * Matthew Barnes
 * COIS4050 Advanced Algorithms Assignment 1 Question 4
 * Title: Majority Element Problem
 * Description: Creates an array of any size, populates it, and then splits it into pairs. if there is an odd number, it moves to the sub array
 *              Compares the pair and adds the element to a sub array if they are equal.
 *              the sub array then runs through the same process. to find potential majorities
 *              The grid will then be compared to potential majorities. If they are equal to n/2 + 1, then it's a majority.
 *              
 */

//Declare array of any size and populate it.
var arr = new Array(8);
arr = [ 2, 3, 3, 1, 3, 1, 3, 3 ];
console.log(arr);

//Search for the majority_element within the array.
var majority_element = discoverMajorityElement(arr);
console.log(majority_element);
//Print the majority or if there is none
if (majority_element){
    console.log("The majority element is " + majority_element);
}
else{
    console.log("The majority element doesn't exist");
}


function spliceArray(array){
  var sub_array = new Array();
  console.log(array);
  //if current sub_array.length is 1, no need to continue.
  if (array.length == 1){
    return array;
  }
  //check to see if current sub_array is odd, if so: splice first element, and adds to new sub_array.
  if (array.length%2 == 1){
    sub_array[sub_array.length] = array[array.length-1];
    array.splice(array.length-1,1);
  }
  
  //iterate through every pair of 
  // console.log(array.length);
  for (var i = 0; i < array.length-1; i+=2){
    // console.log(array[i] + " = " + array[i+1] + "? i = " + i)
    if (array[i]==array[i+1]){
      //  console.log('two values are the same');
      sub_array[sub_array.length] = array[i];
      console.log(sub_array);
    }
  }
      // console.log("sub_array.length: " + sub_array.length);

  if (sub_array.length==0) {
    return null;
  } else if (sub_array.length==2) {
    // console.log("sub_array.length == 2");
    return sub_array;  
  }
  return spliceArray(sub_array);
}

//decide if they are actually majorities
function discover(sub_array){
    //If a single element, return it
    if (sub_array.length == 1) 
        return sub_array[0];
    
    //Print out what sub_array we are currently on
    console.log("On " + sub_array);

    //Split up left and right sides and pass them in recursively
    var left_majority = discover(sub_array.slice(0, sub_array.length/2));
    var right_majority = discover(sub_array.slice(sub_array.length/2, sub_array.length));
    var count = 0;

    //Count how many times candidate exists
    for (i in sub_array) {
        if (sub_array[i] == left_majority) 
            count++;

        if (count > sub_array.length/2) 
            return left_majority;
        }

        return right_majority;
}

function discoverMajorityElement(array){
  //Find the max potential icon
  var arf = array.slice();
  var max_element = spliceArray(array);
  // max_element can be an array of size 1, 2, or null.
  console.log("max_element is: " + max_element);
  console.log(arf);
  // console.log("arf = " + arf);
    if (max_element) {
      if (max_element.length == 2) {
        if (finalPass(max_element[0], arf)>arf.length/2){
          // console.log("first element is majority");
          return max_element[0];
        } else if (finalPass(max_element[1], arf)>arf.length/2){
          // console.log("second element is majority");
          return max_element[1];
        } else {
          // console.log("neither element is majority");
          return null;
        }
      } else {
        if (finalPass(max_element[0], arf)>arf.length/2){
          return max_element[0];
        } else {
          return null;
        }
      }
    }
}

//Function used to do final count through array to make sure majority candidate is truly the majority
function finalPass(element, array){
    // console.log("finalPass");
    // console.log(element);
    // console.log(array);
    var total = 0;
    //Loop through and increase count of emajority candidate
    for (var i = 0; i < array.length; i++){
        if (element == array[i]){
            total++;
        }
    }
    return total;
}




