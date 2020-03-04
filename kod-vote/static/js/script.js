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
