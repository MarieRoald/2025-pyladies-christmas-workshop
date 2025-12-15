// Setting up the CodeMirror editor
var editor = CodeMirror(document.querySelector('#editor'), {
    lineNumbers: true,
    value: 'Loading script...',
    mode: 'python'
});
  
// Function to download the code as a file
function saveCodeAs() {
    if (promptFilename = prompt("Save code as", "")) {
        var textBlob = new Blob([editor.getValue()], {type:'text/plain'});
        var downloadLink = document.createElement("a");
        downloadLink.download = promptFilename;
        downloadLink.innerHTML = "Download File";
        downloadLink.href = window.URL.createObjectURL(textBlob);
        downloadLink.click();
    delete downloadLink;
    delete textBlob;
    }
}

function createSaveSvgAnchorTag() {
    let svgCanvas = document.getElementById("turtleSvgCanvas");
    let tempSvgCanvas = svgCanvas.cloneNode(true);
    tempSvgCanvas.removeAttribute("id")

    for (animateTag of tempSvgCanvas.getElementsByTagName("animate")) {
        let attributeName = animateTag.getAttribute("attributeName");
        let attributeValue = animateTag.getAttribute("to");
        animateTag.parentElement.setAttribute(attributeName, attributeValue);
    }
    for (animateTag of tempSvgCanvas.getElementsByTagName("animate")) {
        animateTag.remove();
    }
    tempSvgCanvas.remove()

    const htmlStr = tempSvgCanvas.outerHTML;
    const blob = new Blob([htmlStr], {type: "image/svg+xml"});

    const url = URL.createObjectURL(blob);
    let a = document.createElement("a");
    a.setAttribute("download", "turtle_canvas.svg");
    a.setAttribute("href", url);
    a.innerText = "Download Turtle drawing"
    return a;
}
  
document.getElementById("downloadLink").onclick = saveCodeAs;

function resetEditor() {
    fetch("./example_script.py")
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.text();
        })
        .then(text => editor.setValue(text))
        .catch(error => console.error('Error loading file:', error));
}

function viewOnlyEditor() {
    document.getElementById("outputPane").style.display = "none";
    document.getElementById("inputPane").style.display = "flex";
}

function viewEditorAndOutput() {
    document.getElementById("outputPane").style.display = "flex";
    document.getElementById("inputPane").style.display = "flex";
}

function viewOnlyOutput() {
    document.getElementById("outputPane").style.display = "flex";
    document.getElementById("inputPane").style.display = "none";
}