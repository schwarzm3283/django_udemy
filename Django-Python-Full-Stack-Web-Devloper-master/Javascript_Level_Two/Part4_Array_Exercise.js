// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
function addNew(name) {
  roster.push(name);
}
// and uses .push to add a new student to the array


// REMOVE STUDENT
function remove(name) {
  var index = roster.indexOf(name);
  if (index > -1) {
    roster.splice(index, 1);
  }
}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function display() {
  console.log(roster);
}

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app
webApp = prompt("Use web app y/n");
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
if (webApp === "y") {
  while (webApp === "y") {
    toAdd = prompt("name to add");
    addNew(toAdd);
    toRemove = prompt("name to remove");
    remove(toRemove);
    displayQuit = prompt ("display \"d\" or quit \"q\"");
    if (displayQuit === "d") {
      display();
    }else {
      webApp = "n";
      alert("bye");
    }
  }
}else {
  alert("bye");
}
// Use if and else if statements to execute the correct function for each command.
