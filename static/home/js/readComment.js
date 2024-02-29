function readComment(message_id, url) {
    const csrfToken = $("[name=csrfmiddlewaretoken]").val();
    $(`#message-${message_id} .read-comment`).click(() => {
        $.ajax({
            type: "post",
            headers: { "X-CSRFToken": csrfToken },
            url,
            data: { id: message_id },
            success(data, status, xhr) {
                $(`#message-${message_id}`).hide();
            },
        });
    });
}

function readAllComment(url) {
    const csrfToken = $("[name=csrfmiddlewaretoken]").val();
    $("#all-read-comment").click(() => {
        $.ajax({
            type: "post",
            headers: { "X-CSRFToken": csrfToken },
            url,
            data: { read_all: "true" },
            success(data, status, xhr) {
                $(".message").hide();
            },
        });
    });
}
