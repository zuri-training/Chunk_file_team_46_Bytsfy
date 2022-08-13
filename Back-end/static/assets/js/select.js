
// Select all checkboxes: Line 120 - 134 on dashboard.html

function toggle(boxcontrol) {
    //let checkboxes = document.getElementsByTagName('input'); this worked too but this takes all input boxes on the page.
    // Every input elements you want the checkbox control to pick should have the class "saved-check" 
    // Please use separate class name for input boxes you do not want the toggle to pick

    let checkboxes = document.querySelectorAll('.saved-check');

    for (var i = 0; i < checkboxes.length; i++) {
        //  if (checkboxes[i] != boxcontrol && checkboxes[i].className == boxcontrol.className) {
        if (checkboxes[i] != boxcontrol) {
            checkboxes[i].checked = boxcontrol.checked;
        }
    }
}


 // Basic See More Button: line 289 - 309 on dashboard.html

 let button = document.getElementById('seeMore');
 let content = document.getElementById('contentDiv');
 
 button.addEventListener('click', function() {

     if (content.className === 'hideContent') {
        // content.classList.remove('hideContent');
         content.className = 'showContent';
         button.textContent = 'Show less';
     } else {
         content.className = 'hideContent';
         button.textContent = 'Show more';
     }

 });
