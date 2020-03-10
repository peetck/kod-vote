/* datetime picker  */
$('#datetimepicker1').datetimepicker({
    locale: 'th',
});
$('#datetimepicker2').datetimepicker({
    locale: 'th',
    minDate: moment($("#datetimepicker1").find("input").val(), "DD/MM/YYYY H:m")
});
$('#datetimepicker1').on("change.datetimepicker", function(e) {
    let date = e.date.clone();
    $('#datetimepicker2').datetimepicker("minDate", date);
    // set value to preview
    $("#poll-start-date").html($("#datetimepicker1").find("input").val());
});

$('#datetimepicker2').on("change.datetimepicker", function(e) {
    // set value to preview
    $("#poll-end-date").html($("#datetimepicker2").find("input").val());
});

/* show file name on input:file */
$('#input-file').on('change',function(){
    //get the file name
    var fileName = $(this).val().split('\\').pop();
    //replace the "Choose a file" label
    $(this).next('.custom-file-label').html(fileName);
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#preview').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function truncatechars(text, lim) {
    if (text.length > lim){
        return text.substring(0, lim - 1) + "...";
    }
    return text;
}

$("#input-file").change(function() {
    readURL(this);
});
$("#poll-subject").on('input', function() {
    var text = truncatechars($("#poll-subject").val(), 25);
    $("#card-title").html(text);
});

$("#poll-detail").on('input', function() {
    var text = truncatechars($("#poll-detail").val(), 20);
    $("#card-detail").html(text);
});

$('#poll-password').on('input', function(){
    var text = $('#poll-password').val();
    if (String(text).localeCompare('') === 0){
        $('#password-status').html('');
    }
    else{
        $('#password-status').html('<i class="fa fa-lock" aria-hidden="true"></i>');
    }
});