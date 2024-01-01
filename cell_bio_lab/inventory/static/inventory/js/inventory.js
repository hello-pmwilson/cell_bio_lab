// $(document).ready(function() {
//     console.log('iteration 1');

//     //on load, load default content
//     let defaultURL = $("#defaultURL").attr('href') 
//     loadContent(defaultURL);

//     //on link click, load content dynmically
//     $("#inventory").click(function(e) {
//         e.preventDefault();
//         let url = e.target.href;

//         loadContent(url);
//     })

//     $("#requests").click(function(e) {
//         e.preventDefault();
//         let url = e.target.href;

//         loadContent(url);
//     })   
    
//     $("#addItem").click(function(e) {
//         e.preventDefault();
//         let url = e.target.href;

//         loadContent(url);
//     })   
    
//     //function, load content into the #content div dynamically given a url
//     function loadContent(url) {
//     $('#content').load(url);
//     }
// });