document.addEventListener('DOMContentLoaded',function(){
	var addBtn = document.querySelector('.footer button');
	document.addEventListener('click',function(e){
		if(e.target.nodeName.toLowerCase() === 'button'){
			var ipt = e.target.previousElementSibling.value,sid = document.querySelector('#pageComment').getAttribute('data-id');
			if(ipt){
				addComment(sid,ipt);
			}
		}
	})

	function addCommentContent(content){

	}

	function addComment(id,value){
		var url = '/api/volume/'+id+'/comments/';
		var data = {
			"comment": value
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
		xhr.onreadystatechange = function(){
			if(xhr.readyState === 4){
				if(xhr.status === 201){
					console.log(1111);
					console.log(xhr.responseText);
				} else{
					console.log(2222)
					console.log(xhr.statusText);
				}
			}
		}


		xhr.open('POST', url, true);
		xhr.setRequestHeader('Content-Type','application/json');
		if(csrfToken){
			xhr.setRequestHeader('X-CSRFToken',csrfToken);
		}
		xhr.send(JSON.stringify(data));
	}
	
	function getComments(id,pageInto){
		var url = '/api/volume/' + id +'/comments/';
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
		xhr.onreadystatechange = function(){
			if(xhr.readyState === 4){
				if(xhr.status === 200){
					if(xhr.responseText){
						var results = JSON.parse(xhr.responseText);
						if(results.results){
							var data = results.results,content='';
							data.forEach(function(item){
								content += '<li>'
										  +'      <div class="comment-user-profile">'
										  +'        <img src="static/news/images/img.jpg" alt=""/>'
										  +'      </div>'
										  +'      <div class="comment-detail">'
										  +'        <span class="good">'
										  +'          <svg class="icon-thumb-up">'
										  +'            <use xlink:href="#icon-thumb-up"></use>'
										  +'          </svg>'
										  +'          <em>1170</em>'
										  +'        </span>'
										  +'        <span class="name">' + item.user_name + '</span>'
										  +'        <span class="comment-text">' + item.comment + '</span>'
										  +'        <span class="comment-time">' + item.submit_date.split('T')[0]+ '</span>'
										  +'      </div>'
										  +'    </li>'
							});
							pageInto.querySelector('ul.comment').innerHTML += content;
						}
					}
				} else{
					console.log(xhr.statusText);
				}
			}
		}


		xhr.open('GET', url, true);
		xhr.setRequestHeader('Content-Type','application/json');
		if(csrfToken){
			xhr.setRequestHeader('X-CSRFToken',csrfToken);
		}
		xhr.send();
	};




	FUN = {
	    home: function(pageInto, pageOut, response) {
	    	if(pageInto && response && response.target){
	    		pageInto.setAttribute('data-id',response.target.id);
	    		getComments(189,pageInto);
	    	}
	    	
	    },
	    start: function(page, into_or_out) {
	    	
	    	console.log('start');
	    },
	    end: function(page, into_or_out) {
	    	console.log('end');
	    }
	};

	Mobilebone.rootTransition = FUN;


},false)
