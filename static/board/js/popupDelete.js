function popupDelete(popup, success_url) {
    popup.onsubmit = function (event) {
        event.preventDefault();
        fetch(this.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": this.querySelector("[name=csrfmiddlewaretoken]").value,
            },
        })
            .then((response) => {
                if (response.ok) {
                    window.opener.location.href = success_url;
                    window.close();
                } else {
                    alert("Failed to delete the object.");
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                alert("An error occurred.");
            });
    };
}
