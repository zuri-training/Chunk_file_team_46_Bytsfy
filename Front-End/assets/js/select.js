
// Select all checkboxes: Line 120 - 134 on dashboard.html

function toggle(boxcontrol, selector) {
    const combinedSelector = selector + ' .saved-check';
    //let checkboxes = document.getElementsByTagName('input'); this worked too
    const checkboxes = document.querySelectorAll(combinedSelector);

    for (var i = 0; i < checkboxes.length; i++) {
        //  if (checkboxes[i] != boxcontrol && checkboxes[i].className == boxcontrol.className) {
        if (checkboxes[i] != boxcontrol) {
            checkboxes[i].checked = boxcontrol.checked;
        }
    }
}


 // Basic See More Button: line 493 - 496 on saved_files.html

 let button = document.getElementById('seeMore');
 let content = document.getElementById('contentDiv');
 content.className = 'hideContent';

 button.addEventListener('click', function() {
    
     if (content.className === 'hideContent') {
        // content.classList.remove('hideContent');
         content.className = 'showContent';
         button.textContent = 'Show less';
     } else {
         content.className = 'hideContent';
         button.textContent = 'See more';
     }

 });
