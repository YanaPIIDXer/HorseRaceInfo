window.onload = () => {
    const start = new Date();
    const end = new Date();
    start.setDate(end.getDate() - 7);
    $("#start_date").val(dateToString(start));
    $("#end_date").val(dateToString(end));
}

const dateToString = (date) => {
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return year + "-" + ("00" + month).slice(-2) + "-" + ("00" + day).slice(-2);
}

const onSubmit = () => {
    const result = window.confirm("情報収集を開始しますか？");
    if (!result) { return; }

    $("#submit_button").prop("disabled", true);
    $.ajax({
        'url': "collect",
        'method': "POST",
        'data': $("form").serializeArray()
    }).done((data) => {
        alert(data["message"]);
        $("#submit_button").prop("disabled", false);
    });
}