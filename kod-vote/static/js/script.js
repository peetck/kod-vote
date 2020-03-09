var current = new Date()
$('#datetimepicker1').datetimepicker({
    locale: 'th',
    defaultDate : current,
});
$('#datetimepicker2').datetimepicker({
    locale: 'th',
});

$('#datetimepicker1').on("change.datetimepicker", function(e) {
    let date = e.date.clone();
    $('#datetimepicker2').datetimepicker("minDate", date);
});

/* show file name on input:file */
$('#input-file').on('change',function(){
    //get the file name
    var fileName = $(this).val().split('\\').pop();
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName);
});