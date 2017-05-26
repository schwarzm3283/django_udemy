// Welcome to Part 8: Your JavaScript Level One Project!
// For this project you will be building a generic website that will seem to ask
// mundane questions to normal users, but you secretly are looking for a spy! Anyone
// visiting your website will be asked a series of questions, only the Spy will be able to
// give specific answers you expect. If all questions are answered correctly, you will
// post a secret message in console for the Spy to read!
//
// Here are the four conditions you will check for the spy:
//
// The Spy has the same first letter of her First Name and Last Name

// VARIABLES
var fname = prompt("Please enter your first name");
var lname = prompt("please enter your last name");
var age = prompt("please enter your age");
var height = prompt("Please enter your height in centimeters");
var pet = prompt("please enter the name of your pet");

// CONDITIONS
var namecond = null;
var agecond = null;
var heightcond = null;
var petcond = null;

// LOGIC
if (fname[0] === lname[0]) {
  namecond = true;
}else {
  namecond = false;
}

if (age > 20 && age < 30) {
  agecond = true;
}else {
  agecond = false;
}

if (height >= 170) {
  heightcond = true;
}else {
  heightcond = false;
}

if (pet[pet.length-1] === "y") {
  petcond = true;
}else {
  petcond = false;
}

// OUTPUT
if (namecond && agecond && heightcond && petcond) {
  console.log("Here's your secret message");
}
else {
  console.log("Nothing to see here");
}
// The Spy is between the Age of 20 and 30 (exclusive of 20 and 30)
// The Spy is at least 170 centimeters tall.
// The Spy has a pet name that ends with the letter "y".
// We are going to leave this project a little more open-ended, but if you feel like
// you need more guidance, check out the solution walkthrough videos! But believe it or not,
// we've actually covered everything you need to know to complete this task. I would suggest
// you use Javascript to prompt the user for information and set these to variables. Then
// use these variables to check for the four conditions to all be true. It's up to you what
// the secret message is!
//
// A spy with the following information should see your secret message:
//
// Jose Johnson
// 26 years old
// 175 cm tall
// Pet name is "Sammy"
// Keep in mind you can ask the question prompts in whatever order you want, you can
// even separate asking for first name and then another prompt for last name
//
// Also remember to switch out the script src to your own .js file! Right now it's
// connected to Part8.js which contains the solutions
