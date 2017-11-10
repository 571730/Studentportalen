function finnFag() {
    var input, filter, ul, li, a, i;
    input = document.getElementById('sokFag');
    filter = input.value.toUpperCase();
    ul = document.getElementById('fagUl');
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++){
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1){
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function fyllAnmeldelse() {
    var txt = '{"anmeldelser":[' +
        '{"vanskGrad":"3","intGrad":"5" },' +
        '{"vanskGrad":"4","intGrad":"1" },' +
        '{"vanskGrad":"2","intGrad":"3" }]}';

    var anmeldelser = JSON.parse(txt).anmeldelser;

    for ( var i = 0; i < anmeldelser.length; i++ ) {
        var anm = anmeldelser[i];
        var $line = $( "<tr></tr>" );
        $line.append( $( "<td></td>" ).html( anm.vanskGrad ) );
        $line.append( $( "<td></td>" ).html( anm.intGrad ) );
        $table.append( $line );
    }

    $table.appendTo( document.body );

// if you want to insert this table in a div with id attribute
// set as "myDiv", you can do this:
   // $table.appendTo( $( "#myDiv" ) );

}