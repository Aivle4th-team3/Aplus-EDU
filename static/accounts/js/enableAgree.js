new Vue({
    delimiters: ["[[", "]]"],
    el: "#consent",
    data: {
        personalOfUse: false,
        termsOfUse: false,
    },
    computed: {
        isDisabled() {
            return !(this.personalOfUse && this.termsOfUse);
        },
    },
});
