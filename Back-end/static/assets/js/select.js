
// Select all checkboxes: Line 120 - 134 on dashboard.html

<<<<<<< HEAD
function toggle(boxcontrol, selector) {
    const combinedSelector = selector + ' .saved-check';
    //let checkboxes = document.getElementsByTagName('input'); this worked too
    const checkboxes = document.querySelectorAll(combinedSelector);
=======
function toggle(boxcontrol) {
    //let checkboxes = document.getElementsByTagName('input'); this worked too but this takes all input boxes on the page.
    // Every input elements you want the checkbox control to pick should have the class "saved-check" 
    // Please use separate class name for input boxes you do not want the toggle to pick

    let checkboxes = document.querySelectorAll('.saved-check');
>>>>>>> 0181990a5bbf9ec351d286fea98ad6600d65471f

    for (var i = 0; i < checkboxes.length; i++) {
        //  if (checkboxes[i] != boxcontrol && checkboxes[i].className == boxcontrol.className) {
        if (checkboxes[i] != boxcontrol) {
            checkboxes[i].checked = boxcontrol.checked;
        }
    }
}


<<<<<<< HEAD
 // Basic See More Button: line 493 - 496 on saved_files.html

 let button = document.getElementById('seeMore');
 let content = document.getElementById('contentDiv');
 content.className = 'hideContent';

 button.addEventListener('click', function() {
    
=======
 // Basic See More Button: line 289 - 309 on dashboard.html

 let button = document.getElementById('seeMore');
 let content = document.getElementById('contentDiv');
 
 button.addEventListener('click', function() {

>>>>>>> 0181990a5bbf9ec351d286fea98ad6600d65471f
     if (content.className === 'hideContent') {
        // content.classList.remove('hideContent');
         content.className = 'showContent';
         button.textContent = 'Show less';
     } else {
         content.className = 'hideContent';
<<<<<<< HEAD
         button.textContent = 'See more';
=======
         button.textContent = 'Show more';
>>>>>>> 0181990a5bbf9ec351d286fea98ad6600d65471f
     }

 });
