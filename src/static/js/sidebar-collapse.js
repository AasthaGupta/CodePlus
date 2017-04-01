(function () {
  'use strict;'

  var sidebarCollapseComponent = function () {
    return {
      listeners: [
        '_onClick(click)'
      ],
      _onClick: function (event) {
        event.preventDefault()
        this.toggle()
      },
      toggle: function () {
        var parent = this.element.parentNode
        var submenu = parent.querySelector('ul')

        if (parent.classList.contains('open')) {
          parent.classList.remove('open')
        }
        else if (submenu) {
          var opened = submenu.querySelectorAll('.open')
          opened = Array.prototype.slice.call(opened)
          opened.forEach(function (open) {
            open.classList.remove('open')
          })
          parent.classList.add('open')
        }
      }
    }
  }

  domFactory.handler.register('sidebar-collapse', sidebarCollapseComponent)
})()