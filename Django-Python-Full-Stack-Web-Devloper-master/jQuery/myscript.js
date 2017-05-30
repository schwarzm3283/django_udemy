$('h1').on('mouseenter',function(){
  $(this).toggleClass('turnBlue');
});

$('input').eq(1).on('click', function(){
  $('.container').fadeOut(3000);
});
