$(function () {
  'use strict';
  //Adjust slider height

  var winH = $(window).height(),
    navH = $('#lari-header').innerHeight();
  $('#lari-carousel, .carousel-item').height(winH);
});

// Add background to navbar when scrolled
$(document).ready(function () {
  var scrollTop = 0;
  $(window).scroll(function () {
    scrollTop = $(window).scrollTop();

    if (scrollTop >= 100) {
      $('#lari-header').addClass('scrolled-nav scrolled-height');
    } else if (scrollTop < 100) {
      $('#lari-header').removeClass('scrolled-nav scrolled-height');
    }
  });
  
var hover_off = false;
var hover_count = 1000;

$("#lari-header").mouseover(function() {
    hover_off = false;
    $(this).addClass('scrolled-nav');
});

$("#lari-header").mouseout(function() {
    hover_off = true;
    setTimeout(myMouseOut, hover_count);
});

function myMouseOut() {
    if (hover_off && scrollTop <= 100) {
        $("#lari-header").removeClass('scrolled-nav');
    }
}

  /*Overlay Menu*/
  $('#toggle').click(function () {
    $(this).toggleClass('active');
    $('#overlay').toggleClass('open');
    $('#lari-header').toggleClass('overlay-opened');
    $('body').toggleClass('overlay-opened');
  });

  /*Hover sub menu*/
  $(".hoverzone").hover(function () {
    $(this).children(".sub-menu").addClass("submenu-opened");
  }, function () {
    $(this).children(".sub-menu").removeClass("submenu-opened");
  });

  // Add minus icon for collapse element which is open by default
  $(".collapse.show").each(function(){
    $(this).prev(".card_pagee").find(".fa").addClass("fa-minus").removeClass("fa-plus");
  });
  
  // Toggle plus minus icon on show hide of collapse element
  $(".collapse").on('show.bs.collapse', function(){
    $(this).prev(".card_pagee").find(".fa").removeClass("fa-plus").addClass("fa-minus");
  }).on('hide.bs.collapse', function(){
    $(this).prev(".card_pagee").find(".fa").removeClass("fa-minus").addClass("fa-plus");
  });

});