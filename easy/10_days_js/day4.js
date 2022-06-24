function getCount(objects){
    var total = 0;
    objects.forEach( obj => {
        if(obj['x'] == obj['y']){
            total++
        }
    })
    return total

}