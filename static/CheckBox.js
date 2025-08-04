function checkbox_01_value(object){
    if($('#checkbox_01').prop('checked')) {
        console.log('checked')
    } 
    else {
        console.log('not checked')
    }

    if(object.checked){
        console.log('checked')
    } 
    else {
        console.log('not checked')
    }
}