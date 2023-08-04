// $(document).load(function () {
//     $(".form-control").each(function (index) {
//         if (index > 2) {
//             $(this).hide()
//         }
//     });
// });
$(document).ready(function () {
    var $brand = $("#brand");
    var $brand_model = $("#brand_model");
    var $brand_model_options = $brand_model.find("option");
    $brand.on('click', function () {
            var brand_id = parseInt($(this).val());
            if (brand_id > 0) {
                $brand_model_options.each(function (el) {
                        if (parseInt($(this).data("brandid")) === brand_id) {
                            $(this).show();
                            $brand_model.show();
                        } else {
                            $(this).hide();
                        }
                    }
                )
            } else {
                $brand_model.hide();
                $brand_model_options.hide();
            }
        }
    ).trigger('change');
    var $created_year = $("#id_year_of_create")
    $("#fuel").hide();

    $created_year.on('click', function () {
        if (parseInt($(this).val()) > 0) {
            $("#fuel").show();
        }
    }).trigger('change');


    $("#health").hide();
    var $fuel_type = $("#id_fuel_type");
    $fuel_type.on('click', function () {
        if ($(this).val() !== "") {
            $("#health").show();
        }
    }).trigger('change');

    $("#descriptions").hide();
    var $body_health = $("#id_body_health_type");
    $body_health.on('click', function () {
        if ($(this).val() !== "") {
            $("#descriptions").show();
        }
    }).trigger('change');

    $("#price").hide();
    var $inside_color = $("#inside_color");
    $inside_color.on('click', function () {
        if (parseInt($(this).val()) > 0) {
            $("#price").show();
            $("#btn").show();
        }
    }).trigger('change');

    var $price_type = $("#id_type");
    $price_type.on('click', function () {
        $("#btn").show();
        if ($(this).val() === 'I') {
            $("#agreement").hide();
            $("#fixed").hide();
            $("#installments").show();


        } else if ($(this).val() === 'A') {
            $("#agreement").show();
            $("#fixed").hide();
            $("#installments").hide();

        } else {
            $("#agreement").hide();
            $("#fixed").show();
            $("#installments").hide();
        }
    })

})