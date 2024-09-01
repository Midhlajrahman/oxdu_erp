$(document).ready(function() {
    
    $('#course-select').change(function(){
        var value = $(this).val()
        if (value !== 'all-courses') {
            window.location.href = value;
        }
    })
});