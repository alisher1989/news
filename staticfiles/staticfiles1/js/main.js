$(document).on("click",".toggle-password",(function(){return"password"===$("#password-input").attr("type")?($(this).addClass("view"),$("#password-input").attr("type","text")):($(this).removeClass("view"),$("#password-input").attr("type","password")),!1})),jQuery((function(o){o("#phone").mask("999 (999) 99 99 99")})),$(document).on("click",".toggle-modal",(function(){$(".modal.add-modal").addClass("show"),$("body").addClass("hidden")})),$(document).on("click",".modal-close",(function(){$(".modal.add-modal").removeClass("show"),$("body").removeClass("hidden")})),$(document).on("click",".small-btn.ok-btn",(function(){$(".modal.status-modal.ok").removeClass("show")})),$(document).on("click",".small-btn.error-btn",(function(){$(".modal.status-modal.error").removeClass("show")}));