document.addEventListener('DOMContentLoaded',function(){
	var data = {
		"comment":"abc"
	}
	var cookies = document.cookie.split(';'),csrfToken;
	//获取cookie
	cookies && cookies.forEach(function(item){
		if(item.split('=')[0] === 'csrftoken' || item.split('=')[0] === ' csrftoken'){
			csrfToken = item.split('=')[1];
		}
	})

	/**
	*ajax
	*/
	var xhr = new XMLHttpRequest();
	xhr.onReadyStatechange = function(){
		if(xhr.readyState === 4){
			if(xhr.status === 200){
				console.log(1111);
				console.log(xhr.responseText);
			} else{
				console.log(2222)
				console.log(xhr.statusText);
			}
		}
	}


	xhr.open('POST', '/api/volume/189/comments/', true);
	xhr.setRequestHeader('Content-Type','application/json');
	if(csrfToken){
		xhr.setRequestHeader('X-CSRFToken',csrfToken);
	}
	xhr.send(JSON.stringify(data));

},false)
