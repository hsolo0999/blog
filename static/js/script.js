$('.toolbar a').click(function (e) {
	var command = $(this).data('command');
	if (command == 'h1' || command == 'h2' || command == 'p') {
		document.execCommand('formatBlock', false, command);
	}
	if (command == 'forecolor' || command == 'backcolor') {
		document.execCommand($(this).data('command'), false, $(this).data('value'));
	}
	if (command == 'createlink' || command == 'insertimage') {
		url = prompt('Enter the link here: ', 'http:\/\/');
		document.execCommand($(this).data('command'), false, url);
	} else document.execCommand($(this).data('command'), false, null);
});



function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInput").change(function(){
    readURL(this);
});
