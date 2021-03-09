
 const ele = document.querySelectorAll('#abcd');

 ele.forEach(element => {
     element.addEventListener('click',()=>{
         const elee = document.querySelector(`#abc${element.value}`)
         elee.classList.remove("d-none");
         const haha = document.querySelectorAll('.haha')
         haha.forEach(ele => {
             if (elee === ele){
                 ele.children[1].play()
                 console.log("Playing the Lesson that is selected")
             }else{
                 ele.classList.add('d-none')
                 ele.children[1].pause()
                 console.log("Pausing the Lessons that are not selected")
             }
         });
     })
 });