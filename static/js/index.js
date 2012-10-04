var dropbox;
$(document).ready(function() {
  dropbox = document.getElementById("dropbox")

  // init event handlers
  dropbox.addEventListener("dragenter", dragEnter, false);
  dropbox.addEventListener("dragexit", dragExit, false);
  dropbox.addEventListener("dragover", dragOver, false);
  dropbox.addEventListener("drop", drop, false);
});

var dragEnter = function(evt) {
  evt.stopPropagation();
  evt.preventDefault();
};

var dragExit = function(evt) {
  evt.stopPropagation();
  evt.preventDefault();
};

var dragOver = function(evt) {
  evt.stopPropagation();
  evt.preventDefault();
};

var drop = function(evt) {
  evt.stopPropagation();
  evt.preventDefault();

  var files = evt.dataTransfer.files;
  var count = files.length;

  // Only call the handler if 1 or more files was dropped.
  if (count > 0)
    handleFiles(files);
};

var handleFiles = function(files) {
  var file = files[0];

  document.getElementById("droplabel").innerHTML = "Processing " + file.name;

  var reader = new FileReader();

  // init the reader event handlers
  reader.onload = handleReaderLoad;

  // begin the read operation
  reader.readAsDataURL(file);
};

function handleReaderLoad(evt) {
  var img = document.getElementById("preview");
  img.src = evt.target.result;
}