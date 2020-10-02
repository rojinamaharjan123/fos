// Vendor Order Action
$(document).ready(function(){
    $('.panel-wrapper').on('click', '.order-action', function(e){
        e.preventDefault();
        var url = $(this).attr('data-href');
        if (url.includes('cancel')){
            var reason = prompt("Why do you want to cancel this order?")
            if(reason != null && reason != ''){
                $.ajax({
                    url: url,
                    method: 'get',
                    data: {
                        'reason': reason
                    },
                    success: function(data){
                        $.toast({
                            heading: "Order Updated",
                            text: data.message,
                            position: 'top-right',
                            loaderBg:'#' + data.bg,
                            icon: data.icon,
                            hideAfter: 3500, 
                            stack: 3
                        });
                        $('.panel-wrapper').load(' .panel-body')
                    }
                })
            }else if(reason == ''){
                alert("You cannot leave the field empty! Please try again.")
            }
        }else{
            $.ajax({
                url: url,
                method: 'get',
                data: '',
                success: function(data){
                    $.toast({
                        heading: "Order Updated",
                        text: data.message,
                        position: 'top-right',
                        loaderBg:'#' + data.bg,
                        icon: data.icon,
                        hideAfter: 3500, 
                        stack: 3
                    });
                    $('.panel-wrapper').load(' .panel-body')
                }
            })
        }
        
    })
})