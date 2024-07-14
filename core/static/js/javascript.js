function mostrarImagen(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var imagenPrev = document.getElementById('imagen-previa');
        imagenPrev.src = reader.result;
        imagenPrev.style.display = 'block';
        imagenPrev.style.height = '20em';
    };
    reader.readAsDataURL(input.files[0]);
    
    var nombreArchivo = input.files[0].name;
    var labelImagen = document.getElementById('label-imagen');
    labelImagen.innerText = nombreArchivo;
}