var sidebarToggle=document.querySelectorAll('[data-toggle="sidebar"]');sidebarToggle=Array.prototype.slice.call(sidebarToggle),sidebarToggle.forEach(function(e){e.addEventListener("click",function(e){var r=e.currentTarget.getAttribute("data-target")||"#default-drawer",t=document.querySelector(r);t&&t.mdkDrawer.toggle()})});
//# sourceMappingURL=main.min.js.map
