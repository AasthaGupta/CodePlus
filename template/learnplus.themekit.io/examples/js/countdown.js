(function($) {

  $.fn.tkCountdown = function () {
    this.countdown({
      date: moment().add((this.data('value') || 3), (this.data('unit') || 'hour')).format("MMMM D, YYYY HH:mm:ss"),
      render: function (date) {
      
        if (date.days > 0) {
          $days = '<span class="h5 text-primary">' + date.days  + '</span>days ';
        }
        else {
          $days = '';
        }
        
        if (date.hours > 0) {
          $hours = '<span class="h5 text-primary">' + this.leadingZeros(date.hours)  + '</span> hrs ';
        }
        else {
          $hours = '';
        }

        if (date.min > 0) {
          $min = '<span class="h5 text-primary">' + this.leadingZeros(date.min)  + '</span> min ';
        }
        else {
          $min = '';
        }
        if (date.sec > 0) {
          $sec = '<span class="h5 text-primary">' + this.leadingZeros(date.sec) + '</span> sec';
        }
        else {
          $sec = '';
        }

        this.el.innerHTML = '<p class="pl-1 pr-1">' + $days + $hours + $min + $sec + '</p>';
      }
    });
  };

  $('.countdown').tkCountdown();

}(jQuery));