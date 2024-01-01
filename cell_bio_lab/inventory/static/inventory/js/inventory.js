$(document).ready(function() {
    console.log('iteration 1');
    $("#inventory").click(function(e) {
        e.preventDefault();
        let url = e.target.href;

        loadContent(url);
    })

    $("#requests").click(function(e) {
        e.preventDefault();
        let url = e.target.href;

        loadContent(url);
    })   
    
    $("#addItem").click(function(e) {
        e.preventDefault();
        let url = e.target.href;

        loadContent(url);
    })   
    
    function loadContent(url) {
    $('#content').load(url);
    }
});