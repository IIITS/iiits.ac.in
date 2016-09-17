$(document).ready(function(){
	
	$("#news").show();
	$("#sn-news").addClass('iiits-sidenav-hover');
	$("#notices").hide();
	$("#archives").hide();
	$("#tenders").hide();
	$('#centres').show();
	$("#sn-centres").addClass('iiits-sidenav-hover');
	$('#areas').hide();
	$('#publications').hide();
	$("#portfolio").hide();
	$("#scholars").hide();
	function getParameterByName(name) {
    	var url = window.location.href;
    	name = name.replace(/[\[\]]/g, "\\$&");
    	var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    	if (!results) return null;
    	if (!results[2]) return '';
    	return decodeURIComponent(results[2].replace(/\+/g, " "));
	}	
	function slideTo(id){
		$('html, body').animate({
        scrollTop: $("#"+id).offset().top
    }, 2000);
		$('.iiits-sidenav-hover').removeClass('iiits-sidenav-hover');
		$("#sn-"+id).addClass('iiits-sidenav-hover');
	}
	window.showOnly = function(sid){
		var elems = document.querySelectorAll('[data-type]');
		
		for(var i=0; i< elems.length; i++){
			var elemid = elems[i]['id'].toString();

			if(elemid==sid['id'].toString()){
				$("#"+elemid).show();
				$("#sn-"+elemid).addClass('iiits-sidenav-hover');
			}
			else{
				$("#"+elemid).hide();
				$("#sn-"+elemid).removeClass('iiits-sidenav-hover');
			}
		}
		
	}
	window.collapse =function(cid){
		var elems = document.querySelectorAll('[data-toggle]');
		for(var i=0; i< elems.length; i++){
			var elemid = elems[i]['id'].toString();
			$('#'+elemid).removeClass('in');
		}
		$('#'+cid).addClass('in');
	}
	var tabs = $('*[id^="iiits-tab-link"]');
	var tabslen = tabs.length;
	
	$('#iiits-tab-link-0').addClass('iiits-tab-header-4-active');
	$('#iiits-tab-content-0').show();
	for(i=1; i<tabslen; i++){
		$('#iiits-tab-content-'+i).hide();
	}
	window.tabNavigate = function(num){
		for(i=0; i<tabslen; i++){
			$('#iiits-tab-content-'+i).hide();
		}
		$('.iiits-tab-header-4-active').removeClass('iiits-tab-header-4-active');
		$('#iiits-tab-link-'+num).addClass('iiits-tab-header-4-active');
		$('#iiits-tab-content-'+num).show();
		
	}
	$('#iiits-faculty-bio').addClass('iiits-tab-header-4-active');
	$('#iiits-faculty-bio-content').show();
	$('#iiits-faculty-publications-content').hide();
	$('#iiits-faculty-teaching-content').hide();
	$('#iiits-faculty-bio').click(function(){
			$(this).addClass('iiits-tab-header-4-active');	
			$('#iiits-faculty-teaching').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-publications').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-bio-content').show();
			$('#iiits-faculty-publications-content').hide();
			$('#iiits-faculty-teaching-content').hide();
		});
		$('#iiits-faculty-teaching').click(function(){
			$(this).addClass('iiits-tab-header-4-active');
			$('#iiits-faculty-bio').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-publications').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-bio-content').hide();
			$('#iiits-faculty-publications-content').hide();
			$('#iiits-faculty-teaching-content').show();
		});
		$('#iiits-faculty-publications').click(function(){
			$(this).addClass('iiits-tab-header-4-active');	
			$('#iiits-faculty-bio').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-teaching').removeClass('iiits-tab-header-4-active');
			$('#iiits-faculty-bio-content').hide();
			$('#iiits-faculty-publications-content').show();
			$('#iiits-faculty-teaching-content').hide();

	});
	var page = getParameterByName('page');
	$('#pb-'+page).addClass('active');
	$('#login-form-container').hide();
	$('#open-options').on('click', function(){
		console.log('hello');
		if(hasClass(document.getElementById('open-options'), 'fa-bars')){
			$('#open-options').removeClass('fa-bars').addClass('fa-arrow-right').css('color','#333');
			$('#login-form-container').show();
		}
		else if(hasClass(document.getElementById('open-options'), 'fa-arrow-right')){
			$('#open-options').removeClass('fa-arrow-right').addClass('fa-bars').css('color','white');
			$('#login-form-container').hide();
		}	
	});
	function hasClass(element, cls) {
    	return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
	}
	$('#login-form').validate({
   		rules: {
     	    username: "required",
     	    password:"required"
        },
        messages: {
        	username:"Please enter your email",
        	password:"Please enter the password",
        },
        submitHandler: function(form){
        	$.ajax({url:'/login/',method:'POST',data:form.serialize(),
        		    success:function(jdata){
        		    	var data = $.parseJSON(jdata);
        		    	if(data["code"]==300){
        		    		document.getElementById('login-error-message').innerHTML=data["message"];
        		    	}
        		    	else{
        		    		window.location.reload();
        		    	}
        		    }
        	})
        }
 });
});