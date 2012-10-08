var file;
/* This following should be wrapped in $(document).ready(function() { ... }); */
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
	// All the File APIs are supported.
}
else {
	alert('The File APIs are not fully supported in this browser.');
}


function handleFileSelect(evt) {
	evt.stopPropagation();
	evt.preventDefault();

	var files = evt.dataTransfer.files; // FileList object.
	// files is a FileList of File objects.
	file = files[0];
	var output = escape(file.name) + ' (' + file.type + ') - ' + file.size + ' bytes';
	/* why not use jQuery for this? */
	document.getElementById('message').innerHTML = output;

	sendFile(file);
}

function sendFile(f){
	var form = new FormData();
	form.append("file", f);
	prepare_ajax();
	$.ajax({
		url: "/upload/",
		type: "POST",
		data: form,
		processData: false,  // tell jQuery not to process the data
		contentType: false   // tell jQuery not to set contentType
	});
}

function handleDragOver(evt) {
	evt.stopPropagation();
	evt.preventDefault();
	evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}

function handleDragEnter(evt){
	evt.stopPropagation();
	evt.preventDefault();

	/* why is output its own variable? */
	var output = 'Let Go!';
	/* why not use jQuery for this? */
	document.getElementById('message').innerHTML = output;
}

function handleDragExit(evt){
	evt.stopPropagation();
	evt.preventDefault();

	var output = 'Drop File Here!';
	document.getElementById('message').innerHTML = output;
}

/* This following should be wrapped in $(document).ready(function() { ... }); */
/* NIT: more conventional names would be onDragOver and onDragEnter etc */
// Setup the drag and drop listeners.
var dropZone = document.getElementById('dropbox');
dropZone.addEventListener('dragover', handleDragOver, false);
dropZone.addEventListener('dragenter', handleDragEnter, false);
dropZone.addEventListener('dragexit', handleDragExit, false);
dropZone.addEventListener('drop', handleFileSelect, false);