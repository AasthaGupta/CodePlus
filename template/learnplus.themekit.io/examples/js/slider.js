(function ($) {
    "use strict";
    var rangeSlider = document.getElementById('slider-range');

    noUiSlider.create(rangeSlider, {
        start: [ 1 ],
        step: 1,
        range: {
            'min': [  1 ],
            'max': [ 15 ]
        }
    });
    var stepSliderValueElement = document.getElementById('slider-range-value');

    rangeSlider.noUiSlider.on('update', function( values, handle ) {
        stepSliderValueElement.innerHTML = values[handle];
    });

})(jQuery);