console.log("hello");
document.addEventListener('DOMContentLoaded', function(){
document.getElementById('requestView').addEventListener('click', function(e){
    e.preventDefault();
    const url = e.target.href;
    console.log(url);
    
    async function loadView(url) {
        console.log('this step happened');
        try {
            console.log('try');
            const loadRequest = await fetch(url);
            if (!loadRequest.ok) {
                throw new Error('Error! Status: ${loadRequest.status}');
            }
        console.log(loadRequest);
        } catch (error) {
            console.error('Error:', error);
        }
    };
});
});
