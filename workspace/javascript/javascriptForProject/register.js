$(document).ready(function(){
    $("#registor").validate({
        rules:{
            fname:{
                requried:true,
                minlenght:10
            }
        }

        }
    )
})
