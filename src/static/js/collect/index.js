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