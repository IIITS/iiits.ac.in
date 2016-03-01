$(document).ready(function(){
	function getParameterByName(name) {
    var url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
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

});