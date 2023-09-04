const ul = document.querySelector("#tags_ul"),
input = document.querySelector("#tags");

let tagsVal = document.getElementById('tags').value
if (tagsVal.length === 0) { tags = [] }
else 
{
    /*let tt = i.target.value*/
    const split_string = tagsVal.split(",");
    tags = split_string;
    document.getElementById('tags').value = '';     
}

createTag();

function createTag(){
    ul.querySelectorAll("li").forEach(li => li.remove());
    document.getElementById('tagval').value=""
    tags.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag } <i class="uit uit-multiply" onclick="remove(this, '${tag}')"></i></li>`;
        ul.insertAdjacentHTML("afterbegin", liTag);
        let licurrent = document.getElementById('tagval').value 
        if(licurrent.length > 1 ){
            document.getElementById('tagval').value= document.getElementById('tagval').value + ","+tag;
        }
        else {
            document.getElementById('tagval').value= tag;
        }        
    });
 
}
function remove(element, tag){
    let index = tags.indexOf(tag);
    if (index > -1) { // only splice array when item is found
        tags.splice(index, 1); 
        element.parentElement.remove(); 
        createTag();  
    }
    
}

function addTag(e){
    if(e.key == "Enter"){
        let tag = e.target.value.replace(/\s+/g, ' ');
        if(tag.length > 1 && !tags.includes(tag)){
            tag.split(',').forEach(tag => {
                    tags.push(tag);
                    createTag();
                });      
        }
        e.target.value = "";
    }
}

input.addEventListener("keyup", addTag);

