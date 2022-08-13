 /**Javacript - CSV and JSon Chunking Pages*/

 let splitType = document.getElementById('splittype');
 let byLine = document.getElementById('byline');
 let bySize = document.getElementById('bysize');
 
// Set input box for the options not to show by default until user made his/her choice
 byLine.style.display = 'none';
 bySize.style.display = 'none';  

 // Function to switch the input box on depending on User's choice
 
 function changeSplitType() {
     
   if (splitType.value === 'bsize') {
        byLine.style.display = 'none';
        bySize.style.display = 'block';
    }else if(splitType.value === 'bline') {
        byLine.style.display = 'block';
        bySize.style.display = 'none';   
    }else {
        byLine.style.display = 'none';
        bySize.style.display = 'none';   
    }

}