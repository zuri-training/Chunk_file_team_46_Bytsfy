 /**Javacript - CSV and JSon Chunking Pages*/

 let splitType = document.getElementById('splittype');
 let byLine = document.getElementById('byline');
 let bySize = document.getElementById('bysize');
 

 byLine.style.display = 'none';
 bySize.style.display = 'none';  

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