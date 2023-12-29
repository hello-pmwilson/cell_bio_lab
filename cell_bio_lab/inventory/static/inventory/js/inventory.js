console.log("hello change 2");

document.getElementById('requestView').addEventListener('click', function(e){
    e.preventDefault();
    let url = e.target.href;
    console.log(url);

    loadContent(url);
    console.log('after');
    
    // async function loadView(url) {
    //     console.log('this step happened');
    //     try {
    //         console.log('try');
    //         const loadRequest = await fetch(url);
    //         if (!loadRequest.ok) {
    //             throw new Error('Error! Status: ${loadRequest.status}');
    //         }
    //     console.log(loadRequest);
    //     } catch (error) {
    //         console.error('Error:', error);
    //     }
    // };
});

function loadContent(url) {
    console.log('ajax');
    $('#content').load(url);
}