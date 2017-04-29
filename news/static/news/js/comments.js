document.addEventListener('DOMContentLoaded',function(){
	
	/**
	*  回调函数
	*	data---response数据
	*   type---请求类型   post / get
	*/  
	function commentsCB(data,type){
		var data = JSON.parse(data);
		if(data){
				var content='',
				commentContainer = document.querySelector('#pageComment ul.comment');
			if(type === 'get'){
				var results = data.results;
				if(results && results.length){
					results.forEach(function(item){
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
								  +'    </li>';
					});
					commentContainer.innerHTML = content;
				}else{
					commentContainer.innerHTML = '<li class="no-comment">还没有评论呢！</li>';
				}
				
			}else if(type === 'post'){
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
						  +'        <span class="name">' + data.user_name + '</span>'
						  +'        <span class="comment-text">' + data.comment + '</span>'
						  +'        <span class="comment-time">' + data.submit_date.split('T')[0]+ '</span>'
						  +'      </div>'
						  +'    </li>';
			    var noComment = commentContainer.querySelector('.no-comment');
			    if(!noComment){
			    	commentContainer.innerHTML = content + commentContainer.innerHTML;
			    }else{
			    	commentContainer.innerHTML = content;
			    }
			    
			}
			
		}
	}

	function addComment(id,value){
		var url = '/api/volume/'+id+'/comments/';
		var data = {
			"comment": value
		}
		var cookies = document.cookie.split(';'),csrfToken;
		cookies && cookies.forEach(function(item){
			if(item.split('=')[0] === 'csrftoken' || item.split('=')[0] === ' csrftoken'){
				csrfToken = item.split('=')[1];
			}
		})
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function(){
			if(xhr.readyState === 4){
				if(xhr.status === 201){
					if(xhr.responseText){
						commentsCB(xhr.responseText,'post');
					}
				} else{
					alert('提交评论失败');
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
	
	function getComments(id){
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
						commentsCB(xhr.responseText,'get');
					}
				} else{
					alert('获取评论列表失败');
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

	var addBtn = document.querySelector('#pageComment .footer button');
	
	addBtn.addEventListener('click',function(e){
		var ipt = e.target.previousElementSibling.value,
			sid = document.querySelector('#pageComment').getAttribute('data-id');
			if(ipt){
				addComment(sid,ipt);
				e.target.previousElementSibling.value = '';
			}
	})


	FUN = {
	    home: function(pageInto, pageOut, options) {
	    	
	    },
	    start: function(page, into_or_out,options) {
	    	
	    },
	    end: function(page, into_or_out,options) {
	    	
	    },
	    callback: function(pageInto,pageOut,options){
	    	if(pageInto && options && options.target){
	    		pageInto.setAttribute('data-id',options.target.id);
    			getComments(options.target.id);
    			window.localStorage.setItem('commentId',options.target.id);
	    	}else{
	    		var id = window.localStorage.getItem('commentId');
	    		pageInto.setAttribute('data-id',id);
    			getComments(id);
	    	}
	    },
	    fallback: function(pageInto,pageOut,options){
	    	pageOut.setAttribute('data-id','');
			document.querySelector('#pageComment ul.comment').innerHTML = '';
	    }
	};

	Mobilebone.rootTransition = FUN;


},false)
