$(document).ready(function() { 
    $('.rating-plus').click(function() { 
        changeRating(+1, $(this).attr('data-id')); 
    });

    $('.rating-minus').click(function() {
        changeRating(-1, $(this).attr('data-id'));
    });
});

function changeRating(delta, photo_id) {
    $.get('/items/change_rating/', //отправляем get-запрос на сервер
        {
            'photo_id': photo_id,
            'delta': delta
         }, function(data) {//заменяем кол-во лайков на новое
             $('.rating-value[data-id="'+photo_id+'"]').text(data.new_rating);
         }
    )
}
