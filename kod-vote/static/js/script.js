$(function () {
    $('#datetimepicker1').datetimepicker({
        locale: 'th',
        minDate : new Date(),
        defaultDate: new Date()
    });
    $('#datetimepicker2').datetimepicker({
        locale: 'th',
        minDate : new Date()
    });
});

/* Auto popup modal if poll request password */
$('#myModal').modal({
    backdrop: 'static',
    keyboard: false
});

/* show file name on input:file */
$('#input-file').on('change',function(){
    //get the file name
    var fileName = $(this).val().split('\\').pop();
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName);
})