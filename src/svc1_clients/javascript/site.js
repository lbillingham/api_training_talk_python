$(document).ready(function () {
    var frm = $('form')

    frm.submit(function (e) {

        loadCarDetails()

        e.preventDefault()
        return false
    })
})

function loadCarDetails() {
    //  get car id
    const car_id = $("input[name=car_id]").val()
    // alert(car_id)

    // build url
    const url = "http://localhost:6543/api/autos/" + car_id
    alert(url)

    // TODO: get().done().fail()
    $.get(url).done(function (results){
        alert("success")
    }).fail(function (error) {
        alert("fail")
    })

}

function populateCarData(car) {
    $("#car_details").fadeOut(function () {

        // TODO: populate data


        $("#car_details").fadeIn('slow')
    })
}