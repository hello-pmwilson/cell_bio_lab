document.getElementById('requestView').addEventListener('click', function(e){
    e.preventDefault();
    let url = e.target.href;
    console.log(url);

    loadContent(url);
    console.log('after');
});

function loadContent(url) {
    $('#content').load(url);
}

$('#tabs').click(function() {
    console.log(click);
})

console.log("bitches");