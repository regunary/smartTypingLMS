(function ($) {
  "use strict";
  $(window).on("load", function (event) {
    $(".js-preloader").delay(500).fadeOut(500);
  });
  $(".searchBtn").on("click", function () {
    $(".search-box-full").addClass("open");
    $("#search_field").focus();
  });
  $(".close-search_box").on("click", function () {
    $(".search-box-full").removeClass("open");
  });
  $(".file-upload").on("change", ".file-upload-field", function () {
    $(this)
      .parent(".file-upload-wrapper")
      .attr(
        "data-text",
        $(this)
          .val()
          .replace(/.*(\/|\\)/, "")
      );
  });
  $(".counter-item").appear(function () {
    var element = $(this);
    var timeSet = setTimeout(function () {
      if (element.hasClass("counter-item")) {
        element.find(".counter-value").countTo();
      }
    });
  });
  $("[data-countdown]").each(function () {
    var $this = $(this),
      finalDate = $(this).data("countdown");
    $this.countdown(finalDate, function (event) {
      $this.html(
        event.strftime(
          '<span class="cdown day"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hours</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>mins</p></span> <span class="cdown second"><span class="time-count">%S</span> <p>secs</p></span>'
        )
      );
    });
  });
  if ($(".skills").length) {
    var offsetTop = $(".skills").offset().top;
    $(window).scroll(function () {
      var height = $(window).height();
      if ($(window).scrollTop() + height > offsetTop) {
        $(".skillbar").each(function () {
          $(this)
            .find(".skillbar-bar")
            .animate({ width: $(this).attr("data-percent") }, 1500);
        });
      }
    });
  }
  var minVal = 1,
    maxVal = 20;
  $(".increaseQty").on("click", function () {
    var $parentElm = $(this).parents(".qtySelector");
    $(this).addClass("clicked");
    setTimeout(function () {
      $(".clicked").removeClass("clicked");
    }, 100);
    var value = $parentElm.find(".qtyValue").val();
    if (value < maxVal) {
      value++;
    }
    $parentElm.find(".qtyValue").val(value);
  });
  $(".decreaseQty").on("click", function () {
    var $parentElm = $(this).parents(".qtySelector");
    $(this).addClass("clicked");
    setTimeout(function () {
      $(".clicked").removeClass("clicked");
    }, 100);
    var value = $parentElm.find(".qtyValue").val();
    if (value > 1) {
      value--;
    }
    $parentElm.find(".qtyValue").val(value);
  });
  $(".mobile-top-bar").on("click", function () {
    $(".header-top-right").addClass("open");
  });
  $(".close-header-top").on("click", function () {
    $(".header-top-right").removeClass("open");
  });
  var wind = $(window);
  var sticky = $(".header-wrap");
  wind.on("scroll", function () {
    var scroll = wind.scrollTop();
    if (scroll < 100) {
      sticky.removeClass("sticky");
    } else {
      sticky.addClass("sticky");
    }
  });
  $(".mobile-menu a").on("click", function () {
    $(".main-menu-wrap").addClass("open");
    $(".mobile-bar-wrap.style2 .mobile-menu").addClass("open");
  });
  $(".mobile_menu a").on("click", function () {
    $(this).parent().toggleClass("open");
    $(".main-menu-wrap").toggleClass("open");
  });
  $(".menu-close").on("click", function () {
    $(".main-menu-wrap").removeClass("open");
  });
  $(".mobile-top-bar").on("click", function () {
    $(".header-top").addClass("open");
  });
  $(".close-header-top button").on("click", function () {
    $(".header-top").removeClass("open");
  });
  var $offcanvasNav = $(".main-menu"),
    $offcanvasNavSubMenu = $offcanvasNav.find(".sub-menu");
  $offcanvasNavSubMenu
    .parent()
    .prepend(
      '<span class="menu-expand"><i class="las la-angle-down"></i></span>'
    );
  $offcanvasNavSubMenu.slideUp();
  $offcanvasNav.on("click", "li a, li .menu-expand", function (e) {
    var $this = $(this);
    if (
      $this
        .parent()
        .attr("class")
        .match(/\b(has-children|sub-menu)\b/) &&
      ($this.attr("href") === "#" || $this.hasClass("menu-expand"))
    ) {
      e.preventDefault();
      if ($this.siblings("ul:visible").length) {
        $this.siblings("ul").slideUp("slow");
      } else {
        $this.closest("li").siblings("li").find("ul:visible").slideUp("slow");
        $this.siblings("ul").slideDown("slow");
      }
    }
    if (
      $this.is("a") ||
      $this.is("span") ||
      $this.attr("class").match(/\b(menu-expand)\b/)
    ) {
      $this.parent().toggleClass("menu-open");
    } else if (
      $this.is("li") &&
      $this.attr("class").match(/\b('has-children')\b/)
    ) {
      $this.toggleClass("menu-open");
    }
  });
  $(".has-subcat").on("click", function () {
    $(this).toggleClass("open");
    $(this).find(".subcategory").slideToggle(500);
    $(this).siblings().find(".subcategory").slideUp(500);
    $(this).siblings().removeClass("open");
  });
  $("#slider-range_one").slider({
    range: true,
    min: 0,
    max: 400,
    values: [10, 300],
    slide: function (event, ui) {
      $("#amount_one").val("$" + ui.values[0] + " - " + "$" + ui.values[1]);
    },
  });
  $(" #amount_one").val(
    "$" +
      $("#slider-range_one").slider("values", 0) +
      " - " +
      "$" +
      $("#slider-range_one").slider("values", 1)
  );
  var hero_slider_one = new Swiper(".hero-slider-one", {
    spaceBetween: 0,
    slidesPerView: 1,
    loop: true,
    autoHeight: true,
    autoplay: { delay: 9000, disableOnInteraction: true },
    speed: 1500,
    navigation: { nextEl: ".hero-one-next", prevEl: ".hero-one-prev" },
  });
  var course_slider_one = new Swiper(".course-slider", {
    spaceBetween: 30,
    autoplay: { delay: 3000, disableOnInteraction: true },
    speed: 1500,
    loop: true,
    pagination: { el: ".course-pagination", clickable: true },
    breakpoints: {
      0: { slidesPerView: 1, spaceBetween: 30 },
      576: { slidesPerView: 2, spaceBetween: 20 },
      768: { slidesPerView: 2, spaceBetween: 20 },
      992: { slidesPerView: 2.5, spaceBetween: 25 },
      1200: { slidesPerView: 3.5, spaceBetween: 25 },
    },
  });
  var tour_slider_one = new Swiper(".event-slider", {
    spaceBetween: 30,
    autoplay: { delay: 3000, disableOnInteraction: true },
    speed: 1500,
    loop: true,
    pagination: { el: ".course-pagination", clickable: true },
    breakpoints: {
      0: { slidesPerView: 1, spaceBetween: 30 },
      768: { slidesPerView: 1, spaceBetween: 20 },
      992: { slidesPerView: 1, spaceBetween: 25 },
      1200: { slidesPerView: 2, spaceBetween: 0 },
    },
  });
  var tour_slider_one = new Swiper(".partner-slider", {
    spaceBetween: 30,
    autoplay: { delay: 3000, disableOnInteraction: true },
    speed: 1500,
    centeredSlides: true,
    loop: true,
    navigation: { nextEl: ".partner-next", prevEl: ".partner-prev" },
    breakpoints: {
      0: { slidesPerView: 3, spaceBetween: 30 },
      768: { slidesPerView: 3, spaceBetween: 20 },
      992: { slidesPerView: 4, spaceBetween: 20 },
      1200: { slidesPerView: 6, spaceBetween: 30 },
    },
  });
  var tour_slider_one = new Swiper(".gallery-slider-one", {
    spaceBetween: 30,
    slidesPerView: 1,
    speed: 1500,
    loop: true,
    navigation: { nextEl: ".gallery-one-next", prevEl: ".gallery-one-prev" },
  });
  var mySwiper = new Swiper(".gallery-slider-two", {
    speed: 1000,
    loop: true,
    autoplay: {
      delay: 4000,
      waitForTransition: true,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".gallery-pagination",
      clickable: true,
      renderBullet: function (index, className) {
        return (
          '<span class="' +
          className +
          '">' +
          '<svg class="fp-arc-loader" width="30" height="30" viewBox="0 0 16 16">' +
          '<circle class="path" cx="8" cy="8" r="5.5" fill="none" transform="rotate(-90 8 8)" stroke="#3469E5"' +
          'stroke-opacity="1" stroke-width="1.5px"></circle>' +
          '<circle cx="8" cy="8" r="3" fill="#000"></circle>' +
          "</svg></span>"
        );
      },
    },
  });
  var galleryThumbs = new Swiper(".gallery-thumbs", {
    spaceBetween: 20,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    breakpoints: {
      0: { slidesPerView: 3, spaceBetween: 20 },
      768: { slidesPerView: 3, spaceBetween: 20 },
      992: { slidesPerView: 3, spaceBetween: 20 },
      1200: { slidesPerView: 4, spaceBetween: 20 },
    },
  });
  var galleryTop = new Swiper(".gallery-top", {
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: { swiper: galleryThumbs },
  });
  var testimonial_one = new Swiper(".testimonial-slider-one", {
    slidesPerView: 1,
    loop: true,
    speed: 1500,
    autoplay: { delay: 4000, disableOnInteraction: true },
    pagination: { el: ".testimonial-pagination", clickable: true },
    breakpoints: {
      0: { slidesPerView: 1, spaceBetween: 20 },
      768: { slidesPerView: 2, spaceBetween: 25 },
      992: { slidesPerView: 2, spaceBetween: 25 },
      1200: { slidesPerView: 3, spaceBetween: 25 },
    },
  });
  var testimonial_two = new Swiper(".testimonial-slider-two", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    speed: 1500,
    pagination: { el: ".testimonial-pagination-two", clickable: true },
  });
  var testimonial_one = new Swiper(".promo-slider", {
    spaceBetween: 30,
    loop: true,
    speed: 1500,
    navigation: { nextEl: ".promo-button-next", prevEl: ".promo-button-prev" },
    breakpoints: {
      0: { slidesPerView: 1, spaceBetween: 20 },
      768: { slidesPerView: 2, spaceBetween: 20 },
      992: { slidesPerView: 2, spaceBetween: 20 },
      1200: { slidesPerView: 2, spaceBetween: 30 },
    },
  });
  var testimonial_one = new Swiper(".team-slider", {
    spaceBetween: 30,
    loop: true,
    speed: 1500,
    pagination: { el: ".swiper-pagination", clickable: true },
    breakpoints: {
      0: { slidesPerView: 1, spaceBetween: 20 },
      768: { slidesPerView: 2, spaceBetween: 20 },
      992: { slidesPerView: 1, spaceBetween: 20 },
      1200: { slidesPerView: 2, spaceBetween: 30 },
    },
  });
  $(".video-play").magnificPopup({
    type: "iframe",
    mainClass: "mfp-fade",
    preloader: true,
  });
  $(window).on("scroll", function (event) {
    if ($(this).scrollTop() > 600) {
      $(".back-to-top").fadeIn(200);
    } else {
      $(".back-to-top").fadeOut(200);
    }
  });
  $(".back-to-top").on("click", function (event) {
    event.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, 1500);
  });
})(jQuery);
