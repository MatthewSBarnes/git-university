/*
 * Matthew Barnes 0555121
 * Title: Security Monitoring Problem
 * Description: Security Guard monitoring session starts at the last 
 *    instant of the job that ends next, and then if the start time
 *    of the next job is before or during, consider that job watched too.
 *      If the next job starts afterwards, then proceed to that job's 
 *    finish time, and start the next monitoring session. 
 *      Worst case, the algorithm runs in nlogn time. 
 *        Mergesort worst case is nlogn.
 *        My algorithm worst case is n.
 */

//Global Vars.
var m = 3;
var watch_count=0;

var job_array = createArray();


printJobs(job_array);
job_array = mergeSort(job_array);
console.log("Merge Sort running...");
printJobs(job_array);
console.log("Monitor time is " + m);
console.log();
monitor(job_array);

/*
 * Create the jobs.
 * Created JS objects to contain the information.
 */
function createArray() {
  var job_one = new Object();
  job_one['start'] = 0;
  job_one['end'] = 10;

  var job_two = new Object();
  job_two['start'] = 11;
  job_two['end'] = 17;

  var job_three = new Object();
  job_three['start'] = 9;
  job_three['end'] = 16;

  var job_four = new Object();
  job_four['start'] = 15;
  job_four['end'] = 24;

  var job_five = new Object();
  job_five['start'] = 27;
  job_five['end'] = 30;

  return [job_three, job_two, job_one, job_four, job_five];
}









/*
 * Prints the job objects.
 */
function printJobs(arr) {
  console.log("     ==========\n\tJobs\n     ==========");
  for (elem in arr) {
    console.log("\nJob "+[elem]+ ":\nstart:"+arr[elem]['start']+"\nend:"+arr[elem]['end']);
  };
  console.log("\n\n\n");
}

/*
 * Sort the jobs with mergesort.
 * mergeSort f'n splits the splits the sections recursively.
 */
function mergeSort(arr) {
  if (arr.length < 2)
      return arr;

  var mid = parseInt(arr.length / 2);
  var left_side   = arr.slice(0, mid);
  var right_side  = arr.slice(mid, arr.length);

  return merge(mergeSort(left_side), mergeSort(right_side));
}

/*
 * Sort the jobs with mergesort.
 * merge f'n combines the split arrays.
 */
function merge(left_side, right_side) {
  var resultant_arr = [];

  while (left_side.length && right_side.length) {
      if (left_side[0]['end'] <= right_side[0]['end']) {
          resultant_arr.push(left_side.shift());
      } else {
          resultant_arr.push(right_side.shift());
      }
  }

  while (left_side.length)
      resultant_arr.push(left_side.shift());

  while (right_side.length)
      resultant_arr.push(right_side.shift());

  return resultant_arr;
}















/*
 * monitor f'n renoves items from the ordered array if they are monitored
 *  and increments + returns the watch count.
 */
function monitor(not_monitored_arr) {
  if (not_monitored_arr.length) {
    //console.log("ends_next_end_time = " + not_monitored_arr[0]['end']);
    var monitor_end_time = not_monitored_arr[0]['end'] + m;
    console.log("==============================\n     monitor_end_time = " +
      monitor_end_time + "\n==============================");

    for (var i = 0; i < not_monitored_arr.length; i++) {
      //console.log(i);
      //console.log(not_monitored_arr);
      if (not_monitored_arr[i]['start'] <= monitor_end_time) {
        //console.log("\nremoving:")
        //console.log(not_monitored_arr.shift());
        not_monitored_arr.shift();
        i--;
      } else {
        break;
      }
    }
    console.log("\nend:");
    console.log(not_monitored_arr);
    watch_count++;
    console.log("watch_count"+watch_count);
    monitor(not_monitored_arr);
  } else {
    console.log("done!");
    console.log("The guard checked the monitors " + watch_count + " times!");
    return watch_count;
  }
}
